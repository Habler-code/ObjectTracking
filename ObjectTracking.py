
import cv2 as cv
from pytube import YouTube

def download_youtube_video(youtube_link, filename):
    print("Downloading the video...")
    yt = YouTube(youtube_link)
    yt.streams.first().download(filename=filename) 

def initialize_tracker(tracker_type):
    print("Initializing the tracker...")
    # OpenCV trackers:
    tracker = None
    try:
        # Try to use the current tracking API
        if tracker_type == "BOOSTING":
            tracker = cv.TrackerBoosting_create()
        elif tracker_type == "MIL":
            tracker = cv.TrackerMIL_create()
        elif tracker_type == "KCF":
            tracker = cv.TrackerKCF_create()
        elif tracker_type == "MEDIANFLOW":
            tracker = cv.TrackerMedianFlow_create()
        elif tracker_type == "CSRT":
            tracker = cv.TrackerCSRT_create()
        elif tracker_type == "MOSSE":
            tracker = cv.TrackerMOSSE_create()
    except AttributeError:
        # If current tracking API is not available, use the legacy tracking API
        if tracker_type == "BOOSTING":
            tracker = cv.legacy.TrackerBoosting_create()
        elif tracker_type == "MIL":
            tracker = cv.legacy.TrackerMIL_create()
        elif tracker_type == "KCF":
            tracker = cv.legacy.TrackerKCF_create()
        elif tracker_type == "MEDIANFLOW":
            tracker = cv.legacy.TrackerMedianFlow_create()
        elif tracker_type == "CSRT":
            tracker = cv.legacy.TrackerCSRT_create()
        elif tracker_type == "MOSSE":
            tracker = cv.legacy.TrackerMOSSE_create()
    return tracker


def track(frame, tracker):
    # Update the tracker with the current frame
    (success, box) = tracker.update(frame)
    # If the tracker successfully updated, draw a rectangle around the tracked object
    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return success, frame

def process_video(cap, tracker):
    BB = None 
    while True:
        ret, frame = cap.read()

        # If the bounding box is defined, track the object
        if BB is not None:
            success, frame = track(frame, tracker)

        # Display the frame
        cv.imshow("Frame", frame)

        # Wait for a key press and perform actions based on the key pressed
        key = cv.waitKey(1) & 0xFF

        # If 'c' is pressed, select ROI and initialize the tracker
        if key == ord("c"):
            BB = cv.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
            tracker.init(frame, BB)

        # If 'q' is pressed, break the loop
        elif key == ord("q"):
            break

    # Release video capture and close all windows
    cap.release()
    cv.destroyAllWindows()

def main():
    print("YouTube Video Object Tracking")

    # Prompt the user to enter the YouTube video link
    youtube_link = input("Enter the YouTube video link: ")

    # Prompt the user to choose a tracker type
    print("\nChoose a tracker type:")
    print("1. BOOSTING")
    print("2. MIL")
    print("3. KCF")
    print("4. MEDIANFLOW")
    print("5. CSRT")
    print("6. MOSSE")
    tracker_choice = int(input("Enter the corresponding number for the tracker type: "))
    tracker_types = [
        "BOOSTING",
        "MIL",
        "KCF",
        "MEDIANFLOW",
        "CSRT",
        "MOSSE"
    ]
    tracker_type = tracker_types[tracker_choice - 1]

    print("\nStarting the tracking...")

    filename = 'video.mp4'
    download_youtube_video(youtube_link, filename)

    tracker = initialize_tracker(tracker_type)

    # Load the video
    print("Loading the video...")
    cap = cv.VideoCapture(filename)

    process_video(cap, tracker)

    print("Finished processing.")

# Run the main function
main()
