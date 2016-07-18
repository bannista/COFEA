from flask import Flask
from flask import url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! wuzzzuuuup'


if __name__ == '__main__':
    app.run()

@app.route("/appointments/")
def appointment_list():
    return "listing of all appointments we have."

@app.route("/appointments/<int:appointment_id>/")
def appointment_detail(appointment_id):
    edit_url = url_for("appointment_edit",appointment_id = appointment_id)
    return "Detail of appointment  #{}.".format(appointment_id)

@app.route(
    "/appointments/<int:appointment_id>/edit/",
    methods=["GET","POST"])

@app.route("/run")
def appointment_edit():
    return"You shall not pass!"

def appointment_edit(appointment_id):
    return"Form to edit appointment #.".format(appointment_id)

@app.route(
    "/appointments/create/",methods=["GET","POST"])
def appointment_create():
    return"Form to create a new appointment."

@app.route(
    "/appoinments/<int:appointment_id>/delete/",
    methods=["DELETE"])
def appointments_delete(appointment_id):
    raise NotImplementedError("DELETE")


