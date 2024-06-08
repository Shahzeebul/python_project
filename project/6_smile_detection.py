import cv2

def detect_smile_in_image(image_path):
    # Load pre-trained cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load pre-trained cascade classifier for smile detection
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Flag to track if any smile is detected
    smile_detected = False

    # Detect smiles within detected faces
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

        if len(smiles) > 0:
            smile_detected = True
            break  # Exit loop if any smile is detected

    if smile_detected:
        print("Smile detected in the image!")
    else:
        print("No smile detected in the image.")

def main():
    # Ask for the image file path
    image_path = input("Enter the path of the JPG image file: ")

    # Check if the image is a valid JPG file
    if not image_path.lower().endswith('.jpg'):
        print("Error: Please provide a valid JPG image file.")
        return

    # Detect smile in the image
    detect_smile_in_image(image_path)

if __name__ == "__main__":
    main()
