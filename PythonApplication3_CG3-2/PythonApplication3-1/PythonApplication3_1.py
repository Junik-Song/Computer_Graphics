import glfw
from OpenGL.GL import *
import numpy as np


shapetype=GL_LINE_LOOP

def key_callback(window, key, scancode, action, mods): 
    
    global shapetype

    if key==glfw.KEY_1 and action==glfw.PRESS: 
        shapetype=GL_POINTS
    elif key==glfw.KEY_2 and action==glfw.PRESS: 
        shapetype=GL_LINES
    elif key==glfw.KEY_3 and action==glfw.PRESS: 
        shapetype=GL_LINE_STRIP
    elif key==glfw.KEY_4 and action==glfw.PRESS: 
        shapetype=GL_LINE_LOOP
    elif key==glfw.KEY_5 and action==glfw.PRESS: 
        shapetype=GL_TRIANGLES
    elif key==glfw.KEY_6 and action==glfw.PRESS: 
        shapetype=GL_TRIANGLE_STRIP
    elif key==glfw.KEY_7 and action==glfw.PRESS: 
        shapetype=GL_TRIANGLE_FAN
    elif key==glfw.KEY_8 and action==glfw.PRESS: 
        shapetype=GL_QUADS
    elif key==glfw.KEY_9 and action==glfw.PRESS: 
        shapetype=GL_QUAD_STRIP
    elif key==glfw.KEY_0 and action==glfw.PRESS: 
        shapetype=GL_POLYGON
    else:
        return



def render(shapetype): 
    glClear(GL_COLOR_BUFFER_BIT) 
    glLoadIdentity() 
    glBegin(shapetype)
    a = np.arange(0,360,30)
    for i in a:
        angle = i*3.141592 / 180
        glVertex2f(np.cos(angle), np.sin(angle))
    glEnd()


def main():
    # Initialize the library 
    if not glfw.init(): 
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480,480,"CG_weekly_practice_03-1_2016024884", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll events   
        glfw.poll_events()
        
        render(shapetype)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        

    glfw.terminate()

if __name__ == "__main__":
    main()