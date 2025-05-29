def get_health_advice(vitals):
    """
    Provide enhanced health advice based on input vitals.
    :param vitals: Dictionary with keys like 'bp', 'sugar', 'weight', etc.
    :return: Dictionary with advice and warnings
    """
    advice = []
    warnings = []

    # Blood Pressure
    try:
        systolic, diastolic = map(int, vitals.get('bp', '0/0').split('/'))
        if systolic >= 180 or diastolic >= 120:
            warnings.append("Hypertensive crisis — seek emergency care.")
            advice.append("Contact your doctor immediately.")
        elif systolic >= 140 or diastolic >= 90:
            warnings.append("High blood pressure (Hypertension Stage 2).")
            advice.append("Reduce salt intake. Exercise regularly. Monitor your BP closely.")
        elif systolic >= 130 or diastolic >= 80:
            warnings.append("Elevated blood pressure (Hypertension Stage 1).")
            advice.append("Adopt DASH diet. Reduce alcohol. Increase physical activity.")
        elif systolic < 90 or diastolic < 60:
            warnings.append("Low blood pressure detected.")
            advice.append("Stay hydrated. Eat small, frequent meals. Avoid alcohol.")
    except:
        warnings.append("Invalid BP format. Use systolic/diastolic format (e.g., 120/80).")

    # Sugar Level (Random or Post-meal)
    try:
        sugar = float(vitals.get('sugar', 0))
        if sugar >= 200:
            warnings.append("Very high blood sugar level.")
            advice.append("Consult your doctor. Avoid sugary and high-carb foods.")
        elif sugar >= 140:
            warnings.append("High blood sugar (Pre-diabetic/Post-meal warning).")
            advice.append("Limit sugary foods. Walk after meals. Get your HbA1c checked.")
        elif sugar < 70:
            warnings.append("Low blood sugar level.")
            advice.append("Take quick sugar (glucose tablet or juice). Eat regular meals.")
    except:
        warnings.append("Invalid sugar value. Use numeric format (e.g., 110).")

    # Weight Advice
    try:
        weight = float(vitals.get('weight', 0))
        if weight > 100:
            advice.append("High weight detected. Consider lifestyle changes and regular exercise.")
        elif weight < 45:
            advice.append("Underweight. Consult a nutritionist for a high-calorie balanced diet.")
    except:
        pass

    if not warnings:
        advice.append("Your vitals are within normal range. Keep maintaining a healthy lifestyle!")

    return {
        "warnings": warnings,
        "advice": advice
    }

# Example usage
if __name__ == "__main__":
    vitals = {
        "bp": "150/95",
        "sugar": "190",
        "weight": "105"
    }
    print(get_health_advice(vitals))
