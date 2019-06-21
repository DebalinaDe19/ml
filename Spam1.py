import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('SMSSPAM', delimiter='\t',header=None)

print(df.head())
def text_preprocess(df):
    df = df.translate(str.maketrans('', '', string.punctuation))
    df = [word for word in text.split() if word.lower() not in  stopwords.words('english')]
    return " ".join(text)

text_preprocess(df)
vectorizer = TfidfVectorizer('english')
message_mat = vectorizer.fit_transform(msg_data)
print(message_mat)

