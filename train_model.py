import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import pickle

# ---------- LOAD DATA ----------
df = pd.read_csv("house_data.csv")

# ---------- SELECT FEATURES ----------
X = df[['bedrooms', 'bathrooms', 'area']]  # only 3 features
y = df['price']

# ---------- HANDLE MISSING VALUES ----------
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# ---------- SPLIT DATA ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------- TRAIN MODEL ----------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------- SAVE MODEL & IMPUTER ----------
with open("house_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("imputer.pkl", "wb") as f:
    pickle.dump(imputer, f)

print("✅ Model trained successfully with 3 features!")