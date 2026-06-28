# Chinese CAD Translation Tool

## Overview

A desktop application that translates Chinese text in CAD drawings (PDF) into English. A CustomTkinter GUI talks to a local FastAPI backend (run in a background thread), which extracts Chinese text from the PDF (PyMuPDF + pdfplumber), translates it offline using a bundled MarianMT (Helsinki-NLP) model, and overlays the English text back onto the original PDF abbreviating and generating a legend page where space doesn't allow the full translation to fit. Jobs run as background tasks and are polled for status; results are returned as a downloadable ZIP.

## Architecture Diagram
check this link for flow diagram:
https://github.com/prerna-phadnis/translation-flow-diagram/blob/main/diagrams.excalidraw.svg

## Environment Variables

The app loads a `.env` file at startup via `python-dotenv`. Create a `.env` file in the project root with:

| Variable | Description |
|---|---|
| `ACTIVATION_SERVER_URL` *(optional)* | Online license activation endpoint, used as a fallback if offline validation needs it |

No other environment variables are required for local development — the translation model is loaded from a local `trained_helsinki/` folder, and the backend runs on a fixed local port (`8000`).

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Place the translation model
#    Ensure a `trained_helsinki/` folder exists at the project root

# 3. Create a .env file (see Environment Variables above)

# 4. Run the app (starts backend + GUI)
python run_app.py
```

To run just the backend (for API testing):

```bash
cd backend
uvicorn main:app --reload --port 8000
```

To build the packaged executable:

```bash
pyinstaller run_app.spec
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `GET`  | `/health` | Health check used by the GUI to confirm the backend is ready |
| `POST` | `/translate/start-translation/` | Starts a translation job for a list of PDF paths; returns `job_id` |
| `GET`  | `/translate/job-status/{job_id}` | Returns current job status (`starting`, `extracting`, `translating`, `creating_pdf`, `complete`, `error`) |
| `GET`  | `/translate/download/{job_id}` | Downloads the resulting ZIP once the job is complete |