# ⚡ Async Agent Pipeline

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Instructor](https://img.shields.io/badge/Instructor-Structured_Outputs-orange.svg)](https://python.useinstructor.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, asynchronous agent pipeline built with **FastAPI**, **Pydantic**, and **Instructor**, designed for robust structured data extraction and triage using local LLMs (fully compatible with LM Studio and OpenAI-compatible APIs).

---

## ✨ Features

* **FastAPI Backend:** Exposes robust REST endpoints for asynchronous processing, analysis, and system health checks.
* **Structured Output Extraction:** Powered by **Instructor** and Pydantic models to guarantee strict schema validation and error-free JSON generation from LLMs.
* **Local LLM Integration:** Configured to work seamlessly with local inference servers like **LM Studio** for complete data privacy and offline execution.
* **Ready-to-Use Client:** Includes an automated test client script for instant pipeline verification.

---

## 📂 Project Structure

* `main.py` — FastAPI server implementing the `/analyze` and `/health` endpoints with Instructor schema enforcement.
* `test_client.py` — Test client script used to send sample payloads and inspect structured JSON responses.

---

## 🛠️ Tech Stack

* **Web Framework:** FastAPI & Uvicorn
* **Data Validation & Modeling:** Pydantic
* **Structured Extraction:** Instructor (`instructor`)
* **Local Inference:** LM Studio (OpenAI-compatible local server)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone [https://github.com/Valentina14142000/async-agent-pipeline.git](https://github.com/Valentina14142000/async-agent-pipeline.git)
cd async-agent-pipeline
```

### 2. Setup Environment

Create and activate a Python virtual environment, then install the dependencies:

```Bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn instructor pydantic openai
```

### 3. Start Local Inference Server

Open LM Studio (or your preferred OpenAI-compatible local server).

Load a capable model (e.g., Llama 3 or Mistral).

Start the local server (typically running on http://localhost:1234/v1).

### 4. Configure Environment Variables

Create a .env file in the root directory to point your pipeline to your local inference server:

```Code snippet
OPENAI_API_BASE=http://localhost:1234/v1
OPENAI_API_KEY=not-needed-locally
```

### 5. Run the FastAPI Server

```Bash
uvicorn main:app --reload --port 8000
```

### 6. Test the Pipeline

Open a separate terminal window, activate your virtual environment, and run the test client:

```Bash
source venv/bin/activate
python test_client.py
```

