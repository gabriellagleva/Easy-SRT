**Easy SRT**

A simple Python script to automatically generate SRT subtitle files from a video using the highly accurate FasterWhisper model.

This program takes a video file, transcribes the audio, and formats the output into a standard .srt file. SubRip files (.srt) are a common way to embed closed captions on platforms like YouTube, Vimeo, or in media players like VLC. This makes your content more accessible and engaging.

Features

1. Automatic Transcription: Leverages the powerful faster-whisper library for accurate speech-to-text.
2. Standard SRT Formatting: Creates a universally compatible .srt file with correct timestamps and sequencing.
3. Hardware Flexibility: Supports running on a CUDA-enabled GPU for maximum speed or on a CPU for broader compatibility.
4. Simple & Clean: A single script with minimal setup required.


Setup

Before you can run Easy SRT, please make sure that you have both Python and FasterWhisper installed on your machine.
You can install FasterWhisper by following the instructions provided by SYSTRAN: https://github.com/SYSTRAN/faster-whisper

How to Use

Getting your subtitles is easy! Just follow these steps:

1. Add Your Video: Place your video file (e.g., my_awesome_video.mp4) in the same directory as the Python script.

2. Edit the Script: Open the script and modify the following variables:
  2a. videoFileName: Change this to the exact name of your video file.
  2b. model_size: You can choose from models like tiny, base, small, medium, large-v2, or large-v3. Larger models are more accurate but require more resources. large-v3 is recommended for the highest accuracy.

3. Change videoFileName to the name of your video file!
```
videoFileName = "my_awesome_video.mp4" # <--- CHANGE THIS
model_size = "large-v3"
```
4. Select Your Device: The script is pre-configured to run on a GPU. If you want to run it on your CPU or change the compute type, simply comment out the active model line and uncomment the one you wish to use.
Python
```
# Run on GPU with FP16 (fastest, for modern GPUs)
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8 (uses less VRAM)
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")

# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")
```
5. Run the Script: Open your terminal or command prompt in the project directory and run the script.

```
python your_script_name.py
```
6. Get Your File: Once completed, a new file named output.srt will appear in the directory. You're all set!

