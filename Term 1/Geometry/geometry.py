#benjamin vielstich 
#9/11/2019
#geometry homework
#test





































#Errors: Format in the first square, circle and triangle-logic error.
#Forgot the input() at the end-runtime error.
#Able to break the program by inputting a letter and special characters- runtime error.
#Didn't double the amount of backslashes-syntax error.
#Mispelled perimeter- logic error.
#Improper punctuation- logic error.
#Can't input units- runtime error.
#Able to have negative answers - logic error.
#Found by April Fuentes, Rachel Thomas, Bryan Morris, Daniel Embley

#defines tha main menu
def intro():
    print("""
    Please input an option from below

    1:Area and perimeter of a square
    2:Circumference of a circle
    3:Area of a triangle
    4:Volume of a cube
    5:Quit
    """)

def square():
    #perimeter and area of square
    print("Preimeter and area of a square")

    #gets the length of the square
    sqr_side = input("What is the length of the square?")
    sqr_unit = input("What is the unit of mesurement?")

    #calculates the perimeter
    perimeter = int(sqr_side)*4

    #calculates the area
    sqr_area = int(sqr_side)*int(sqr_side)

    #prints the perimeter and area
    sqr = str.format("""                            {}
                       +--------+
                       |        |
                   {}   |        |  {}
                       |        |
                       +--------+
                             {}
    Perimeter {} {}
    Area      {} square {}""",sqr_side,sqr_side,sqr_side,sqr_side,perimeter,sqr_unit,sqr_area,sqr_unit)
    print(sqr)

def circle():
    #circumference of a circle
    print("Circumference of a circle")

    #gets the radius
    rad = input("What is the radius?")
    cir_unit = input("What is the unit of mesurement?")

    #sets pi
    pi = 3.14

    #calculates the circumference
    circ = pi*int(rad)**2

    #prints the circumference
    crcl = str.format("""
                           * *
                         *   {} *
                        *   ----*
                         *     *
                           * *
    Circumference {} {}""",rad,circ,cir_unit)
    print(crcl)

def triangle():
    #area of a triangle
    print("Area of a triangle")

    #gets the base and height
    base = input("What is the base?")
    height = input("What is the height?")
    tri_unit = input("What is the unit of mesurement?")

    #calculates the area
    tri_area = 0.5*int(base)*int(height)

    #prints the area
    tri = str.format("""
                  /\\
                 /| \\
                /{}|  \\
               /  |   \\
               ---------
                   {}
    Area {} square {}""",height,base,tri_area,tri_unit)
    print(tri)

def cube():
    #volume of a cube
    print("Volume of a cube?")

    #gets the length of the side
    side = input("What is the length of a side?")
    cube_unit = input("What is the unit of mesurement?")

    #calculates the volume
    vol = int(side)**3

    #prints the volume
    cube = str.format("""
          +----+
         /    /|
        +----+ |  All sides are {} {} long
        |    | +
        |    |/
        +----+

    Volume {} {} cubed""",side,cube_unit,vol,cube_unit)
    print(cube)

def option5():
    verify = input("Do you really want to quit? y/n")
    verify = verify.lower()
    if "y" in verify:
        return True
    else:
        return False

def menu():
    while True:
        intro()
        choice = input()
        if choice == "1":
            square()
        elif choice == "2":
            circle()
        elif choice == "3":
            triangle()
        elif choice == "4":
            cube()
        elif choice == "5":
            verify = option5()
            if verify == True:
                break
            else:
                continue
        else:
            print("Try again")
menu()
print("Press ENTER to exit")
input()
