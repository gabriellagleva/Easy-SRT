from faster_whisper import WhisperModel

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
    
    
    
    
    
videoFileName = "" #name of video file in active directory

model_size = "large-v3"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe(videoFileName, beam_size=10)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

segmentcounter = 1
srtholder = ""
for segment in segments:
    srtholder += str(segmentcounter) + "\n"
    srtholder += formatter(segment.start) + " --> " + formatter(segment.end) + "\n"
    srtholder += segment.text + "\n"
    srtholder += "\n"
    segmentcounter += 1


with open("output.srt", "w") as outfile:
    outfile.write(srtholder)
                      
