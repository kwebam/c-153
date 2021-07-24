from tkinter import *
import random

root = Tk()
root.title("3D_Arrays")
root.geometry("400x400")

label = Label(root)

array_3d = [[[1,2,3,4,5,6,7,8,9,10,11,12], ["Head","Tail"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]]]
print(array_3d[0][2][3])

def new_password():
    random_number_1 = random.randint(0, 11)
    random_number_2 = random.randint(0, 1)
    random_number_3 = random.randint(0, 19)
    
    letter_1 = str(array_3d[0][0][random_number_1])
    letter_2 = str(array_3d[0][1][random_number_2])
    letter_3 = str(array_3d[0][2][random_number_3])
    label["text"] = letter_1 + "" + letter_2 + "" + letter_3

btn = Button(root, text="New Password", command=new_password)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
root.mainloop()