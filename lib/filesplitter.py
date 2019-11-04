import os
import subprocess

class split:

    def __init__(self):

        self.rootdir = ""
        self.linesize = 0
        self.filename = ""
        self.outputs = ""
    
    def filesplitter(self,linesize,filename,outputs):
        print("Splitting file: %s into %s lines with prefix %s" % (filename,linesize,outputs))
        subprocess.call(['split','-l',linesize,filename,outputs])

    def removebasefile(filename):
        print("Removing %s" % filename)
        subprocess.call(['rm',filename])

    def recursivesplitter(self,linesize,rootdir,outputs):
        for folder,subs,files in os.walk(rootdir):
            for f in files:
                filename = os.path.join(folder, f)
                print("Splitting file: %s into %s lines with prefix %s" % (filename,linesize,outputs))
                subprocess.call(['split','-l',linesize,filename,filename+outputs])
