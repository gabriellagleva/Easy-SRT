# **Easy SRT**

A simple Python script to automatically generate SRT subtitle files from a video using the FasterWhisper model.

This program takes a video file, transcribes the audio, and formats the output into a standard .srt file. SubRip files (.srt) are a common way to embed closed captions on platforms like YouTube, Vimeo, or in media players like VLC. This makes your content more accessible and engaging.

A demonstration of the program can be seen [here](https://www.youtube.com/watch?v=jIoNuMOXPPE), with it transcribing this interview of a park ranger in [South Carolina, Desegregating Edisto State Park](https://dare.wisc.edu/audio/south-carolina-desegregating-edisto-state-park/)

## **Features**

1. Automatic Transcription: Leverages the powerful faster-whisper library for accurate speech-to-text.
2. Standard SRT Formatting: Creates a universally compatible .srt file with correct timestamps and sequencing.
3. Hardware Flexibility: Supports running on a CUDA-enabled GPU for maximum speed or on a CPU for broader compatibility.
4. Simple & Clean: A single script with minimal setup required.


## **Setup**

Before you can run Easy SRT, please make sure that you have both Python and FasterWhisper installed on your machine.
You can install FasterWhisper by following the instructions provided by SYSTRAN: https://github.com/SYSTRAN/faster-whisper

## **How to Use**

Getting your subtitles is easy! Just run the script with command line arguments:

### **Basic Usage**

```bash
python easy-srt.py <model_size> <video_file> [--device <cuda|cpu>]
```

### **Arguments**

- `model_size` (required): Choose from `tiny`, `base`, `small`, `medium`, `large-v2`, or `large-v3`. Larger models are more accurate but require more resources. `large-v3` is recommended for highest accuracy.
- `video_file` (required): Path to your video file (can be relative or absolute path)
- `--device` (optional): Choose `cuda` for GPU or `cpu` for CPU. Defaults to `cuda`.

### **Device & Compute Types**

The script automatically selects the optimal compute type based on your device:
- **CUDA (GPU)**: Uses `float16` for maximum speed and accuracy (requires CUDA-enabled GPU)
- **CPU**: Uses `int8` for efficient processing on any computer

### **Examples**

1. **Run on GPU with large-v3 model (recommended):**
```bash
python easy-srt.py large-v3 my_video.mp4
```

2. **Run on CPU with medium model:**
```bash
python easy-srt.py medium my_video.mp4 --device cpu
```

3. **Process video from different folder:**
```bash
python easy-srt.py large-v3 C:\Videos\my_video.mp4
```

4. **Quick processing with smaller model:**
```bash
python easy-srt.py small my_video.mp4
```

### **Output**

Once completed, a file named `output.srt` will be created in the same directory as the script. You can then use this subtitle file with your video on YouTube, Vimeo, VLC, or any media player that supports SRT files.

### **Getting Help**


To see all available options:
```bash
python easy-srt.py --help
```

