import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

# Carregar Chave API
load_dotenv()

def main():
    # Carregar os PDFs da pasta 'inputs'
    print("📖 Localizando e lendo os arquivos PDF na pasta 'inputs'...")
    try:
        # O DirectoryLoader varre a pasta e o PyPDFLoader lê cada arquivo encontrado
        loader = DirectoryLoader('inputs/', glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        
        if not documents:
            print("❌ Nenhum arquivo PDF encontrado na pasta 'inputs'.")
            return
            
        print(f"✅ {len(documents)} páginas carregadas com sucesso!")

        # Fragmentação 
        print("✂️ Fragmentando o conteúdo em blocos de texto...")
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)

        # Criar Base de Dados Vetorial (Embeddings + FAISS)
        print("🤖 Criando representações matemáticas (embeddings) e base vetorial...")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = FAISS.from_documents(docs, embeddings)

        # Configurar o Modelo de Resposta (RAG)
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )

        #Chat Interativo no Terminal
        print("\n" + "="*50)
        print("✨ Chatbot de PDFs Pronto! Digite sua pergunta ou 'sair'.")
        print("="*50)
        
        while True:
            pergunta = input("\n🧐 Você: ")
            
            if pergunta.lower() in ['sair', 'exit', 'quit']:
                print("👋 Até logo!")
                break
            
            print("⏳ Pensando...")
            try:
                # Envia a pergunta para a chain de RAG
                resultado = qa_chain.invoke(pergunta)
                print(f"🤖 Chatbot: {resultado['result']}")
            except Exception as e:
                print(f"❌ Erro ao gerar resposta: {e}")

    except Exception as e:
        print(f"❌ Erro crítico no carregamento: {e}")

if __name__ == "__main__":
    main()