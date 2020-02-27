from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    #print('test')
    f = open(fname, "r")
    f1 = f.read()
    commands = f1.split("\n")[:-1]
    add = 0
    #print(commands)
    for i in range(len(commands)):
        print(commands[i])
        if commands[i] == 'ident':
            ident(transform)
        if commands[i] == 'apply':
            matrix_mult(transform, points)
        if commands[i] == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        if commands[i] == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, commands[i+1])
            add = 1
        if commands[i] == 'line':
            pts = commands[i+1].split()
            add_edge(points, pts[0], pts[1], pts[2], pts[3], pts[4], pts[5])
            add = 1
        if commands[i] == 'scale':
            pts = commands[i+1].split()
            temp = make_scale(pts[0], pts[1], pts[2])
            matrix_mult(temp, transform)
            add = 1
        if commands[i] == 'translate':
            pts = commands[i+1].split()
            temp = make_translate(pts[0], pts[1], pts[2])
            matrix_mult(temp, transform)
            add = 1
        if commands[i] == 'rotate':
            pts = commands[i+1].split()
            temp = new_matrix()
            if pts[0] == 'x':
                temp = make_rotX(pts[1])
            if pts[0] == 'y':
                temp = make_rotY(pts[1])
            if pts[0] == 'z':
                temp = make_rotZ(pts[1])
            matrix_mult(temp, transform)
            add = 1
        if commands[i] == 'quit':
            break
        i += add
        add = 0
