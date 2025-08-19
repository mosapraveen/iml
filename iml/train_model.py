import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("dataset.csv")

print("Columns:", df.columns.tolist())
print(df.head())

# Keep only rows where Puntaje is a number (ignore AUSENTE or missing)
df = df[df["Puntaje"].str.replace(",", "").str.isdigit()]

# Convert Puntaje to float
df["Puntaje"] = df["Puntaje"].str.replace(",", "").astype(float)

# Create performance categories (adjust ranges as needed)
def performance_category(score):
    if score < 200000:
        return "Low"
    elif score < 400000:
        return "Medium"
    else:
        return "High"

df["Performance"] = df["Puntaje"].apply(performance_category)

# Features and target
X = df[["Puntaje"]]
y = df["Performance"]

# Scale the feature
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model trained and saved successfully!")
