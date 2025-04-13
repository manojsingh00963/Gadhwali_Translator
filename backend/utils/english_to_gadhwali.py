english_to_gadhwali = {
    "i": "म्यर",
    "you": "तू",
    "he": "ऊ",
    "she": "ऊ",
    "we": "अमि",
    "they": "उनि",
    "happy": "खुसी",
    "not": "नै",
    "am": "छू",
    "is": "च",
    "are": "च",
    "was": "थ",
    "were": "था",
    "play": "खेल",
    "want": "चौन",
    "eat": "खाण",
    "drink": "पीण",
    "go": "जाण",
    "speak": "बोलण",
}

def convert_english_to_gadhwali(sentence):
    words = sentence.lower().split()
    translated_words = [english_to_gadhwali.get(word, word) for word in words]
    return " ".join(translated_words)

