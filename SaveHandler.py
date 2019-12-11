import pickle
from pathlib import Path

class SaveHandler:
    def __init__(self, fname):
        self.fname = fname

    def hasSavedData(self):
        path = Path(self.fname)
        return path.is_file()

    def dump(self, object):
        with open(self.fname, 'wb') as fp:
            pickle.dump(object, fp)

    def load(self):
        object = None
        with open(self.fname, 'rb') as fp:
            object = pickle.load(fp)
        return object
