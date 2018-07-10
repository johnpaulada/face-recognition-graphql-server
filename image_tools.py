import base64
from face_recognition import load_image_file, face_encodings
from img_rotate import fix_orientation

def base64_to_embedding(image_data, multiple=False):
    as_bytes = image_data.encode('utf-8')
    decoded = base64.decodestring(as_bytes)
    embedding = get_embedding(decoded, multiple)

    return embedding

def get_embedding(image, multiple=False):
    with open("temp.jpg", "wb") as f:
        f.write(image)

    try:
        fix_orientation("temp.jpg", save_over=True)
    except:
        print("Warning: Did not fix orientation because there was no EXIF data.")

    img = load_image_file('temp.jpg')
    encodings = face_encodings(img)

    return encodings if multiple else encodings[0]