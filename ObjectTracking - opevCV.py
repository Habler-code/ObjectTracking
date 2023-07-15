import cv2 as cv
from pytube import YouTube

def download_youtube_video(youtube_link, filename):
    print("Downloading the video...")
    yt = YouTube(youtube_link)
    yt.streams.first().download(filename=filename) 

def initialize_tracker(tracker_type):
    print("Initializing the tracker...")
    #OpenCV trackers:
    tracker = None
    if tracker_type == "BOOSTING":
        tracker = cv.TrackerBoosting_create()
    elif tracker_type == "MIL":
        tracker = cv.TrackerMIL_create()
    elif tracker_type == "KCF":
        tracker = cv.TrackerKCF_create()
    elif tracker_type == "TLD":
        tracker = cv.TrackerTLD_create()
    elif tracker_type == "MEDIANFLOW":
        tracker = cv.TrackerMedianFlow_create()
    elif tracker_type == "CSRT":
        tracker = cv.TrackerCSRT_create()
    elif tracker_type == "MOSSE":
        tracker = cv.TrackerMOSSE_create()
    return tracker

def track(frame, tracker):
    # Update the tracker with current frame
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

        # If bounding box is defined, track the object
        if BB is not None:
            success, frame = track(frame, tracker)

        # Display the frame
        cv.imshow("Frame", frame)

        # Wait for key press and perform actions based on the key pressed
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

def main(youtube_link, tracker_type):
    print("Starting the tracking...")

    filename = 'video.mp4'
    download_youtube_video(youtube_link, filename)

    tracker = initialize_tracker(tracker_type)

    # Load the video
    print("Loading the video...")
    cap = cv.VideoCapture(filename)

    process_video(cap, tracker)

    print("Finished processing.")

# Main function
youtube_link = 'https://www.youtube.com/watch?v=-u0AINRLfM4'  # car race video
tracker_type = "CSRT"  # replace with your choice: BOOSTING, MIL, KCF, TLD, MEDIANFLOW, CSRT, MOSSE
main(youtube_link, tracker_type)



