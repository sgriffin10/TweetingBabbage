from flask import Flask, escape, url_for, render_template, request
from Final_Project_Code import main
import random 
from random import choice

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app.route("/Final_Project_Code", methods= ["POST"]) #binds a function to a specified URL
def info_tweetingbabbage():
    """
    Will posts the images taken by the Teddy Bear onto Twitter with a random caption.
    """
    if request.method == "POST":
        status = request.form["status"]
        # wheelchair_boarding = str(request.form["wheelchair_boarding"]) 
        # print(place_name)
        camera.capture, status = main()

        return render_template(
            "input_results.html", status=status, #photo = photo or camera.capture = camera.capture
        )
    else:
        return render_template ("input_form.html", error=True)
    return render_template("input_form.html", error=None)
