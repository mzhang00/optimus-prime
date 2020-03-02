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
    f=open(fname,"r")
    count=0
    ident(transform)
    for instruct in f:
        count+=1
        if instruct == "line\n":
            instruct=f.readline().strip("\n").split(" ")
            edge=[int(instruct[0]),int(instruct[1]),int(instruct[2]),1]
            points.append(edge)
            edge=[int(instruct[3]), int(instruct[4]),int(instruct[5]),1]
            points.append(edge)
        elif instruct == "ident\n":
            ident(transform)
        elif instruct == "scale\n":
            instruct=f.readline().strip("\n").split(" ")
            scale=make_scale(int(instruct[0]),int(instruct[1]),int(instruct[2]))
            matrix_mult(scale,transform)
        elif instruct == "move\n":
            instruct=f.readline().strip("\n").split(" ")
            translate=make_translate(int(instruct[0]),int(instruct[1]),int(instruct[2]))
            matrix_mult(translate,transform)
        elif instruct == "rotate\n":
            instruct=f.readline().strip("\n").split(" ")
            if(instruct[0]=="x"):
                rotate=make_rotX(int(instruct[1]))
                matrix_mult(rotate,transform)
            elif(instruct[0]=="y"):
                rotate=make_rotY(int(instruct[1]))
                matrix_mult(rotate,transform)
            elif(instruct[0]=="z"):
                rotate=make_rotZ(int(instruct[1]))
                matrix_mult(rotate,transform)
            else:
                print("Invalid Argument at line "+str(count))
        elif instruct == "apply\n":
            matrix_mult(transform,points)
        elif instruct == "display\n":
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        elif instruct == "save\n":
            instruct=f.readline().strip("\n")
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,instruct)
        elif instruct == "quit\n":
            break
        else:
            print(instruct)
            print("Invalid Command at line "+str(count))
    f.close()