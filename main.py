from video_capture.video_input import VideoInput
# Import other necessary modules

def main():
    # Initialize the GUI

    # Setup video capture

    # Create an instance of VideoInput
    video_input = VideoInput()
    
    # Initialize video capture
    video_input.init_video_capture(1)  # Initialize video capture with default device
    video_input.display_stream()      # Display the camera feed
    print("Video capture initialized")
    
    # Initialize hand model simulation
    # hand_model_setup()


    # Start the event loop
    #app_gui.mainloop()

    # Cleanup on exit
    # cleanup_resources()

if __name__ == "__main__":
    main()