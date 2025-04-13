import spacy
import stanza
from typing import List, Tuple, Set

# Download the Hindi model (only needs to be run once)
try:
    stanza.download("hi")
except Exception as e:
    print(f"⚠️ Warning: Could not download Stanza model: {e}")

# Initialize models
try:
    nlp = spacy.load("en_core_web_sm")  # For English parsing if needed
    nlp_hi = stanza.Pipeline(lang="hi", processors="tokenize,pos,lemma,depparse")
except Exception as e:
    print(f"⚠️ Warning: Could not load NLP models: {e}")
    nlp = None
    nlp_hi = None

# Custom Gadhwali grammar components
HELPING_VERBS: Set[str] = {"छू", "च", "हौ", "थ", "छै", "छैन", "छौं", "छौ", "छौं"}
MODALS: Set[str] = {"चौन", "चाहू", "सकदु", "पैदु", "लैदु", "चाहिन्दु", "सकदु", "पैदु"}
PREPOSITIONS: Set[str] = {"में", "पर", "से", "को", "के लिए", "तैं", "कैं", "मा", "बटी", "कन"}
NEGATIONS: Set[str] = {"नै", "कस", "न", "नैं", "नी", "निच"}
CONJUNCTIONS: Set[str] = {"अर", "तैं", "कि", "जैं", "अरु", "तैं"}
ADVERBS: Set[str] = {"बड़ी", "छोटी", "धीर", "तेज", "अच्छी", "बहोते", "धीरु", "तेजी"}

def process_sentence_with_stanza(sentence: str) -> stanza.Document:
    """
    Processes a sentence using Stanza's Hindi model and returns the parsed doc.
    """
    if not sentence.strip():
        raise ValueError("❌ Empty sentence provided")

    if not nlp_hi:
        raise ValueError("❌ Stanza model not initialized")

    try:
        doc = nlp_hi(sentence)
        return doc
    except Exception as e:
        raise ValueError(f"❌ Error processing sentence with Stanza: {str(e)}")

def categorize_tokens(doc: stanza.Document) -> Tuple[List[str], List[str], List[str], List[str], List[str], List[str], List[str], List[str]]:
    """
    Categorizes tokens into various Gadhwali grammar parts.
    """
    subject, verbs, objects, auxiliaries = [], [], [], []
    modals, preps, negations, others = [], [], [], []

    for sent in doc.sentences:
        for word in sent.words:
            text = word.text.strip()
            upos = word.upos
            dep = word.deprel

            # Handle compound words
            if "-" in text:
                parts = text.split("-")
                for part in parts:
                    if part in HELPING_VERBS:
                        auxiliaries.append(part)
                    elif part in MODALS:
                        modals.append(part)
                    elif part in PREPOSITIONS:
                        preps.append(part)
                    elif part in NEGATIONS:
                        negations.append(part)
                    else:
                        others.append(part)
                continue

            if dep in ("nsubj", "nsubj:pass"):
                subject.append(text)
            elif upos == "VERB":
                verbs.append(text)
            elif upos == "AUX" or text in HELPING_VERBS:
                auxiliaries.append(text)
            elif dep in ("obj", "iobj", "dobj", "pobj"):
                objects.append(text)
            elif text in MODALS:
                modals.append(text)
            elif text in PREPOSITIONS:
                preps.append(text)
            elif text in NEGATIONS:
                negations.append(text)
            else:
                others.append(text)

    return subject, verbs, objects, auxiliaries, modals, preps, negations, others

def correct_gadhwali_structure(sentence: str) -> str:
    """
    Corrects Gadhwali sentence structure using the rule:
    Subject + Object + Negation + Verb + Helping Verb + Modal + Preposition + Others
    """
    if not sentence.strip():
        return sentence

    try:
        doc = process_sentence_with_stanza(sentence)
        subject, verbs, objects, auxiliaries, modals, preps, negations, others = categorize_tokens(doc)

        # Special handling for common Gadhwali patterns
        if not verbs and not auxiliaries and not modals:
            # If no verbs found, return original sentence
            return sentence

        # Handle common Gadhwali patterns
        if "च" in auxiliaries and not verbs:
            # Handle cases like "मैं खुश च"
            corrected = subject + objects + others + auxiliaries
        else:
            # Standard SOV pattern
            corrected = subject + objects + negations + verbs + auxiliaries + modals + preps + others

        return " ".join(corrected).strip()
    except Exception as e:
        print(f"⚠️ Warning: Could not correct Gadhwali structure: {e}")
        return sentence  # Return original sentence if correction fails

# Test cases
if __name__ == "__main__":
    test_sentences = [
        "मै खाना खांदु",                # Basic SOV
        "तू स्कूल जौन चौन",             # Modal verb
        "मै किताब नै पढ़न",             # Negation
        "ऊ घर में छै",                  # Preposition + helping verb
        "तुमि काम करण चाहू",           # Modal + helping verb
        "मै बड़ी धीर चलण",             # Adverb
        "तू अर मै स्कूल जौन",           # Conjunction
        "तुं जां सकदु",                 # Modal
        "मैं खुश च",                    # Simple statement
        "तुम ठीक छा",                   # Question form
    ]

    for sentence in test_sentences:
        try:
            corrected = correct_gadhwali_structure(sentence)
            print(f"👉 Original : {sentence}")
            print(f"✅ Corrected: {corrected}\n")
        except ValueError as e:
            print(f"❌ Error: {e}\n")


print("hello i am working")