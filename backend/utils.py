import os

def ensure_upload_folder(path="uploads"):
    """
    Ensure the upload folder exists.
    """
    os.makedirs(path, exist_ok=True)
    return path

def allowed_file(filename, allowed_extensions={"png", "jpg", "jpeg", "pdf"}):
    """
    Check if the uploaded file has a valid extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
