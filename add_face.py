import os
import numpy as np
from image_tools import base64_to_embedding

def add_face(name, image_data):
    embedding = base64_to_embedding(image_data)
    add_name(name)
    add_embedding(embedding)

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