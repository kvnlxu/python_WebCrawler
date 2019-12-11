import os

class SimpleFileWriter:
    def __init__(self, directory):
        self.dir = directory

    def rename(self, path, num):
        split = path.split(".")
        split[0] = split[0] + "_" + str(num)
        return ".".join(split)

    def validPath(self, path):
        i = 1
        tempPath = path
        while os.path.isfile(tempPath):
            tempPath = self.rename(path, i)
            i += 1
        return tempPath

    def write(self, fname, content):
        fpath = os.path.join(self.dir, fname)
        fpath = self.validPath(fpath)
        output_file = open(fpath, "w")
        output_file.write(content)
        output_file.close()
