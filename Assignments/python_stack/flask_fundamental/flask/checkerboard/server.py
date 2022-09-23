from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:i>/<int:j>/<box1>/<box2>")
def index_with_variable(i,j,box1,box2):
    return render_template("index_with_variables.html",x=i, y=j,color1 = box1, color2=box2)

if __name__ == "__main__":
    app.run(debug=True)