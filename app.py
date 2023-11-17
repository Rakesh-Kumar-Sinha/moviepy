from moviepy.editor import *

# Create a list of texts for each frame
texts = ["Hello", "world", "i", "am", "testing"]


# Function to generate a video from texts
def create_text_video(texts, output_path='text_video.mp4', duration_per_frame=2):
    clips = []

    for text in texts:
        txt_clip = TextClip(text, fontsize=70, color='white', font='Arial').set_duration(duration_per_frame)
        clips.append(txt_clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path, fps=24)


# Create the video
create_text_video(texts)
