from moviepy.editor import *
import os
from shutil import rmtree

class FramesPerMinute:
    
    #constructor to set path and initialize other atttributes as neccessary
    def __init__(self, path):
        
        self.path = path
        self.clip = VideoFileClip(path)
        self. intervals = []
    
    # Calculates intervals based on duration of videos (in seconds)
    def minuteInterval(self):
        
        for interval in range(int(self.clip.duration)):
            if interval % 60 == 0:
                self.intervals.append(interval)
                
        self.intervals.append(int(self.clip.duration)) # add total duration (in seconds)
    
    # Determines the number of Frames per Interval
    def getFramesPerMin(self):
        
        counter = 0 # Keeps track of frames
        
        # create a new directory  under current working directory to  write the output data
        new_path = os.path.join(os.getcwd(), "output\\")
        if os.path.exists(new_path): # if directory exists overwrite it
            rmtree(new_path)
        os.makedirs(new_path) 
        
        # for each interval 
        for i in range(len(self.intervals)-1):

            #print(self.intervals[i+1], " - Counter Value ", end = " : ")
            fname = counter + 1 if counter > 0 else 0
            #print(fname)

            self.clip = VideoFileClip(self.path) # initialize video file object

            # generating a subclip for a interval
            self.clip = self.clip.subclip(self.intervals[i], self.intervals[i+1])
            
            
            # writing file as per guidelines
            self.clip.write_videofile(r"" + new_path + str(fname) + "thFrame.mov", codec = "libx264") 


            # count frames; using loop to transverse the frames
            frames = self.clip.iter_frames()
            for value in frames:
                counter += 1 # incrementing the counter

            self.clip.close() # close video file object
    
    # driver function to run the job
    def driver(self):
            
        self.minuteInterval()
        self.getFramesPerMin() 
        self.clip.close() # ensuring no memory in use
            
if __name__ == '__main__':
  
    # Calling the function
    filepath = "C:\\Users\\gsksa\\Downloads\\airshow.mp4" #input file path
    FramesPerMinute(filepath).driver()