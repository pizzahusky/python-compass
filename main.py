degrees = 0

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45: 
        basic.show_arrow(ArrowNames.NORTH)
    elif degrees < 135:
        basic.show_arrow(ArrowNames.EAST)
    elif degrees < 225:
        basic.show_arrow(ArrowNames.SOUTH)
    elif degrees < 315:
        basic.show_arrow(ArrowNames.WEST)
    else:
        basic.show_arrow(ArrowNames.NORTH)
basic.forever(on_forever)