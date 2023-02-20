import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



def fig():
    data = pd.read_csv("test.csv")

    # Extract x and y data from the DataFrame
    x = data["time"]
    y = data["ratio"]

    # Create a figure and a canvas to render the chart in PyQt
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)

    # Create a line chart with a dashed line style
    ax.plot(x, y, linestyle='--')

    # Add y-axis values to every point
    for i, j in zip(x, y):
        ax.text(i, j, str(j))

    # Add chart title and axis labels
    ax.set_title("Line Chart Title")
    ax.set_xlabel("time")
    ax.set_ylabel("unlock ratio")

    return canvas
