import os
import pandas as pd
import requests

# ✅ Function to check internet connection
def is_connected():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

# ✅ Load CSV file
csv_path = os.path.join(os.path.dirname(__file__), "translations.csv")
try:
    data = pd.read_csv(csv_path)
    print("✅ CSV Loaded Successfully!")
except Exception as e:
    raise ValueError(f"❌ Error loading CSV file: {str(e)}")

# ✅ Ensure required columns exist
expected_columns = {"English", "Hindi", "Gadhwali"}
missing_columns = expected_columns - set(data.columns)
if missing_columns:
    raise ValueError(f"❌ Missing columns in CSV: {missing_columns}")

# ✅ Create phrase dictionaries for translation
phrase_dict = {
    "en-hi": dict(zip(data["English"].str.lower(), data["Hindi"])),
    "hi-en": dict(zip(data["Hindi"], data["English"])),
    "en-gadhwali": dict(zip(data["English"].str.lower(), data["Gadhwali"])),
    "gadhwali-en": dict(zip(data["Gadhwali"], data["English"])),
    "hi-gadhwali": dict(zip(data["Hindi"], data["Gadhwali"])),
    "gadhwali-hi": dict(zip(data["Gadhwali"], data["Hindi"])),
}
