from flask import Flask, render_template, request

app = Flask(__name__)

scores = []

@app.route("/", methods=["GET", "POST"])
def home():

    global scores
    total = None

    if request.method == "POST":

        if "reset" in request.form:
            scores.clear()

        else:
            score = float(request.form["score"])

            if len(scores) < 5:
                scores.append(score)

            if len(scores) == 5:

                highest = max(scores)
                lowest = min(scores)

                total = sum(scores) - highest - lowest

    return render_template(
        "index.html",
        scores=scores,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)