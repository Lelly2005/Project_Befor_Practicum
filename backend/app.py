# Current app.py core functionality
from flask import Flask, render_template, request, Response
from dbcontext import db_data, db_delete, db_add, health_check
from person import Person

app = Flask(__name__)

@app.route("/")
def main():
    data = db_data()
    return render_template("index.html.jinja", host_name=host_name,
                         db_host=db_host, data=data, backend=backend)

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id: int):
    return db_delete(id)

@app.route("/add", methods=["PUT"])
def add():
    body = request.json
    if body is not None:
        person = Person(0, body["firstName"], body["lastName"],
                       body["age"], body["address"], body["workplace"])
        return db_add(person)
    return Response(status=404)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
