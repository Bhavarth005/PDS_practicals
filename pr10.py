import re
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def clean(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

df = pd.read_csv("IMDB Dataset.csv")
df["review"] = df["review"].apply(clean)

x_train, x_test, y_train, y_test = train_test_split(df["review"], df["sentiment"], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3,5))

x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

log_reg = LogisticRegression(solver="liblinear")

param_grid = {
    'C': [0.01, 0.1, 1, 10],
    'penalty': ['l1', 'l2']
}

grid = GridSearchCV(log_reg, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
grid.fit(x_train_vec, y_train)

print("Best Parameters: ", grid.best_params_)
print("Best Cross-Validation Accuracy: ", grid.best_score_)

best_model = grid.best_estimator_
y_pred = best_model.predict(x_test_vec)

print("Test Set Accuracy: ", accuracy_score(y_test, y_pred))
print("\nClassification Report: ", classification_report(y_test, y_pred))

