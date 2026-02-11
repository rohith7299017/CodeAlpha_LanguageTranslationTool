# Language Translation Tool

A simple web-based language translation tool built with **Python**, **Flask**, and a **free translation API (MyMemory)**.  
Users can enter text, choose source and target languages, see the translated text, copy it, and listen to it via text-to-speech in the browser.

---

## Features

- **Text input**: Type or paste text to be translated.
- **Language selection**:
  - Choose **source language** (or let the API auto-detect).
  - Choose **target language** (English, Hindi, Spanish, French, German, Arabic, Chinese (Simplified), Japanese, etc.).
- **Translation API**:
  - Uses **Microsoft Translator Text API v3** on the backend.
- **Output display**:
  - Translated text is shown clearly in a styled panel.
- **Copy to clipboard**:
  - One-click copy of the translated text.
- **Text-to-speech**:
  - Uses the **browser’s Speech Synthesis API** to read the translated text aloud (where supported).

---

## Prerequisites

- **Python 3.9+** installed.

---

## Setup Instructions

1. **Navigate to the project folder**

   ```bash
   cd "d:\Translation"
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open the app in your browser**

   Navigate to:

   ```text
   http://127.0.0.1:5000/
   ```

---

## How It Works

- The **frontend** (`templates/index.html`, `static/styles.css`, `static/script.js`):
  - Shows a 2-panel layout: left for source text, right for translated output.
  - Provides dropdowns for source and target languages.
  - Sends a POST request to `/api/translate` with the text and language codes.
  - Displays the translated text and offers **Copy** and **Speak** buttons.

- The **backend** (`app.py`):
  - Exposes `/` to serve the UI.
  - Implements `/api/translate` which:
    - Reads the input JSON `{ text, from, to }`.
    - Calls the **MyMemory** free translation endpoint:
      - `https://api.mymemory.translated.net/get?q=...&langpair=en|hi`
    - Extracts `responseData.translatedText` from the JSON response.
    - Returns the translated text as JSON back to the browser.

---



