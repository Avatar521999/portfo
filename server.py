from flask import Flask, render_template, request, url_for, redirect
import csv
# render_template allow us to send html files

app = Flask(__name__)
# print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html") 

def write_to_file(data):
    with open("database.text", mode="a") as database:
        name  = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f"\n {name}, {email}, {message}")
        
def write_to_csv(data):
    with open("database.csv" , mode="a") as database2:
        name  = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', lineterminator='\n' ,quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])
        
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/#thank_you")
        except:
            return "did not save to database"
    else:
        return "something went wrong"



# @app.route("/about.html")
# def about():
#     return render_template("about.html")


# dynamically access page 
# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(page_name)
    







# flask --app server run           # to run 
# flask --app server run --debug   # to on the debug mode
# .venv\Scripts\activate           # run environment variable
# py -3 -m venv .venv              # create venv