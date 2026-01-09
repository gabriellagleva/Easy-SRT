from faster_whisper import WhisperModel
import argparse

def formatter(time):
    timetracker = time
    hourtracker = 0
    minutetracker = 0
    secondtracker = 0
    militracker = 0
    while timetracker > 3600:
        hourtracker +=1
        timetracker -= 3600
    while timetracker > 60:
        minutetracker +=1
        timetracker-=60
    secondtracker = int(timetracker)
    militracker = int((timetracker - secondtracker) * 1000)

    return f"{hourtracker:02d}:{minutetracker:02d}:{secondtracker:02d},{militracker:03d}"
    
    
# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate SRT subtitles from video using Whisper')
parser.add_argument('model_size', type=str, help='Whisper model size (e.g., tiny, base, small, medium, large-v3)')
parser.add_argument('video_file', type=str, help='Path to the video file')
parser.add_argument('--device', type=str, default='cuda', choices=['cuda', 'cpu'], 
                    help='Device to run on (default: cuda)')

args = parser.parse_args()

# Set compute_type based on device
if args.device == 'cuda':
    compute_type = "float16"
else:  # cpu
    compute_type = "int8"

# Initialize model with appropriate settings
model = WhisperModel(args.model_size, device=args.device, compute_type=compute_type)

segments, info = model.transcribe(args.video_file, beam_size=10)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

segmentcounter = 1
srtholder = ""
for segment in segments:
    print(segment.text)
    srtholder += str(segmentcounter) + "\n"
    srtholder += formatter(segment.start) + " --> " + formatter(segment.end) + "\n"
    srtholder += segment.text + "\n"
    srtholder += "\n"
    segmentcounter += 1


with open("output.srt", "w") as outfile:
    outfile.write(srtholder)
                      
