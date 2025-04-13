from .gadhwali_nlp import is_connected, phrase_dict  # Import utility functions form gadhwali_nlp
from .hindi_correction import correct_hindi_structure
from .gadhwali_correction import correct_gadhwali_structure

__all__ = ["is_connected", "phrase_dict", "correct_hindi_structure", "correct_gadhwali_structure"]
