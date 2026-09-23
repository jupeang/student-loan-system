from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")

db = client["student_loan_system"]

applications_collection = db["applications"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/loan", methods=["POST"])
def loan():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data was received."
        }), 400

    name = data.get("name", "").strip()
    student_id = data.get("student_id", "").strip()
    course = data.get("course", "").strip()
    loan_amount = data.get("loan_amount")

    if not name:
        return jsonify({
            "error": "Full name is required."
        }), 400

    if not student_id:
        return jsonify({
            "error": "Student ID is required."
        }), 400

    if not course:
        return jsonify({
            "error": "Course is required."
        }), 400

    if loan_amount is None or loan_amount == "":
        return jsonify({
            "error": "Loan amount is required."
        }), 400

    try:
        loan_amount = float(loan_amount)
    except (ValueError, TypeError):
        return jsonify({
            "error": "Loan amount must be a number."
        }), 400

    if loan_amount <= 0:
        return jsonify({
            "error": "Loan amount must be greater than zero."
        }), 400

    existing_application = applications_collection.find_one({
        "student_id": student_id
    })

    if existing_application:
        return jsonify({
            "error": "This Student ID has already submitted a loan application."
        }), 400

    if loan_amount <= 50000:
        status = "Approved"
        message = "Congratulations! Your loan application is approved."
    else:
        status = "Not Approved"
        message = "Your loan application is not approved."

    application = {
        "name": name,
        "student_id": student_id,
        "course": course,
        "loan_amount": loan_amount,
        "status": status,
        "application_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("ABOUT TO SAVE TO MONGODB")

    result = applications_collection.insert_one(application)

    print("SAVED TO MONGODB:", result.inserted_id)

    return jsonify({
        "message": message,
        "status": status,
        "name": name,
        "student_id": student_id,
        "course": course,
        "loan_amount": loan_amount,
        "application_date": application["application_date"]
    })


@app.route("/api/applications", methods=["GET"])
def get_applications():

    applications = []

    rows = applications_collection.find().sort("_id", -1)

    for row in rows:
        applications.append({
            "id": str(row["_id"]),
            "name": row["name"],
            "student_id": row["student_id"],
            "course": row["course"],
            "loan_amount": row["loan_amount"],
            "status": row["status"],
            "application_date": row.get("application_date", "Not available")
        })

    return jsonify(applications)


@app.route("/applications")
def applications_page():
    return render_template("applications.html")
@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")
@app.route("/api/dashboard", methods=["GET"])
def dashboard():

    total_applications = applications_collection.count_documents({})

    approved_applications = applications_collection.count_documents({
        "status": "Approved"
    })

    not_approved_applications = applications_collection.count_documents({
        "status": "Not Approved"
    })

    total_loan = 0

    rows = applications_collection.find()

    for row in rows:
        total_loan += row.get("loan_amount", 0)


    recent_applications = list(
        applications_collection.find(
            {},
            {
                "_id": 0,
                "id": 1,
                "name": 1,
                "student_id": 1,
                "course": 1,
                "loan_amount": 1,
                "status": 1
            }
        ).sort("id", -1).limit(5)
    )


    return jsonify({

        "total_applications": total_applications,

        "approved_applications": approved_applications,

        "not_approved_applications": not_approved_applications,

        "total_loan": total_loan,

        "recent_applications": recent_applications

    })


@app.route("/api/applications/<id>", methods=["DELETE"])
def delete_application(id):

    try:
        object_id = ObjectId(id)
    except Exception:
        return jsonify({
            "error": "Invalid application ID."
        }), 400

    result = applications_collection.delete_one({
        "_id": object_id
    })

    if result.deleted_count == 1:
        return jsonify({
            "message": "Application deleted successfully."
        })

    return jsonify({
        "error": "Application not found."
    }), 404


@app.route("/api/applications/<id>", methods=["PUT"])
def update_application(id):

    try:
        object_id = ObjectId(id)
    except Exception:
        return jsonify({
            "error": "Invalid application ID."
        }), 400

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data was received."
        }), 400

    name = data.get("name", "").strip()
    course = data.get("course", "").strip()
    loan_amount = data.get("loan_amount")

    if not name:
        return jsonify({
            "error": "Student name is required."
        }), 400

    if not course:
        return jsonify({
            "error": "Course is required."
        }), 400

    if loan_amount is None or loan_amount == "":
        return jsonify({
            "error": "Loan amount is required."
        }), 400

    try:
        loan_amount = float(loan_amount)
    except (ValueError, TypeError):
        return jsonify({
            "error": "Loan amount must be a number."
        }), 400

    if loan_amount <= 0:
        return jsonify({
            "error": "Loan amount must be greater than zero."
        }), 400

    if loan_amount <= 50000:
        status = "Approved"
    else:
        status = "Not Approved"

    result = applications_collection.update_one(
        {
            "_id": object_id
        },
        {
            "$set": {
                "name": name,
                "course": course,
                "loan_amount": loan_amount,
                "status": status
            }
        }
    )

    if result.matched_count == 0:
        return jsonify({
            "error": "Application not found."
        }), 404

    return jsonify({
        "message": "Application updated successfully.",
        "status": status
    })


if __name__ == "__main__":
    app.run(debug=True)

