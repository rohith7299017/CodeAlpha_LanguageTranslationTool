import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


TRANSLATE_ENDPOINT = "https://api.mymemory.translated.net/get"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/translate", methods=["POST"])
def translate():
    """
    Translate text using the free MyMemory translation API.
    Expects JSON: { "text": "...", "from": "en", "to": "fr" }.
    """
    data = request.get_json(silent=True) or {}

    text = (data.get("text") or "").strip()
    from_lang = (data.get("from") or "en").strip() or "en"
    to_lang = (data.get("to") or "en").strip() or "en"

    if not text:
        return jsonify({"error": "Text is required."}), 400

    params = {
        "q": text,
        "langpair": f"{from_lang}|{to_lang}",
        "mt": 1,
    }

    try:
        response = requests.get(
            TRANSLATE_ENDPOINT,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()

        translated_text = (
            (payload.get("responseData") or {}).get("translatedText") or ""
        )

        if not translated_text:
            error_detail = payload.get("responseDetails") or "No translation returned."
            return jsonify({"error": error_detail}), 502

        return jsonify({"translatedText": translated_text})
    except requests.exceptions.RequestException:
        return jsonify(
            {
                "error": "Translation request failed. "
                "Please check your connection and try again."
            }
        ), 502
    except (ValueError, TypeError):
        return jsonify(
            {"error": "Unexpected response from translation service."}
        ), 502


if __name__ == "__main__":
    app.run(debug=True)

