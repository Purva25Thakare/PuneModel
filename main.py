from flask import Flask, jsonify, render_template, request

from project_app.utils import PuneHouse

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Insurance Prediction System")   
    return render_template("index.html")


@app.route("/predict_charges", methods = ["POST", "GET"])
def get_house_price():
    if request.method == "GET":
        print("We are in a GET Method")

        area_type=request.args.get("area_type")
        availability=request.args.get("availability")
        size=request.args.get("size")
        total_sqft=eval(request.args.get("total_sqft"))
        bath=eval(request.args.get("bath"))
        balcony=eval(request.args.get("balcony"))
        site_location=request.args.get("site_location")
        
        pune = PuneHouse(area_type,availability,size,total_sqft,bath,balcony,site_location)
        price = pune.get_predicted_price()
        
        return render_template("index.html", prediction = price)
    
print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)