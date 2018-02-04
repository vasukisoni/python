import time
import win32api

# Coordinates for left top : ( 0 , 0 )
# Coordinates for right bottom : ( 1365 , 767 )
# Coordinates for right top : ( 0 , 767 )
# Coordinates for left bottom : ( 1365 , 0 )
 
MOUSE_SPEED = .4 #seconds
 
def mouse_glide_to(x,y):
    """Smooth glides mouse from current position to point x,y with default timing and speed"""
    x1,y1 = win32api.GetCursorPos()
    smooth_glide_mouse(x1,y1, x, y, MOUSE_SPEED)
 
def smooth_glide_mouse(x1,y1,x2,y2, t, intervals):
    """Smoothly glides mouse from x1,y1, to x2,y2 in time t using intervals amount of intervals"""
    distance_x = x2-x1
    distance_y = y2-y1
    for n in range(0, intervals+1):
        move_mouse(x1 + n * (distance_x/intervals), y1 + n * (distance_y/intervals))
        time.sleep(t*1.0/intervals)
 
def move_mouse(x, y):
    win32api.SetCursorPos((x,y))


# use function move_mouse(x,y) to move the mouse pointer to any position
# use function win32api.GetCursorPos() to get current mouse position
