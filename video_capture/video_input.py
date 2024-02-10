import cv2  # Import OpenCV
import mediapipe as mp  # Import Mediapipe
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class VideoInput:
    def __init__(self, device_index=0):
        self.running = True

        self.cap = cv2.VideoCapture(device_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Set the width of the frame
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500) # Set the height of the frame

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hand = self.mp_hands.Hands()
        self.result = None
        
        #self.hand_model = None
        #self.hand_data = None
        #self.hand_gestures = None

    def interpret_gestures(self, hand_data):
        # Check to see if the hand detection has been successful
        if hand_data is None:
            print("No hand result detected")
            return
        
        # Interpret the hand data

    def display_stream(self):
        if not self.cap.isOpened():
            print("Video capture not opened.")
            return

        while self.running:
            success, frame = self.cap.read()
            if success:
                self.hand_detection(frame) # Detect hand landmarks
                
                cv2.imshow('Test Camera', cv2.flip(frame, 1)) # Display a flipped frame
                if cv2.waitKey(1) == ord('q'):  # Press 'q' to close
                    break

        self.cap.release()
        cv2.destroyAllWindows()
  
    def hand_detection(self, frame):
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hand.process(RGB_frame)
        if self.result.multi_hand_landmarks:
            for hand_landmarks in self.result.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS,
                                                self.mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=6, circle_radius=4),
                                                self.mp_drawing.DrawingSpec(color=(16, 242, 16), thickness=2, circle_radius=2)
                                               )
                print(hand_landmarks)

    def close_stream(self):
        # Signal the loop to stop
        self.running = False
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()
        print("Video capture closed")