
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

Array = np.array([[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]])


def key_callback(window, key, scancode, action, mods): 
    
    global Array
    th = np.radians(10)
    Trans = np.array([[0.,0.,0.1], [0.,0.,0.], [0.,0.,0.]])
    Scale = np.array([[0.9,0.,0.], [0.,1.,0.], [0.,0.,1.]])

    if key==glfw.KEY_1 and (action==glfw.PRESS or action==glfw.REPEAT): 
        Array = np.array([[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]])
    # Translate
    elif key==glfw.KEY_Q and (action==glfw.PRESS or action==glfw.REPEAT):
        Array = Array-Trans
    elif key==glfw.KEY_E and (action==glfw.PRESS or action==glfw.REPEAT):
        Array=Array+Trans
    # Rotate by local coordinate
    elif key==glfw.KEY_A and (action==glfw.PRESS or action==glfw.REPEAT):
        Rot = np.array([[np.cos(th), -np.sin(th),0.], [np.sin(th), np.cos(th),0.],[0.,0.,1.]])
        Array = Array@Rot
    elif key==glfw.KEY_D and (action==glfw.PRESS or action==glfw.REPEAT):
        Rot = np.array([[np.cos(-th), -np.sin(-th),0.], [np.sin(-th), np.cos(-th),0.],[0.,0.,1.]])
        Array = Array@Rot
    # Scale
    elif key==glfw.KEY_W and (action==glfw.PRESS or action==glfw.REPEAT):
        Array = Scale @ Array

    # Rotate by global coordinate
    elif key==glfw.KEY_S and (action==glfw.PRESS or action==glfw.REPEAT):
        Rot = np.array([[np.cos(th), -np.sin(th),0.], [np.sin(th), np.cos(th),0.],[0.,0.,1.]])
        Array = Rot @ Array

    else:
        return


def render(T): 
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()


    glBegin(GL_LINES) 
    glColor3ub(255, 0, 0) 
    glVertex2fv(np.array([0.,0.])) 
    glVertex2fv(np.array([1.,0.])) 
    glColor3ub(0, 255, 0) 
    glVertex2fv(np.array([0.,0.])) 
    glVertex2fv(np.array([0.,1.])) 
    glEnd()

    # draw triangle 
    glBegin(GL_TRIANGLES) 
    glColor3ub(255, 255, 255) 
    glVertex2fv( (T @ np.array([.0,.5,1.]))[:-1] ) 
    glVertex2fv( (T @ np.array([.0,.0,1.]))[:-1] ) 
    glVertex2fv( (T @ np.array([.5,.0,1.]))[:-1] )
    
    glEnd()

def main():
    # Initialize the library 
    if not glfw.init(): 
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480,480,"CG_weekly_practice_04_2016024884", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)

    glfw.make_context_current(window)


    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll events   
        glfw.poll_events()
       
        global Array
        render(Array)

        # Swap front and back buffers
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()

