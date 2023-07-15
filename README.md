**YouTube Video Object Tracking
**
Python script for tracking objects in a YouTube video using various tracking algorithms provided by OpenCV.

**Required Libraries:
**youtube-dl: pip install youtube-dl
pytube: pip install pytube
OpenCV (headless version): pip install opencv-python-headless
OpenCV (contrib version): pip install opencv-contrib-python

**Usage**
1.Clone this repository or download the script file.
2.Install the dependencies mentioned in the prerequisites section.
3.Run the script using the following command:

```
python ObjectTracking.py
```

When prompted, enter the YouTube video link you want to track. For example:
```
Enter YouTube video link: https://www.youtube.com/watch?v=-u0AINRLfM4
```

**Choose a tracker type by entering the corresponding number:
BOOSTING**
MIL
KCF
TLD
MEDIANFLOW
CSRT
MOSSE

a.The script will download the YouTube video and initialize the selected tracker.
b.A window will open showing the video. To select a region of interest (ROI) for tracking, press the 'c' key and drag the mouse to define the bounding box. Release the mouse button to start tracking.
c.To stop the tracking, press the 'q' key.
d.After finishing the tracking process, the script will display a message indicating the completion.
