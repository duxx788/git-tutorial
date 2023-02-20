import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class fig(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load CSV data into a pandas DataFrame
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

        # Create a layout and add the canvas to it
        layout = QVBoxLayout()
        layout.addWidget(canvas)

        # Create a widget and set the layout to it
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the main window to the widget
        self.setCentralWidget(widget)

        # Set window properties and show the window
        self.setWindowTitle("Line Chart Window Title")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("path/to/icon/file.png"))
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = fig()
    window.show()
    app.exec_()
