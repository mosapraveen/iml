from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Function to classify student performance
def classify_fixed_thresholds(score_pct):
    if score_pct < 50:
        return "Low"
    elif score_pct < 75:
        return "Average"
    else:
        return "High"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        code = request.form["code"]
        score = request.form["score"]

        try:
            # Convert score to float
            score = float(score)
            performance = classify_fixed_thresholds(score)
            result = f"\U0001F4CC {name} ({code}) - Score: {score}%\n\U0001F539 Predicted Performance: {performance}"
        except ValueError:
            result = "\u274C Invalid Score! Please enter a valid number."

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
