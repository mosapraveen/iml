from flask import Flask, render_template, request
import joblib
import numpy as np

# Load saved model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Get form inputs
            name = request.form["name"]
            code = request.form["code"]
            score = float(request.form["score"])  # Ensure numeric

            # Scale input
            score_scaled = scaler.transform(np.array([[score]]))

            # Predict
            prediction = model.predict(score_scaled)[0]

            # Show result with student info
            result = f"Student {name} (Code: {code}) → Predicted Performance: {prediction}"

        except ValueError:
            result = "❌ Invalid input! Please enter a valid numeric score."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
