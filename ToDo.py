from flask import Flask, request, render_template

app = Flask(__name__)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)
    return render_template("index.html", tasks=tasks)

@app.route("/delete", methods=["POST"])
def delete():
    task_index = int(request.form["index"])
    del tasks[task_index]
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
