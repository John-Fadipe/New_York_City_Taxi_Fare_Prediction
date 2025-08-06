from flask import Flask, render_template, request
import joblib

model_wrapper = joblib.load("Model/model_3_wrapper.pkl")

app = Flask(__name__)
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    location = request.form.get("Location")
    destination = request.form.get("Destination")
    passenger_count = request.form.get("Number of Passengers")

    predictions = None
    error = None

    try:
        predictions = model_wrapper.predict(location, destination, int(passenger_count))
        predictions = round(float(predictions), 2)
    except ValueError as ve:
        error = f"Invalid input: {ve}"
    except Exception as e:
        error = "❌ Could not process your request. Please check your inputs."
        print(f"[PREDICTION ERROR] {e}")

    return render_template("index.html",
                           predictions=predictions,
                           error=error,
                           location=location,
                           destination=destination,
                           passenger_count=passenger_count)

if __name__ == "__main__":
    app.run(debug=True)