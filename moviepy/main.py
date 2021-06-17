# Import everything needed to edit video clips
from moviepy.editor import *

clip1 = VideoFileClip("noichuyen.mp4").subclip(50,60)
clip2 = VideoFileClip("thangnam.mp4").subclip(50,60)
clip3 = VideoFileClip("test.flv")

final_clip = concatenate_videoclips([clip2, clip3])
final_clip.resize(height=1080).write_videofile("edited_video.mp4")

