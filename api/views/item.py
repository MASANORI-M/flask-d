from flask import Flask, render_template, request, Blueprint
from ..models.item import Item

item = Blueprint('item_router', __name__)

@item.route("/")
def index():
    name = request.args.get('name')
    books = ["化学", "物理", "数学", "情報"]
    items = Item.query.all()
    print(items)
    return render_template("index.html", name = name, books = books, items = items)

# @item.route("/index", methods=["post"])
# def post():
#     name = request.form["name"]
#     books = ["化学", "物理", "数学", "情報"]
#     return render_template("index.html", name = name, books = books)