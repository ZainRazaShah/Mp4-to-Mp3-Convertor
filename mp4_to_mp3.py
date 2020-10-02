import moviepy.editor as mp 

video = mp.VideoFileClip("File.mp4")  
audio = video.audio
 
audio.write_audiofile("Converted.mp3")  

print("Mp4 file converted to Mp3 Successfully !")  