import matplotlib.pyplot as plt

class Artist(object):

    def __init__(self):
        pass

    def setup_figure(self, *args, **kwargs):
        self.figure = plt.figure(*args, **kwargs)
        self.axes = self.figure.add_subplot(111)
