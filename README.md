# 🤖 Chatbot Inteligente com IA Generativa e Busca Vetorial (RAG)

Este projeto foi desenvolvido como parte de um desafio prático da **DIO (Digital Innovation One)**. O objetivo é criar um sistema de **IA Generativa** capaz de responder perguntas baseadas no conteúdo de múltiplos arquivos PDF fornecidos pelo usuário.

## 🚀 Visão Geral do Projeto
O sistema utiliza a técnica de **RAG (Retrieval-Augmented Generation)**. Diferente de um chat comum, esta IA não apenas gera texto, mas primeiro busca informações relevantes em uma base de dados local (criada a partir dos seus PDFs) para fornecer respostas precisas e fundamentadas, evitando "alucinações".

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12 (Versão estável)
* **Framework de IA:** [LangChain](https://www.langchain.com/) (Orquestração de documentos e modelos)
* **Modelo de Linguagem (LLM):** Google Gemini 1.5 Pro
* **Banco de Dados Vetorial:** FAISS (Facebook AI Similarity Search)
* **Embeddings:** Google Generative AI Embeddings
* **Gerenciamento de Ambiente:** Python VENV e Dotenv

## 📂 Estrutura de Pastas
```text
chatbot-pdf/
├── inputs/           <-- Local onde os arquivos PDF são armazenados
├── app.py            <-- Código principal do Chatbot
├── requirements.txt  <-- Lista de dependências do projeto
├── .env              <-- Chave da API do Google (não versionado)
└── README.md         <-- Documentação do projeto