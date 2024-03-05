# 21698102_Shubham_srip
Extracting components from thermal video having frequency range 0-1 Hz.


Video Frequency Analysis using Fast Fourier Transform (FFT):

This repository contains a Python script for analyzing video frequency components in the range of 0 to 1 Hz using Fast Fourier Transform (FFT). The script reads a video file, calculates frame differences, performs FFT on the frames, and detects peaks in the frequency spectrum within the specified range.

#Requirements
Python 3
OpenCV (cv2)
NumPy

#Installation
1) Clone the repository to your local machine

2) Install the required Python libraries:
pip install opencv-python numpy

#Usage
1) Replace the video_path variable in the script with the path to your video file.
2) Run the script:
 python video_analysis.py

The script will analyze the video and print the number of components with frequencies in the range of 0 to 1 Hz.

#Customization
You can adjust parameters such as the threshold for detecting peaks (np.mean(filtered_magnitude_spectrum) + 3 * np.std(filtered_magnitude_spectrum)) according to your requirements.
Experiment with different frequency ranges or analysis techniques as needed.

#Credits:
1) I have used openCV library documentation.
2) I have referred to this github repo - https://github.com/jchrisweaver/vidpipe.git
3) I have referred to repos and projects related to video processing using openCV from "KAGGLE".
