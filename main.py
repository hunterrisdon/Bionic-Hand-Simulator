from video_capture.video_input import VideoInput
# Import other necessary modules

def main():
    # Create an instance of VideoInput
    video_capture = VideoInput()

    video_capture.__init__(1)       # Initialize video capture with MacBook Camera
    video_capture.display_stream()    # Display the camera and runs analysis on hands

    # Initialize the GUI that will display the hand gestures

if __name__ == "__main__":
    main()