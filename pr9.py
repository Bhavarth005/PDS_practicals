from datasets import load_dataset
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

dataset = load_dataset("wikipedia", "20220301.simple", split="train[:1%]", trust_remote_code=True)

def get_label(title):
    title = title.lower()
    if "science" in title:
        return "science"
    elif "politics" in title or "government" in title:
        return "politics"
    elif "football" in title or "cricket" in title:
        return "sports"
    elif "computer" in title or "technology" in title:
        return "technology"
    elif "geography" in title or "mountain" in title:
        return "geography"
    else:
        return None

def custom_preprocessor(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

labeled_data = dataset.filter(lambda x: get_label(x['title']) is not None)
df = pd.DataFrame({
    'text': labeled_data['text'],
    'label': [get_label(title) for title in labeled_data['title']]
})

x_train, x_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(preprocessor=custom_preprocessor, analyzer='char', ngram_range=(2, 4))),
    ('clf', LogisticRegression(max_iter=200))
])

pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)

print(classification_report(y_test, y_pred))