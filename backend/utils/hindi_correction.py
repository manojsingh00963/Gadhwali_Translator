import spacy

# Load Hindi NLP model (spaCy doesn't have a native Hindi model, so we use basic rules)
# If you have an external Hindi NLP model, load it here

def correct_hindi_structure(sentence):
    """
    Corrects Hindi sentence structure to follow Subject-Object-Verb (SOV) order.
    Example: "मैं खुश हूँ" → "मैं खुश हूँ"
    """
    words = sentence.split()

    # Ensure "हूँ", "है", "था", etc. (helping verbs) appear at the end
    helping_verbs = {"हूँ", "है", "थे", "थी", "था", "रहा", "रही", "रहे", "कर", "किया", "किए"}
    verb_index = None

    # Find the position of the first helping verb
    for i, word in enumerate(words):
        if word in helping_verbs:
            verb_index = i
            break

    # If a verb exists, move it to the end
    if verb_index is not None and verb_index < len(words) - 1:
        verb = words.pop(verb_index)
        words.append(verb)

    return " ".join(words)
