import cv2
import mediapipe as mp
from warnings import warn

filepath = 'C:/Users/afzal/Downloads/sample_720.mp4'

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For webcam input:
cap = cv2.VideoCapture(filepath)

with mp_face_detection.FaceDetection(
    model_selection = 1,
    min_detection_confidence = 0.5
) as face_detection:

    while cap.isOpened():

        # end feed
        if cv2.waitKey(1) == ord('q'):
            break

        success, image = cap.read()
        if not success:
            warn('File not found.')
            break
            #print("Webcam not detected.")
            # If loading a video, use 'break' instead of 'continue'.
            #continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        # Draw the face detection annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection,)

        cv2.imshow('MediaPipe Face Detection', image)


cap.release()
# Destroy all the windows
cv2.destroyAllWindows()