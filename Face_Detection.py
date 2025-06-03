import cv2 as cv
import mediapipe as mp

mp_face_mesh=mp.solutions.face_mesh
face_mesh=mp_face_mesh.FaceMesh()

cap =cv.VideoCapture(0)

while True:
    key,img=cap.read()
    rgb_frame = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            for point in landmarks.landmark:
                x, y = int(point.x * img.shape[1]), int(point.y * img.shape[0])
                cv.circle(img, (x, y), 1, (0,255,0), -1)

cv.imshow("my_video",img)
cv.waitKey(1)

