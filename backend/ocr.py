from PIL import Image
import pytesseract
import os

def extract_text(image_path):
    """
    Extract text from the given image using Tesseract OCR.
    :param image_path: Path to the image file
    :return: Extracted text as a string
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Example usage
if __name__ == "__main__":
    sample_image = "../uploads/sample_prescription.jpg"
    print("Extracted Text:\n", extract_text(sample_image))
