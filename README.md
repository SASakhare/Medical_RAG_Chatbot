#  **Medical RAG Chatbot (FastAPI + LangChain + Pinecone)**

A production-ready **AI-powered Medical Chatbot** built using **RAG (Retrieval-Augmented Generation)**.
It retrieves relevant medical information from documents and generates **accurate, context-aware responses**.

---

## *Features*

*  Semantic search using embeddings
*  Context-aware answers using LLMs
*  Source-grounded responses (reduces hallucination)
*  Fast retrieval with Pinecone vector DB
*  Interactive chat UI (web interface)
*  FastAPI backend (production-ready)

---

##  Tech Stack

* Python
* FastAPI
* LangChain / LangGraph
* Pinecone (Vector DB)
* OpenAI / Groq LLMs
* HuggingFace Embeddings
* HTML, CSS, JS (Frontend)

---

## 📂 Project Structure

```bash
Medical_RAG_Chatbot/
│
├── data/                # Medical PDFs
├── research/            # Jupyter notebooks
├── src/                 # Core logic (helpers, prompt)
├── static/              # CSS files
├── templates/           # HTML UI
├── app.py               # FastAPI app
├── store_index.py       # Create vector DB
├── requirements.txt
├── setup.py
├── .env
```

---

## ⚙️ How to Run

### 🔹 STEP 1: Clone Repository

```bash
git clone <your-repo-link>
cd Medical_RAG_Chatbot
```

---

### 🔹 STEP 2: Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 🔹 STEP 3: Install Requirements

```bash
pip install -r requirements.txt
```

---

### 🔹 STEP 4: Setup Environment Variables

Create `.env` file:

```env
PINECONE_API_KEY=your_pinecone_key
OPENAI_API_KEY=your_openai_key
```

---

### 🔹 STEP 5: Store Embeddings in Pinecone

```bash
python store_index.py
```

---

### 🔹 STEP 6: Run FastAPI Server

```bash
fastapi dev app.py
```

👉 Open in browser:

```
http://127.0.0.1:8000
```

👉 API Docs:

```
http://127.0.0.1:8000/docs
```

---

##  *How It Works (RAG Pipeline)*

1. User enters query
2. Retriever fetches relevant documents
3. Context injected into prompt
4. LLM generates grounded response

---

## 📸 Demo

* Chat UI with real-time responses
* Supports medical queries
* Displays contextual answers

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Not a substitute for professional medical advice.

---

## 💡 Future Improvements

* Streaming responses (ChatGPT-like typing)
* Multi-agent workflows
* Voice input/output
* Deployment (Docker + AWS)

---

## 🔐 Environment Variables

| Variable         | Description      |
| ---------------- | ---------------- |
| PINECONE_API_KEY | Pinecone API key |
| GROQ_API_KEY   | Groq API key   |

---


##  If you like this project

Give it a ⭐ on GitHub!

---


# **AWS-CICD-Deployment-with-Github-Actions**

### 1. Login to AWS console

---

### 2. Create IAM user for deployment

#### With specific access:
1. EC2 access → Virtual machine  
2. ECR → Elastic Container Registry (to store Docker images)

#### Description (Deployment Flow):
1. Build Docker image of the source code  
2. Push Docker image to ECR  
3. Launch EC2 instance  
4. Pull image from ECR in EC2  
5. Run Docker container on EC2  

#### Policy:
- AmazonEC2ContainerRegistryFullAccess  
- AmazonEC2FullAccess  

---

### 3. Create ECR repository

- Save the URI  
```

707610778250.dkr.ecr.us-east-1.amazonaws.com/modelrag

```

---

### 4. Create EC2 machine (Ubuntu)

---

### 5. Install Docker in EC2

#### Optional:
```

sudo apt-get update -y
sudo apt-get upgrade

```

#### Required:
```

curl -fsSL [https://get.docker.com](https://get.docker.com) -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

```

---

### 6. Configure EC2 as self-hosted runner

- Go to:  
  `GitHub → Settings → Actions → Runners → New self-hosted runner`  
- Select OS and run the commands provided  

---

### 7. Setup GitHub Secrets

Add the following secrets in your repository:

- AWS_ACCESS_KEY_ID  
- AWS_SECRET_ACCESS_KEY  
- AWS_DEFAULT_REGION  
- ECR_REPO  
- PINECONE_API_KEY  
- GROQ_API_KEY  

---
```

