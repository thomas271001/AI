import cv2 as cv
from deepface import DeepFace

cap = cv.VideoCapture(0)
while True:
    ret,frame =cap.read()
    results=DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)

    emotion =results[0]['dominant_emotion']
    cv.putText(frame,f'Emotion:{emotion}',(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv.imshow("Emotion Recognition",frame)

    if cv.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
