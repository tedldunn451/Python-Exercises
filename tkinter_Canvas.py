# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Canvases

from tkinter import * # not a themed tk widget
root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas.config(width = 640, height = 480)

# use line variable to capture the  id of the line so that it can be referenced in the future for changes
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5) # params: xy pairs of coordinates referenced from top left corner of canvas, color, width
canvas.itemconfigure(line, fill = 'green') # change color of line
canvas.coords(line) # returns coordinates of line
canvas.coords(line, 0, 0 , 320, 240, 640, 0) # use to change coordinates of line and add another pair of xy coordiantes
canvas.itemconfigure(line, smooth = True) # smooths out line using smaller straight lines
canvas.itemconfigure(line, splinesteps = 5) # configures smooth line to be comprised of 5 straight lines
canvas.itemconfigure(line, splinesteps = 100) # higher number of splinesteps creates smoother lines

canvas.delete(line) # deletes line
canvas.delete(all) # clears everything from canvas

rect = canvas.create_rectangle(160,120,480,360) # 4 params representing opposite corners of rectangle
canvas.itemconfig(rect, fill = 'yellow')
oval = canvas.create_oval(160,120,480,360) # top left, bottom right corners of oval
arc = canvas.create_arc(160, 1, 480, 240) # same params as rec and oval
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green') # numbers are in degrees
poly = canvas.create_polygon(160,360,320,480,480,360, fill = 'blue') # you can add as many coordinates as you want

text = canvas.create_text(320,240, text = 'Python', font = ('Courier', 32, 'bold'))
logo = PhotoImage(file = 'filepath')
image = canvas.create_image(320,240, image = logo) # items added go to the top so add them in the appropriate order or using the lift / lower methods (see below)
canvas.lift(text)
canvas.lower(image) # pushes image down below all object to where it can't be seen
canvas.lower(image, text) # lower image to just below text object

button = Button(canvas, text = 'Click Me')
canvas.create_window(320, 60, window = button)

# all items on canvas have a unique id used to modify or further configure
# tags can also be applied to items to group them and pass the tags instead of the ids into a method
canvas.itemconfigure(rect, tag = ('shape'))
canvas.itemconfigure(oval, tag = ('shape', 'round'))
canvas.itemconfigure('shape', fill = 'grey')
canvas.gettage(oval) # returns tags associated with parameter
