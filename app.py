from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# Try multiple translation APIs
LIBRETRANSLATE_URL = "https://libretranslate.com/translate"
GOOGLE_TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()
        
        if not data or not data.get("text"):
            return jsonify({"error": "No text provided", "translatedText": ""}), 400
        
        text = data["text"]
        source = data["source"]
        target = data["target"]
        
        # Try Google Translate first (more reliable)
        translated_text = try_google_translate(text, source, target)
        
        if translated_text:
            return jsonify({"translatedText": translated_text})
        
        # Fallback to LibreTranslate
        translated_text = try_libretranslate(text, source, target)
        
        if translated_text:
            return jsonify({"translatedText": translated_text})
        
        return jsonify({"error": "All translation services are currently unavailable", "translatedText": ""}), 500
            
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return jsonify({"error": f"Server error: {str(e)}", "translatedText": ""}), 500

def try_libretranslate(text, source, target):
    """Try LibreTranslate API"""
    try:
        # LibreTranslate might need different language codes
        # Map common codes to LibreTranslate format
        lang_map = {
            'en': 'en',
            'es': 'es', 
            'fr': 'fr',
            'hi': 'hi',
            'ta': 'ta',
            'de': 'de',
            'it': 'it',
            'pt': 'pt',
            'ru': 'ru',
            'ja': 'ja',
            'ko': 'ko',
            'zh': 'zh',
            'ar': 'ar'
        }
        
        source_lang = lang_map.get(source, source)
        target_lang = lang_map.get(target, target)
        
        payload = {
            "q": text,
            "source": source_lang,
            "target": target_lang,
            "format": "text"
        }
        
        print(f"LibreTranslate payload: {payload}")
        response = requests.post(LIBRETRANSLATE_URL, json=payload, timeout=10)
        
        print(f"LibreTranslate status: {response.status_code}")
        if response.status_code != 200:
            print(f"LibreTranslate error response: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            return result.get("translatedText", "")
        else:
            return None
            
    except Exception as e:
        print(f"LibreTranslate error: {str(e)}")
        return None

def try_google_translate(text, source, target):
    """Try Google Translate API (free version)"""
    try:
        params = {
            'client': 'gtx',
            'sl': source,
            'tl': target,
            'dt': 't',
            'q': text
        }
        
        response = requests.get(GOOGLE_TRANSLATE_URL, params=params, timeout=10)
        
        if response.status_code == 200:
            # Google Translate returns a complex nested structure
            result = response.json()
            if result and len(result) > 0 and len(result[0]) > 0:
                translated_parts = []
                for part in result[0]:
                    if part[0]:  # The translated text is in part[0]
                        translated_parts.append(part[0])
                return ''.join(translated_parts)
        else:
            print(f"Google Translate failed with status {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Google Translate error: {str(e)}")
        return None

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
