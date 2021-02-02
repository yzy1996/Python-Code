import os


command = 'ffmpeg ' + '-y -f s16le -ar 16000 -i ' + 'demo.pcm' + ' aa' + '.wav'
os.system(command)