# P8_15.py
# Author: Austin Clayton
# This program converts an image to its color negative
# Date Created: 5/25/2018

from graphics import*

def main():

    print("This program converts an image to its color negative")

    infile = input("What is the file name?: ")
    outfile = input("What do you want to save the negative image as?: ")

    # Import image and find width and height 
    file = Image(Point(0,0), infile)
    width = file.getWidth()
    height = file.getHeight()

    # Get center of window
    cw = width / 2
    ch = height / 2
    center = Point(cw, ch)

    # Create graphics window
    image = Image(center,infile)
    win = GraphWin("Color Negative Image", width, height)
    image.draw(win)


    # Convert to color negative
    win.getMouse()
    x = 0
    y = 0

    for x in range(width):
        for y in range(height):
            r, g, b = image.getPixel(x, y)
            image.setPixel(x,y, color_rgb(255 - r, 255 - g, 255 - b)) 
            win.update()

    # Exit program
    image.save(outfile)
    win.getMouse()
    win.close()

main()
