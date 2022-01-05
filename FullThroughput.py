import subprocess
#MAKE SURE TO CD INTO THE WORKING FILES' PROPER DIRECTORY

#RIPS AUDIO AND CREATES A FILE WITH NAME OUTPUTAUDIO.OPUS
def RipAudio(url, imageName, audioStart, audioLength):
	audio_call = "youtube-dl -x --audio-format mp3 -o aud_out.mp3 {}".format(url)
	subprocess.call(audio_call, shell=True)
	print("finished audio")
	ImageAudioToVideo(imageName,audioStart,audioLength)

#CONVERSION FROM PNG,JPEG/JPG TO MP4, MERGE AUDIO AND VIDEO AT SPECIFIED START 
#OFFSET (SECONDS) AND  OUTPUT LENGTH (SECONDS)
def ImageAudioToVideo(imageName,audioStart,audioLength):
	subprocess.call("ffmpeg -y -loop 1 -r 1 -i "+imageName+" -vf 'pad=ceil(iw/2)*2:ceil(ih/2)*2' -c:v libx264 -t " +str(audioLength)+" -pix_fmt yuv420p imageVideoOut.mp4", shell=True)
	print("finished video from image")
	subprocess.call("ffmpeg -y -i imageVideoOut.mp4 -ss "+str(audioStart)+" -to "+str(audioStart+audioLength)+" -i aud_out.mp3 -c:v copy -c:a aac -shortest AudioVideoOut.mp4", shell=True)
	subprocess.call("rm imageVideoOut.mp4", shell=True)
	

print('Image to Video'.center(40, '_'))
imagename = input('Enter file name : ')
url_name = input('Enter YouTube URL : ')
audiostart = input('Enter when the audio should begin (seconds) : ')
audiolength = input('Enter video duration : ')

RipAudio(url_name, imagename, audiostart, audiolength)
ImageAudioToVideo(imagename,audiostart,audiolength)