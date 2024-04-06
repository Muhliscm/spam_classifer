from flask import Blueprint, render_template, request, flash
import pandas as pd
from .utils import predict


views = Blueprint('views', __name__)


@views.route("/home", methods=["GET", "POST"])
@views.route("/", methods=["GET", "POST"])
def home():
    outputs = []
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash("Add some inputs", category="error")
        else:
            flash("Your Query Submitted", category="success")
            prediction, probability = predict(text)
            if prediction == 1:
                o1 = "Spam!!"
                probability = probability[-1]
                o2 = "Confidence: {}".format(probability*100)
            else:
                o1 = "Not Spam "
                probability = probability[0]
                o2 = "Confidence: {}".format(probability*100)

            outputs = [o1, o2]

    return render_template('home.html', outputs=outputs)
