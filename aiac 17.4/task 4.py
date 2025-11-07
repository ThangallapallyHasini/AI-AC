# Step 1: Install pandas if not installed
# pip install pandas

import pandas as pd
import re
import string

# -----------------------------
# Step 2: Example dataset
# -----------------------------
data = {
    'text': [
        "I loooove this product!! 😍😍 Check it out: https://example.com",
        "Worst service ever... never buying again!!! #angry 😡",
        "Just okay, not great but not terrible either. 🤷‍♂️",
        "The new update is awesome!! 🔥🔥🔥"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 3: Simple lemmatizer (rule-based)
# -----------------------------
def simple_lemmatizer(word):
    # Very basic rule-based lemmatizer
    if word.endswith('ies'):
        return word[:-3] + 'y'
    elif word.endswith('ing'):
        return word[:-3]
    elif word.endswith('ed'):
        return word[:-2]
    elif word.endswith('s') and len(word) > 3:
        return word[:-1]
    else:
        return word

# -----------------------------
# Step 4: Preprocessing function
# -----------------------------
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    
    # Remove emojis and non-ASCII characters
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Remove special characters, punctuation, and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize (split into words)
    tokens = text.split()
    
    # Stopwords list (basic)
    stopwords = set([
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
        'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 
        'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 
        'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
        'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 
        'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 
        'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 
        'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 
        'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 
        'into', 'through', 'during', 'before', 'after', 'above', 'below', 
        'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 
        'under', 'again', 'further', 'then', 'once', 'here', 'there', 
        'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 
        'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 
        'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
        'can', 'will', 'just', 'dont', 'should', 'now'
    ])
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords]
    
    # Lemmatize using the simple rule-based function
    tokens = [simple_lemmatizer(word) for word in tokens]
    
    # Join tokens back to a sentence
    clean_text = " ".join(tokens)
    
    return clean_text

# -----------------------------
# Step 5: Apply cleaning
# -----------------------------
df['clean_text'] = df['text'].apply(clean_text)

# -----------------------------
# Step 6: Display results
# -----------------------------
print(df[['text', 'clean_text']])
