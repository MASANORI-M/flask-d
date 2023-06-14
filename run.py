# import api.app as app

# run = app.create_app()
# print(run.url_map)
# run.run()

# from flask import Flask, render_template, request

# run = Flask(__name__)

# @run.route("/")
# @run.route("/index")
# def index():
#     name = request.args.get('name')
#     books = ["化学", "物理", "数学", "情報"]
#     return render_template("index.html", name = name, books = books)

# @run.route("/index", methods=["post"])
# def post():
#     name = request.form["name"]
#     books = ["化学", "物理", "数学", "情報"]
#     return render_template("index.html", name = name, books = books)


# if __name__ == "__main__":
#     run.run(debug=True)