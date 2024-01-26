from flask import Flask, render_template

app =Flask(__name__)


@app.route('/')
def Student():
    return render_template('Student.html')

@app.route( rule: '/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST'
        result=request.form
        return render_template('template_name_or_list: "result.html", result=result')


if __name__ == "__main__":
    app.run(debug=True)