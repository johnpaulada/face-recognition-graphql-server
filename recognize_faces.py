import base64
import numpy as np
from face_recognition import compare_faces, load_image_file, face_encodings
from image_tools import base64_to_embedding

def recognize_faces(image_data):
    embeddings = base64_to_embedding(image_data, multiple=True)
    names = get_names()
    known_faces = np.load('embeddings.npy')
    matched_names = get_matched_names(known_faces, embeddings, names)
    trimmed_names = [x.strip(' \t\n\r') for x in matched_names]

    return trimmed_names

def get_matched_names(known_faces, embeddings, names):
    name_indices = get_name_indices(known_faces, embeddings)
    matched_names = names_from_indices(name_indices, names)

    return matched_names
    
def get_name_indices(known_faces, embeddings):
    name_indices = []

    for embedding in embeddings:
        matches = compare_faces(known_faces, embedding)
        indices = []

        for i, match in enumerate(matches):
            if match:
                indices.append(i)

        name_indices = name_indices + indices

    return name_indices

def names_from_indices(name_indices, names):
    matched_names = []

    for index in name_indices:
        matched_names.append(names[index])

    return matched_names

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