from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-development-secret"

# DEMO DATA ONLY — these are fictional sample fares and do not represent live inventory.
FLIGHTS = [
    {"id":"VY101","airline":"Voyara Air","from_code":"HYD","from_city":"Hyderabad","to_code":"DEL","to_city":"New Delhi","depart":"06:20","arrive":"08:35","duration":"2h 15m","stops":"Non-stop","price":4899,"tag":"Best value","color":"violet"},
    {"id":"VY204","airline":"Voyara Air","from_code":"HYD","from_city":"Hyderabad","to_code":"BLR","to_city":"Bengaluru","depart":"09:10","arrive":"10:25","duration":"1h 15m","stops":"Non-stop","price":3299,"tag":"Quick escape","color":"blue"},
    {"id":"VY318","airline":"Skyline Airways","from_code":"HYD","from_city":"Hyderabad","to_code":"BOM","to_city":"Mumbai","depart":"12:40","arrive":"14:10","duration":"1h 30m","stops":"Non-stop","price":3799,"tag":"Popular","color":"orange"},
    {"id":"VY427","airline":"Voyara Air","from_code":"HYD","from_city":"Hyderabad","to_code":"GOI","to_city":"Goa","depart":"15:25","arrive":"17:00","duration":"1h 35m","stops":"Non-stop","price":4199,"tag":"Weekend pick","color":"teal"},
    {"id":"VY512","airline":"AeroVista","from_code":"HYD","from_city":"Hyderabad","to_code":"MAA","to_city":"Chennai","depart":"18:15","arrive":"19:35","duration":"1h 20m","stops":"Non-stop","price":2899,"tag":"Evening flight","color":"pink"},
    {"id":"VY620","airline":"Skyline Airways","from_code":"HYD","from_city":"Hyderabad","to_code":"COK","to_city":"Kochi","depart":"20:05","arrive":"21:50","duration":"1h 45m","stops":"Non-stop","price":4599,"tag":"Relaxed arrival","color":"green"},
]

@app.template_filter("inr")
def inr(value):
    return "₹{:,.0f}".format(value)

@app.route("/")
def index():
    return render_template("index.html", flights=FLIGHTS[:3], today=datetime.now().strftime("%Y-%m-%d"))

@app.route("/search")
def search():
    origin = request.args.get("origin", "HYD").upper().strip()
    destination = request.args.get("destination", "").upper().strip()
    date = request.args.get("date", "")
    passengers = request.args.get("passengers", "1")
    results = [f for f in FLIGHTS if (not origin or f["from_code"] == origin) and (not destination or destination in (f["to_code"], f["to_city"].upper()))]
    if not results:
        results = [f for f in FLIGHTS if not destination or destination in (f["to_code"], f["to_city"].upper())]
    return render_template("results.html", flights=results, origin=origin, destination=destination, date=date, passengers=passengers)

@app.route("/book/<flight_id>", methods=["GET", "POST"])
def book(flight_id):
    flight = next((f for f in FLIGHTS if f["id"] == flight_id), None)
    if flight is None:
        flash("That sample flight could not be found.", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        passengers = request.form.get("passengers", "1")
        if not name or not email:
            flash("Please enter your name and email to continue.", "error")
            return render_template("book.html", flight=flight)
        # Demo only: no database persistence, ticket issuance, or payment processing.
        reference = "VY-DEMO-" + datetime.now().strftime("%H%M%S")
        return render_template("confirmation.html", flight=flight, name=name, email=email, passengers=passengers, reference=reference)
    return render_template("book.html", flight=flight)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
