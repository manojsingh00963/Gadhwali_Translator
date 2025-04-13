# Hindi-to-Gadhwali dictionary
hindi_to_gadhwali = {
    "मैं": "म्यर",
    "तू": "तू",
    "तुम": "तुमि",
    "वह": "ऊ",
    "हम": "अमि",
    "वे": "उनि",
    "खुश": "खुसी",
    "नहीं": "नै",
    "हूँ": "छू",
    "है": "च",
    "थे": "था",
    "था": "थ",
    "थी": "थी",
    "करता": "करण",
    "करती": "करणी",
    "करते": "करण",
    "खेलना": "खेल",
    "खेलता": "खेलण",
    "चाहता": "चौन",
    "चाहती": "चौनी",
    "चाहते": "चौन",
    "क्योंकि": "किलै",
    "खाना": "खाण",
    "पीना": "पीण",
    "आना": "आण",
    "जाना": "जाण",
    "बोलना": "बोलण",
}

def convert_hindi_to_gadhwali(sentence):
    """
    Converts a given Hindi sentence to Gadhwali word-by-word.

    :param sentence: Hindi sentence as a string.
    :return: Translated Gadhwali sentence.
    """
    words = sentence.split()
    translated_words = [hindi_to_gadhwali.get(word, word) for word in words]  # Replace words if found
    return " ".join(translated_words)
