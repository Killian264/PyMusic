from tinytag import TinyTag
import math
from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaContent

# tinytag gets
'''
{
  'filesize': 3031559, 
  'album': None, 
  'albumartist': None, 
  'artist': None, 
  'audio_offset': 5668, 
  'bitrate': None, 
  'channels': 2, 
  'comment': None, 
  'composer': None, 
  'disc': None, 
  'disc_total': None, 
  'duration': 2.56, 
  'genre': None, 
  'samplerate': 44100, 
  'title':None, 
  'track': None, 
  'track_total': None, 
  'year': None
}
'''

# My current plan for class
# init takes file loc and gets base details on it stuff needed to show
# if the song is played or if later on the user can look at the info on the file show information got from the properties of the file
# if the user wants to change these properties they can and it will change for the file
# thus never storing much and keeping memory low
class Song():
    def __init__(self, location, fileName):
        self.location = location
        self.fileName = fileName
        # for now duration will be (min, sec) to get proper time min + (sec / 100)
        self.duration = self.getDuration()

    def getDuration(self):
        ret = self.location + '/' + self.fileName
        tag = TinyTag.get(ret)
        return splitDuration(tag.duration)

    def returnMediaContent(self):
        url = QtCore.QUrl.fromLocalFile(self.location + '/' + self.fileName)
        return QMediaContent(url)


def splitDuration(duration):
    min = math.floor(duration / 60)
    sec = math.floor(duration % 60)
    return min,sec

