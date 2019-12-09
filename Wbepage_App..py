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
        choice(status) = request.form["status"]
        # wheelchair_boarding = str(request.form["wheelchair_boarding"]) 
        # print(place_name)
        photo, choice(status) = main()

        return render_template(
            "input_results.html", status=status, photo=photo
        )
    else:
        return render_template ("input_form.html", error=True)
    return render_template("input_form.html", error=None)
