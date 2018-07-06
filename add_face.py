import os
import base64
import numpy as np
from face_recognition import load_image_file, face_encodings

def add_face(name, image_data):
    as_bytes = image_data.encode('utf-8')
    decoded = base64.decodestring(as_bytes)
    embedding = get_embedding(decoded)
    add_name(name)
    add_embedding(embedding)

def get_embedding(image):
    with open("temp.jpg", "wb") as f:
        f.write(image)

    img = load_image_file('temp.jpg')

    return face_encodings(img)[0]

def add_name(name):
    with open('names.txt', 'a') as names_file:
        names_file.write(name)
        names_file.write('\n')

def add_embedding(embedding):
    if (not os.path.exists('embeddings.npy')):
        np.save('embeddings.npy', [embedding])
    else:
        embeddings = np.load('embeddings.npy')
        embeddings = np.concatenate((embeddings, [embedding]))
        np.save('embeddings.npy', embeddings)