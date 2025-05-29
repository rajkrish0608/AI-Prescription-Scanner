from flask import Flask, request, jsonify, render_template
from ocr import extract_text
from nlp import extract_medicines, extract_schedule, extract_conditions
from health_advisor import get_health_advice
import os

app = Flask(__name__, template_folder="templates")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_prescription():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded."}), 400

    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    extracted_text = extract_text(filepath)
    medicines = extract_medicines(extracted_text)
    schedule = extract_schedule(extracted_text)
    conditions = extract_conditions(extracted_text)

    return jsonify({
        "text": extracted_text,
        "medicines": medicines,
        "schedule": schedule,
        "conditions": conditions
    })

@app.route("/health-check", methods=["POST"])
def health_check():
    data = request.get_json()
    advice_data = get_health_advice(data)
    return jsonify(advice_data)

if __name__ == "__main__":
    app.run(debug=True)
