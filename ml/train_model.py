import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# synthetic data
data = pd.DataFrame({
    "amount": [1000, 5000000, 20000, 900000, 300],
    "foreign": [0, 1, 0, 1, 0],
    "new_device": [0, 1, 1, 0, 0],
    "fraud": [0, 1, 0, 1, 0]
})

X = data[["amount", "foreign", "new_device"]]
y = data["fraud"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✅ Model trained and saved")
