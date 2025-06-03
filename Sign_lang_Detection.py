import cv2 as cv
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def recognize_gesture(landmarks):
    # Define key points
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]

    # Helper: Is finger extended?
    def is_finger_up(finger_tip, lower_joint):
        return finger_tip[1] < lower_joint[1]

    # Get necessary joints
    thumb_ip = landmarks[3]
    index_pip = landmarks[6]
    middle_pip = landmarks[10]
    ring_pip = landmarks[14]
    pinky_pip = landmarks[18]

    # THUMBS UP (Yes)
    if thumb_tip[1] < thumb_ip[1] and all(tip[1] > pip[1] for tip, pip in [
        (index_tip, index_pip), (middle_tip, middle_pip),
        (ring_tip, ring_pip), (pinky_tip, pinky_pip)]):
        return "Yes 👍"

    # THUMBS DOWN (No)
    if thumb_tip[1] > thumb_ip[1] and all(tip[1] < pip[1] for tip, pip in [
        (index_tip, index_pip), (middle_tip, middle_pip),
        (ring_tip, ring_pip), (pinky_tip, pinky_pip)]):
        return "No 👎"

    # OPEN HAND (Hello)
    if all(is_finger_up(tip, pip) for tip, pip in [
        (thumb_tip, thumb_ip), (index_tip, index_pip),
        (middle_tip, middle_pip), (ring_tip, ring_pip),
        (pinky_tip, pinky_pip)]):
        return "Hello 👋"

    # VICTORY (Peace)
    if (is_finger_up(index_tip, index_pip) and
        is_finger_up(middle_tip, middle_pip) and
        not is_finger_up(ring_tip, ring_pip) and
        not is_finger_up(pinky_tip, pinky_pip)):
        return "Peace ✌️"

    # FIST (Stop)
    if all(tip[1] > pip[1] for tip, pip in [
        (index_tip, index_pip), (middle_tip, middle_pip),
        (ring_tip, ring_pip), (pinky_tip, pinky_pip)]):
        return "Stop ✊"

    return "..."

# Start video capture
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
            gesture = recognize_gesture(landmarks)
            cv.putText(frame, f'Sign: {gesture}', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

    cv.imshow("Sign Language Detection", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
