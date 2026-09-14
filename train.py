import pandas as pd
import joblib
from model import IrisModel

data = pd.read_csv("iris.csv")

model = IrisModel(data)

joblib.dump(model, "iris_model.pkl")

print("Model trained successfully!")
print("Model saved as iris_model.pkl")