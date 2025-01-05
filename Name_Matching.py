from rapidfuzz import fuzz
import unicodedata

def normalize_text(text):
    # Convert to lowercase, remove diacritics, and strip whitespace
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return text.lower().strip()

def compare_names(name1, name2):
    # Normalize the names
    name1 = normalize_text(name1)
    name2 = normalize_text(name2)
    
    # Compute similarity using token-based matching
    similarity_ratio = fuzz.token_sort_ratio(name1, name2)
    
    return similarity_ratio

# Input strings
name1 = "Eldeleklioglu, Jale"
name2 = "Jale Eldeleklioğlu"

# Compare the names
similarity_ratio = compare_names(name1, name2)

# Output the similarity score
print(f"Similarity between '{name1}' and '{name2}': {similarity_ratio}%")

# Threshold to decide if the names match
threshold = 80  # Adjust based on requirements

if similarity_ratio >= threshold:
    print("The two names match!")
else:
    print("The two names do not match.")
