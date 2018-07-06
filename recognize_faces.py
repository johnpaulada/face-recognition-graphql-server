import base64
import numpy as np
from face_recognition import load_image_file, face_encodings

def recognize_faces(image_data):
    return ["John Paul Ada"]

def get_names():
    names = []

    try:
        with open("names.txt", "r") as name_file:
            for line in name_file:
                names.append(line)
    except FileNotFoundError:
        with open("names.txt", "w") as name_file:
            name_file.write('')

    return names