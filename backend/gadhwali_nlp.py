import spacy

# ✅ Load spaCy NLP Model
nlp = spacy.load("en_core_web_sm")

# ✅ Function to correct Gadhwali sentence structure
def correct_gadhwali_structure(sentence):
    doc = nlp(sentence)
    
    subject = []
    verb = []
    object_ = []
    others = []

    # 🔹 Categorize words based on POS tagging
    for token in doc:
        if token.dep_ in ("nsubj", "nsubjpass"):  # Subject
            subject.append(token.text)
        elif token.pos_ in ("VERB", "AUX"):  # Verb
            verb.append(token.text)
        elif token.dep_ in ("dobj", "pobj"):  # Object
            object_.append(token.text)
        else:  # Other words
            others.append(token.text)

    # 🔥 Gadhwali sentence structure: **Object + Verb + Subject**
    corrected_sentence = object_ + verb + subject + others
    return " ".join(corrected_sentence).strip()
