from flask import Flask, render_template, request
harsh = Flask(__name__)

@harsh.route("/signin")
def home():
  return render_template('singin.html')



@harsh.route("/main", methods=["POST"])
def main():
    name = request.form.get("name")
    password=request.form.get("password")
    if(name=="harsh" and password=="jaimatadi"):
       return render_template('main.html')
