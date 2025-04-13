from gensim.models import FastText
import pandas as pd
import os

# Load dataset
csv_path = "translations.csv"
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"❌ CSV file not found: {csv_path}")

data = pd.read_csv(csv_path)

# Ensure correct column names
required_columns = {"English", "Hindi", "Gadhwali"}
if not required_columns.issubset(data.columns):
    raise ValueError(f"❌ CSV must contain columns: {required_columns}")

# Preprocess: Remove NaN & convert to lowercase
data = data.dropna(subset=["English", "Hindi", "Gadhwali"])
data = data.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

# Tokenize sentences into words
source_words = [sentence.split() for sentence in data["English"]]
hindi_words = [sentence.split() for sentence in data["Hindi"]]
gadhwali_words = [sentence.split() for sentence in data["Gadhwali"]]

# Combine all for multilingual training
combined_words = source_words + hindi_words + gadhwali_words

# Train FastText model (better for rare or unseen words)
model = FastText(sentences=combined_words, vector_size=100, window=5, min_count=1, workers=4)

# Save the model
model.save("fasttext_translator.model")
model.wv.save_word2vec_format("fasttext_translator.txt", binary=False)

print(f"✅ FastText model trained successfully! Vocabulary size: {len(model.wv)} words")
print("✅ FastText word vectors saved!")
