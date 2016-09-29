import matplotlib.pyplot as plt
import numpy as np

class MatPlotPloter:
    def __init__(self):
        """
        keep track of the figure number so that graphs won't be printed on the same figure
        """
        self.figure = 1
        
    def scatterPlot(self, x, y):
        """
        do a scatter plot with two lists x and y
        where the size of the bubble is related to the y value
        """
        plt.figure(self.figure)
        self.figure += 1
        colors = np.random.rand(len(y))
        size = [10 * np.pi * i ** 2 for i in y]
        plt.scatter(x, y, s = size, c = colors, alpha = 0.5)
        plt.show()
        
    def barGraph(self, x, y):
        """
        a horizontal bar graph just like in command line plotter
        takes in two lists x and y
        """
        plt.figure(self.figure)
        self.figure += 1
        plt.barh(y, x)
        plt.show()
