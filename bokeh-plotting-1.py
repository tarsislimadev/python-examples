# Bokeh plotting example

## This is a simple example of how to create a line plot using Bokeh, a powerful interactive visualization library for Python. The code creates a figure, adds a line to it, and then displays the plot.
from bokeh.plotting import figure, show

## Create a new plot with a title and axis labels
p = figure(title="Simple Line Example", x_axis_label='x', y_axis_label='y')

## Add a line renderer with the specified x and y coordinates and line width
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

## Display the plot
show(p)
