from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    location = ""
    destination = ""
    if request.method == "POST":
        location = request.form.get("Location")
        destination = request.form.get("Destination")
    return render_template("index.html", location=location, destination=destination)

if __name__ == "__main__":
    app.run(debug=True)