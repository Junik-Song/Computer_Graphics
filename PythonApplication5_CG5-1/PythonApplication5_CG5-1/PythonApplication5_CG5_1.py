import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def drawUnitCube():
    glBegin(GL_QUADS)
    glVertex3f( 0.5, 0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f( 0.5, 0.5, 0.5) 
                             
    glVertex3f( 0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f( 0.5,-0.5,-0.5) 
                             
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)
                             
    glVertex3f( 0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f( 0.5, 0.5,-0.5)
 
    glVertex3f(-0.5, 0.5, 0.5) 
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5) 
    glVertex3f(-0.5,-0.5, 0.5) 
                             
    glVertex3f( 0.5, 0.5,-0.5) 
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)
    glVertex3f( 0.5,-0.5,-0.5)
    glEnd()

def drawCubeArray():
    for i in range(5):
        for j in range(5):
            for k in range(5):
                glPushMatrix()
                glTranslatef(i,j,-k-1)
                glScalef(.5,.5,.5)
                drawUnitCube()
                glPopMatrix()

def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,0]))
    glVertex3fv(np.array([0.,0.,1.]))
    glEnd()

def myOrtho(left, right, bottom, top, near, far): 
    # first, get an orthographic matrix
    x = np.array([2 / (right - left), 0, 0, 0])
    y = np.array([0, 2 / (top - bottom), 0, 0])
    z = np.array([0, 0, 2 / (near - far), 0])
    w = np.array([-(right + left)/(right - left), -(top + bottom)/(top - bottom), -(near + far)/(near - far), 1])
    M = np.array([x, y, z, w])
    glMultMatrixf(M)

def myLookAt(eye, at, up):
    #Eye:5, 5, 3 at:1, 1, -1, up:0, 1, 0
    forward = eye - at
    forward = forward / np.sqrt(np.sum(forward**2))
    side = np.cross(up, forward)
    side = side / np.sqrt(np.sum(side**2))
    newup = np.cross(forward, side)
    pos = np.array([-np.dot(eye, side), -np.dot(eye, newup), -np.dot(eye, forward)])
    x = np.array([side[0], newup[0], forward[0], 0.0])
    y = np.array([side[1], newup[1], forward[1], 0.0])
    z = np.array([side[2], newup[2], forward[2], 0.0])
    w = np.array([pos[0], pos[1], pos[2], 1.0])
    inpVM = np.array([x, y, z, w])
    glMultMatrixf(inpVM)


def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()

    myOrtho(-5, 5, -5, 5, -8, 8)
    myLookAt(np.array([5, 3, 5]), np.array([1, 1, -1]), np.array([0, 1, 0]))
    # above is equivalent to:
    # glOrtho(-5, 5, -5, 5, -8, 8)
    # gluLookAt(5, 3, 5, 1, 1, -1, 0, 1, 0)

    drawFrame()

    glColor3ub(255, 255, 255)
    drawCubeArray()




def main():
    if not glfw.init():
        return 
    window = glfw.create_window(480, 480, "CG_weekly_practice_05-1_2016024884", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
