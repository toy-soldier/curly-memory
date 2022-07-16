"""Defines the Chart class."""
import io
from abc import ABCMeta, abstractmethod
from openpyxl.drawing import image


class Chart(metaclass=ABCMeta):
    """Parent class of all charts."""
    def __init__(self, data):
        self._data = data

    @abstractmethod
    def draw_chart(self):
        """Draw a chart to represent the data."""

    def get_image(self):
        """Return the image representation of the chart."""
        img = io.BytesIO()
        fig = self.draw_chart()
        fig.savefig(img, format="png")
        img.seek(0)
        return image.Image(img)