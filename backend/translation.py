from utils import is_connected, phrase_dict  # Import utilities
from utils import correct_hindi_structure, correct_gadhwali_structure  # Import NLP functions
from googletrans import Translator
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Google Translator
try:
    translator = Translator()
except Exception as e:
    logger.error(f"Failed to initialize translator: {e}")
    translator = None

def translate_sentence(sentence, source_lang, target_lang):
    """
    Translates a sentence from source language to target language.
    Handles English, Hindi, and Gadhwali translations.
    """
    if not sentence or not source_lang or not target_lang:
        raise ValueError("Sentence, source_lang, and target_lang are required")

    lang_pair = f"{source_lang}-{target_lang}"
    logger.info(f"Translating from {source_lang} to {target_lang}: {sentence}")

    try:
        # 1. Use Google Translate for English ↔ Hindi if online
        if (source_lang in ["en", "hi"]) and (target_lang in ["en", "hi"]):
            if is_connected() and translator:
                try:
                    return translator.translate(sentence, src=source_lang, dest=target_lang).text
                except Exception as e:
                    logger.warning(f"Google Translate failed: {e}")
                    # Fall through to CSV translation
            else:
                logger.info("No internet or translator not available, using CSV")

        # 2. Use CSV-based translation
        return translate_using_csv(sentence, source_lang, target_lang)

    except Exception as e:
        logger.error(f"Translation failed: {e}")
        raise

def translate_using_csv(sentence, source_lang, target_lang):
    """
    Translates using the CSV dictionary with fallback options.
    """
    lang_pair = f"{source_lang}-{target_lang}"
    sentence_lower = sentence.lower().strip()

    # 1. Check for exact match in CSV
    if sentence_lower in phrase_dict.get(lang_pair, {}):
        translation = phrase_dict[lang_pair][sentence_lower]
        logger.info(f"Found exact match in CSV: {translation}")
        return translation

    # 2. Try phrase-based translation
    words = sentence_lower.split()
    translated_words = []
    unknown_words = []

    for word in words:
        translated_word = phrase_dict[lang_pair].get(word, None)
        if translated_word:
            translated_words.append(translated_word)
        else:
            unknown_words.append(word)
            # For unknown words, try Google Translate if available
            if (source_lang in ["en", "hi"]) and (target_lang in ["en", "hi"]):
                if is_connected() and translator:
                    try:
                        translated_word = translator.translate(word, src=source_lang, dest=target_lang).text
                        translated_words.append(translated_word)
                        continue
                    except Exception as e:
                        logger.warning(f"Failed to translate word '{word}': {e}")
            translated_words.append(word)  # Keep original word if no translation found

    if unknown_words:
        logger.warning(f"Could not translate words: {unknown_words}")

    translated_sentence = " ".join(translated_words)

    # 3. Apply language-specific corrections
    if target_lang == "gadhwali":
        try:
            corrected = correct_gadhwali_structure(translated_sentence)
            if corrected != translated_sentence:
                logger.info(f"Applied Gadhwali correction: {corrected}")
            return corrected
        except Exception as e:
            logger.error(f"Gadhwali correction failed: {e}")
            return translated_sentence
    elif target_lang == "hindi":
        try:
            corrected = correct_hindi_structure(translated_sentence)
            if corrected != translated_sentence:
                logger.info(f"Applied Hindi correction: {corrected}")
            return corrected
        except Exception as e:
            logger.error(f"Hindi correction failed: {e}")
            return translated_sentence

    return translated_sentence
