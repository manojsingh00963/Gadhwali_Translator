pip install nltk

# The utils.py file is used to correct the structure of translated Hindi sentences to make them grammatically correct.

# Why is it needed?
# When you translate English to Hindi word by word, the sentence structure may become incorrect.

# 🔴 Example without correction:

# Input: "I am happy" → Direct word translation: "मैं हूँ खुश" (Incorrect)

# Hindi follows Subject-Object-Verb (SOV) order, so correct sentence: "मैं खुश हूँ"

# How is utils.py used?
# It provides the function correct_hindi_structure(sentence), which is used inside app.py to fix grammar after translation.

# How it is used in app.py
# python
# Copy
# Edit
# from utils import correct_hindi_structure

# def translate_sentence(sentence):
#     words = sentence.lower().split()
#     translated_words = [word_dict.get(word, word) for word in words]  # Word-by-word translation
    
#     translated_sentence = " ".join(translated_words)
    
#     # Correct Hindi sentence structure using `utils.py`
#     return correct_hindi_structure(translated_sentence)
# When is it NOT needed?
# ✅ If you only translate words without forming full sentences, you don’t need utils.py.
# ✅ If you manually write correct Hindi sentences in the dataset, then utils.py is not required.

# Conclusion
# 📌 If you are translating full sentences, keep utils.py.
# 📌 If your translation only needs individual words, you can remove utils.py.

# Let me know what you want to do! 🚀