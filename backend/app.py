from flask import Flask, request, jsonify
from translation import translate_sentence  # Import translation function
from flask_cors import CORS
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# API endpoint for translation
@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "❌ No JSON data provided"}), 400

        text = data.get("text", "").strip()
        source_lang = data.get("source_lang", "").lower()
        target_lang = data.get("target_lang", "").lower()

        logger.info(f"Translation request: {text} from {source_lang} to {target_lang}")

        if not text:
            return jsonify({"error": "❌ Text is required"}), 400
        if not source_lang:
            return jsonify({"error": "❌ Source language is required"}), 400
        if not target_lang:
            return jsonify({"error": "❌ Target language is required"}), 400

        # Validate language codes
        valid_languages = ["en", "hi", "gadhwali"]
        if source_lang not in valid_languages:
            return jsonify({"error": f"❌ Invalid source language. Must be one of: {valid_languages}"}), 400
        if target_lang not in valid_languages:
            return jsonify({"error": f"❌ Invalid target language. Must be one of: {valid_languages}"}), 400

        # Perform translation
        translation = translate_sentence(text, source_lang, target_lang)
        logger.info(f"Translation successful: {translation}")

        return jsonify({
            "translation": translation,
            "source_lang": source_lang,
            "target_lang": target_lang
        }), 200

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": f"⚠️ An error occurred: {str(e)}"}), 500

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Run the Flask app
if __name__ == "__main__":
    logger.info("🚀 Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=5000)
