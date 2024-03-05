import cv2
import numpy as np

# Define video file path
video_path = video_path = "C:\\Users\\shubham kumar gupta\\Downloads\\1705951007967.mp4"
# Open video file
cap = cv2.VideoCapture(video_path)

# Initialize variables
frame_count = 0
prev_frame = None

# Get video frame rate
frame_rate = cap.get(cv2.CAP_PROP_FPS)

# Initialize counter for components with frequency 0-1 Hz
component_count = 0

# Loop through video frames
while cap.isOpened():
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break

    # Converting frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate frame difference and Fast Fourier Transform(FFT)
    if prev_frame is not None:
        diff_frame = gray_frame.astype(np.float32) - prev_frame.astype(np.float32)
        fft_frame = np.fft.fft2(diff_frame)

        # Calculating the magnitude spectrum of the FFT frame
        magnitude_spectrum = 20 * np.log(np.abs(fft_frame))

        # FFT frame dimensions
        rows, cols = fft_frame.shape

        # Create frequency range arrays
        freq_range_rows = np.fft.fftfreq(rows, 1 / frame_rate)
        freq_range_cols = np.fft.fftfreq(cols, 1 / frame_rate)

        # Reshape frequency range arrays to match the shape of the FFT frame
        freq_range_rows = np.tile(freq_range_rows[:, np.newaxis], (1, cols))
        freq_range_cols = np.tile(freq_range_cols[np.newaxis, :], (rows, 1))

        # Create a mask to filter out frequencies outside the desired range (0-1 Hz)
        freq_mask = np.logical_and(
            np.logical_and(freq_range_rows >= 0, freq_range_rows <= 1),
            np.logical_and(freq_range_cols >= 0, freq_range_cols <= 1)
        )

        # Apply the mask to the magnitude spectrum
        filtered_magnitude_spectrum = magnitude_spectrum * freq_mask

        # Find peaks in the filtered magnitude spectrum
        peaks = np.where(filtered_magnitude_spectrum > np.mean(filtered_magnitude_spectrum) + 3 * np.std(filtered_magnitude_spectrum))

        # Check if peak frequencies fall within the range of 0-1 Hz and count them
        for peak_row, peak_col in zip(peaks[0], peaks[1]):
            frequency_row = freq_range_rows[peak_row, peak_col]
            frequency_col = freq_range_cols[peak_row, peak_col]
            if 0 <= frequency_row <= 1 and 0 <= frequency_col <= 1:
                component_count += 1

    # Update previous frame
    prev_frame = gray_frame.copy()

# Release resources
cap.release()
cv2.destroyAllWindows()

# Print the number of components with a frequency of 0-1 Hz
print("Number of components with a frequency of 0-1 Hz:", component_count)
