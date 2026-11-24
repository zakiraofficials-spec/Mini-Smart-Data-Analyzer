from flask import Flask, render_template, request
from main import analyze_numbers, get_ai_analysis

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    error = None
    ai_analysis = None
    raw_numbers = ""

    if request.method == "POST":
        raw_numbers = request.form.get("numbers", "").strip()

        try:
            results = analyze_numbers(raw_numbers)
            ai_analysis = get_ai_analysis(results)
        except ValueError as exc:
            error = str(exc)
        except Exception:
            # Keep unexpected technical details out of the page.
            error = "Something went wrong while analyzing your data. Please try again."

    return render_template(
        "index.html",
        results=results,
        error=error,
        ai_analysis=ai_analysis,
        raw_numbers=raw_numbers
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
