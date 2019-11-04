import os
import sys
import re
import gc

class parser:

    def __init__(self):

        self.rootdir = ""
        self.creds = []
        self.username = ""
        self.name = ""
        self.domain = ""
        self.password = ""
        
    def extract_creds(self,filename,delimiter):
        emailregex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        try:
            f = open(filename, "r")
            print("Parsing %s ..." % filename)
        except:
            print("Error opening file %s" % filename)
            pass
        try:
            for line in f:
                line.strip()
                line_index = line.split(delimiter)
                for i in line_index:
                    if len(line_index[0]) and len(i[0:]) > 0:
                        if re.match(emailregex, str(line_index[0])):
                            self.username = str(line_index[0]).strip()
                            self.password = str("".join(i[0:])).strip()
                        else:
                            pass
                    else:
                        pass
                if len(self.username) > 0:
                    username_index = self.username.split("@")
                    for i in username_index:
                        if len(username_index[0]) and len(i[0:]) > 0:
                            self.name = str(username_index[0]).strip()
                            self.domain = str(username_index[1]).strip()
                        else:
                           pass
                if len(self.username) < 128 and len(self.password) < 128:
                    self.creds.append([str(self.name),str(self.domain),str(self.password)])
                else:
                    pass
            return(self.creds)
            f.close()
        except:
            pass

    def credsize(self):
        return len(self.creds)

    def cleanup(self):
        self.creds = []
        gc.collect()
        return len(self.creds)
    
    def recursive_extract(self,rootdir,delimiter):
        try:
            for folder,subs,files in os.walk(rootdir):
                for f in files:
                    filename = os.path.join(folder, f)
                    self.extract_creds(filename,delimiter)
                    return(self.creds)
        except:
            print("Error opening %s" % filename)
    
