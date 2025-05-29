import re
import spacy

nlp = spacy.load("en_core_web_sm")

# Sample lists for simple matching (can be expanded or replaced by ML models)
KNOWN_CONDITIONS = ["diabetes", "hypertension", "asthma", "fever", "cold", "infection"]
TIME_KEYWORDS = ["morning", "afternoon", "evening", "night", "before", "after", "meal", "breakfast", "lunch", "dinner"]


def extract_medicines(text):
    doc = nlp(text)
    medicines = []
    for ent in doc.ents:
        if ent.label_ in ["PRODUCT", "DRUG"] or re.match(r"[A-Z][a-z]+\s\d+mg", ent.text):
            medicines.append(ent.text)
    return list(set(medicines))


def extract_schedule(text):
    lines = text.split("\n")
    schedule = []
    for line in lines:
        if any(keyword in line.lower() for keyword in TIME_KEYWORDS):
            schedule.append(line.strip())
    return schedule


def extract_conditions(text):
    found = []
    for cond in KNOWN_CONDITIONS:
        if cond in text.lower():
            found.append(cond)
    return list(set(found))


# Example usage
if __name__ == "__main__":
    sample_text = """
    Take Metformin 500mg twice a day after meals.
    Condition: Type 2 Diabetes
    Paracetamol 650mg if fever persists.
    """
    print("Medicines:", extract_medicines(sample_text))
    print("Schedule:", extract_schedule(sample_text))
    print("Conditions:", extract_conditions(sample_text))
