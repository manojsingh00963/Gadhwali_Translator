# 🌐 Multilingual Translator (EN ⇄ HI ⇄ GDW)

A powerful Flask-based API for translating between **English**, **Hindi**, and **Gadhwali** using:
- 🧠 Word & phrase matching from `translations.csv`
- 🗣️ Grammar correction with custom NLP logic
- 🌍 Google Translate fallback (for English ↔ Hindi)
- 💡 Offline Gadhwali translation & correction support

---

## 🚀 Features

- 🔁 **Bidirectional Translation**:
  - English ⇄ Hindi
  - English ⇄ Gadhwali
  - Hindi ⇄ Gadhwali

- 🧠 **Grammar Correction**:
  - Rule-based Hindi structure fixer
  - Gadhwali-specific word order correction via POS tags & fallback rules

- 📦 **Offline & Online Modes**:
  - Uses local dictionary first
  - Falls back to Google Translate if needed (EN-HI only)

- ⚡ **Flask REST API** with `/translate` endpoint
- 📄 **CSV-driven** dictionary system (`translations.csv`)

---

## 📁 Project Structure


---

## 📦 Installation

```bash
git clone https://github.com/yourusername/translator-app
cd translator-app/backend
pip install -r requirements.txt
```


## 📌 Requirements (requirements.txt)
```bash
text
Copy
Edit
Flask
flask-cors
pandas
stanza
spacy
requests
googletrans==4.0.0-rc1
gensim


```


🧠 How It Works
---------------

1.  User sends text like "i want to go" to /translate
    
2.  The app tries to match the full phrase from the CSV
    
3.  If not found, it falls back to word-by-word translation
    
4.  If target is Gadhwali or Hindi, it applies grammar correction:
    
    *   correct\_gadhwali\_structure() for GDW
        
    *   correct\_hindi\_structure() for HI
        
5.  If English ↔ Hindi and internet is available, it uses Google Translate
    
6.  Response is returned as JSON
    

🔄 API Usage
------------

### Endpoint:

```  bashCopyEditPOST /translate   ```

### Request Body (JSON):
>   jsonCopyEdit{    "text": "i not can go",  
  "source_lang": "en",   
   "target_lang": "gadhwali"  }  

### Response:

```bash
 jsonCopyEdit{  
"translation": "मि नि जै सकदु", 
}  
```
🧪 Train FastText (Optional)
----------------------------

If you'd like to train a FastText model on your dataset:

> bashCopyEditpython train_model.py   

This will generate:

*   fasttext\_translator.model
    
*   fasttext\_translator.txt
    

Useful for synonyms, embeddings, and expansion.

📂 How to Add New Words
-----------------------

Just update translations.csv like this:

EnglishHindiGadhwalieatखानाखाणwantचाहताचौनschoolस्कूलस्कूल

> Add both full phrases and individual words for better matching!

✨ Future Ideas
--------------

*   Add React frontend
    
*   User upload for CSV
    
*   Neural model integration
    
*   Voice input
    

<!-- 👨‍💻 Author
------------

**Manoj Singh**Aspiring full-stack + AI/ML developer🔗 [GitHub](https://github.com/manojsingh00963) -->