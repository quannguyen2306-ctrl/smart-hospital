from cgitb import html
from crypt import methods
from threading import main_thread
from flask import Blueprint, render_template, request, flash
import json
from numpy import number
from requests import delete
from website.models import Prescripion, Patient
from . import db 

views = Blueprint("views", __name__)
@views.route('/')
def home():
    return render_template("home.html")
@views.route('/patient')
def patient():
    return render_template("patient.html")

listMedicine = []
med_length = len(listMedicine)

@views.route('/pre', methods=['GET', 'POST'])
def pre():
    return render_template("prescription.html")

@views.route('/post_prescription', methods=['POST'])
def post_prescription():
    output = request.get_json()
    result = json.loads(output)
    print(result)
    numberPatient = int(result["patient_number"])
    roomPatient = int(result["room"])
    # patientObj = Patient.query.filter_by(room_number=roomPatient, number=numberPatient).first()
    # patient_first_name = patientObj.first_name
    # patient_last_name = patientObj.last_name
    pre = Prescripion(
        doctor_name = result["doctor_name"],
        room_number = roomPatient,
        patient_number = numberPatient,
        medicine_list = json.dumps(result["medicine_list"]),
        amount_list = json.dumps(result["amount_list"]),
        delivery_time = json.dumps(result["delivery_time"])
    )
    db.session.add(pre)
    db.session.commit()
    print(Prescripion.query.filter_by(
        doctor_name = result["doctor_name"],
        room_number = roomPatient,
        patient_number = numberPatient,
        medicine_list = json.dumps(result["medicine_list"]),
        amount_list = json.dumps(result["amount_list"]),
        delivery_time = json.dumps(result["delivery_time"])
    ).first())
    return result


@views.route('/medicine')
def medicine():
    return render_template("medicine.html")


@views.route('/history')
def history():
    all_prescription = Prescripion.query.all()
    all_medicine = []
    for i in all_prescription:
        all_medicine.append(json.loads(i.medicine_list))
    all_amount = []
    for i in all_prescription:
        all_amount.append(json.loads(i.amount_list))
    return render_template("history.html", data=all_prescription, medicine=all_medicine, amount=all_amount)


