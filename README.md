# Async Agent Pipeline

A lightweight, asynchronous agent pipeline built with **FastAPI**, **Pydantic**, and **Instructor**, designed for structured data extraction and triage using local LLMs (compatible with LM Studio / OpenAI-compatible APIs).

## Features

* **FastAPI Backend:** Exposes robust REST endpoints for asynchronous processing and triage.
* **Structured Output Extraction:** Powered by `instructor` and Pydantic models to guarantee strict schema validation.
* **Local LLM Integration:** Configured to work seamlessly with local inference servers (LM Studio).
* **Ready-to-Use Client:** Includes an automated test client script for quick verification.

## Project Structure

* `main.py`: FastAPI server implementing the `/analyze` and `/health` endpoints using Instructor.
* `test_client.py`: Test client script to send sample payloads and inspect structured JSON responses.
