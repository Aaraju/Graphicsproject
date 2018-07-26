from Tkinter import *
#from Tkinter import messagebox


root = Tk()
root.title("Sudoku")

canvas = Canvas(root, width=1100,height=1200,bg='white')

pinkPolygon = canvas.create_polygon(100,200,1000,200,1000,1100,100,1100,fill = "thistle1",outline = "cornflower blue",width=10)


def create_grid(event = None):
    w = canvas.winfo_width() # Get current width of canvas
    h = canvas.winfo_height() 
    # Creates all vertical lines at intevals of 100
    for i in range(100, w-100, 100):
        canvas.create_line([(i, 200), (i, 1100)], tag='grid_line')
	for i in range(100,w-100,300):
            canvas.create_line([(i,200),(i,1100)],tag='grid_line',fill="cornflower blue" ,width=10)
    
# Creates all horizontal lines at intevals of 100
    for i in range(200, h-100, 100):
        canvas.create_line([(100, i), (1000, i)], tag='grid_line')
	for i in range(200,h-100,300):
	     canvas.create_line([(100,i),(1000,i)],tag='grid_line',fill="cornflower blue" ,width=10)

def callback():
    print "click!"
   
b = Button(root, text="1", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3, command=callback)
b.pack()
b.place(height=90,width=90,x=100,y=100)

b = Button(root, text="2", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3 ,command=callback)
b.pack()
b.place(height=90,width=90,x=200,y=100)

b = Button(root, text="3", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1", font="25",padx=3,pady=3,command=callback)
b.pack()
b.place(height=90,width=90,x=300,y=100)

b = Button(root, text="4", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3 ,command=callback)
b.pack()
b.place(height=90,width=90,x=400,y=100)

b = Button(root, text="5", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3,command=callback)
b.pack()
b.place(height=90,width=90,x=500,y=100)

b = Button(root, text="6", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3, command=callback)
b.pack()
b.place(height=90,width=90,x=600,y=100)

b = Button(root, text="7", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3,command=callback)
b.pack()
b.place(height=90,width=90,x=700,y=100)

b = Button(root, text="8", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3, command=callback)
b.pack()
b.place(height=90,width=90,x=800,y=100)

b = Button(root, text="9", bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",font="25",padx=3,pady=3 ,command=callback)
b.pack()
b.place(height=90,width=90,x=900,y=100)


#def __init__(self,image):

b = Button(root,bg="cornflower blue",fg="white",activebackground="grey",activeforeground="thistle1",padx=3,pady=3 ,text="Eraser",font="Times 20 bold",command=callback)
#p = PhotoImage(file="/home/araju/Desktop/sixth sem/miniproject/eraser.png")
#b.config(image=self.p)
#b.image=p
b.pack()
b.place(height=100,width=150,x=950,y=0)

#messagebox.showerror('Warning', 'wrong move') 
canvas.pack(expand=True)
canvas.bind('<Configure>', create_grid)
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print arr[i][j],
        print ('n')

def find_empty_location(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
 
# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
 
# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number.
def used_in_col(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
 
# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number
def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False
 
# Checks whether it will be legal to assign num to the given row,col
#  Returns a boolean which indicates whether it will be legal to assign
#  num to the given row,col location.
def check_location_is_safe(arr,row,col,num):
     
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)
 
# Takes a partially filled-in grid and attempts to assign values to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def solve_sudoku(arr):
     
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function    
    l=[0,0]
     
    # If there is no unassigned location, we are done    
    if(not find_empty_location(arr,l)):
        return True
     
    # Assigning list values to row and col that we got from the above Function 
    row=l[0]
    col=l[1]
     
    # consider digits 1 to 9
    for num in range(1,10):
         
        # if looks promising
        if(check_location_is_safe(arr,row,col,num)):
             
            # make tentative assignment
            arr[row][col]=num
 
            # return, if sucess, ya!
            if(solve_sudoku(arr)):
                return True
 
            # failure, unmake & try again
            arr[row][col] = 0
             
    # this triggers backtracking        
    return False
 
# Driver main function to test above functions
if __name__=="__main__":
     
    # creating a 2D array for the grid
    grid=[[0 for x in range(9)]for y in range(9)]
     
    # assigning values to the grid
    grid=[[0,0,0,9,0,0,2,0,0],
          [7,0,0,0,0,0,0,9,4],
          [0,0,0,3,0,2,0,0,1],
          [6,7,0,2,0,3,0,4,8],
          [0,0,5,7,0,8,1,0,0],
          [8,9,0,6,0,4,0,2,7],
          [9,0,0,4,0,6,0,0,0],
          [5,2,0,0,0,0,0,0,3],
          [0,0,8,0,0,1,0,0,0]]

     
    # if sucess print the grid
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print "No solution exists"

root.mainloop()
