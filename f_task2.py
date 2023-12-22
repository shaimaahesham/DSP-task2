import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
import customtkinter
import numpy as np
customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("700x500")

def git_x_y_vals():
    data1 = []
    x = []
    y = []
    filepath = filedialog.askopenfilename()
    file1 = open(filepath,'r')
    line1 = file1.readline()
    line2 = file1.readline()
    line3 = file1.readline()
    line3 = int(line3)
    while line3 > 0:
        line = file1.readline()
        line3 = line3 - 1
        data1.append(line)
    
    file1.close()
    x = []
    y = []
    for i in data1:
        w = i.split()
        x.append(int(w[0]))
        y.append(float(w[1]))
    return x,y


        
def add() :
    x1=[]
    y1=[]
    x1,y1=git_x_y_vals()
    x2=[]
    y2=[]
    x2,y2=git_x_y_vals()
    # Calculate the sum of y_vals_signal1 and y_vals_signal2
    sum = []
    for i in range(len(y1)):
        sum.append(y1[i] + y2[i])
    plt.subplot(1, 3, 1)
    plt.plot(x1, sum ,label="after Addition ",color='m')
    plt.legend()
    plt.subplot(1, 3, 2)
    plt.plot(x1, y1 ,label="Original_file[1]",color='#00FF00')
    plt.legend()
    plt.subplot(1, 3, 3)
    plt.plot(x2, y2 ,label="Original_file[2]",color='#00FF00')
    plt.legend()
    plt.show()

# add()
def sub():
    x1=[]
    y1=[]
    x1,y1=git_x_y_vals()
    x2=[]
    y2=[]
    x2,y2=git_x_y_vals()
    # Calculate the sub of y_vals_signal1 and y_vals_signal2
    sub = []
    for i in range(len(y1)):
        sub.append(y1[i] - y2[i])

    # Plot the graph
    # subplot(nrows, ncols, index)
    plt.subplot(1, 3, 1)
    plt.plot(x1, sub ,label="after Subtraction ",color='m')
    plt.legend()
    plt.subplot(1, 3, 2)
    plt.plot(x1, y1 ,label="Original_file[1]",color='#00FF00')
    plt.legend()
    plt.subplot(1, 3, 3)
    plt.plot(x2, y2 ,label="Original_file[2]",color='#00FF00')
    plt.legend()
    plt.show()
# sub()

def multi():
    x=[]
    y=[]
    x,y=git_x_y_vals()
    # Calculate the multi  y_vals of num
    multip = []
    num = float(input())
    for i in range(len(y)):
        multip.append(np.multiply(y[i], num))

    # Plot the graph
    plt.plot(x, multip,label="After Multiplication",color='m')
    plt.plot(x,y,label="original",color='#00FF00')
    plt.legend()
    plt.title("Multiplication")
    plt.show()   

# multi()
def squared():
    x=[]
    y=[]
    x,y=git_x_y_vals()
    squared_list = []
    for i in range(len(y)):
        squared_list.append(np.square(y[i]))

    # Plot the graph
    plt.plot(x, squared_list,label="After square",color='m')
    plt.plot(x,y,label="original",color='#00FF00')
    plt.legend()
    plt.title("squared")
    plt.show()
# squared() 
def shift():
    x=[]
    y=[]
    x,y=git_x_y_vals()
    shifted = []
    shifted_ather_side=[]
    num = float(input())
    for i in range(len(x)):
        shifted.append(np.add(x[i], num))
        shifted_ather_side.append(np.add(x[i], -num))
    # Plot the graph
    plt.plot(shifted, y,label="shifted_line",color='#00FF00')
    plt.plot(x, y,label="original_line",marker="o",color='c')
    plt.plot(shifted_ather_side, y,label="shifted_line",color='#00FF00')
    plt.title("before and after shifting ")
    plt.legend()
    plt.grid(True)
    plt.show()   

# shift()

def normalization():
    x=[]
    y=[]
    x,y=git_x_y_vals()
    normList=[]
    upper=max(y)
    lower=min(y)
    print("choose  [0:1] or [-1:1] .")
    normalization_type=input("enter your choice:")
    if normalization_type=="[0:1]":
           print("[0:1]")
           normList=[(val - lower) / (upper - lower) for val in y]
    else :
           print("[-1:1]")
           normList=[(((2*(val - lower)) / (upper - lower))-1 )for val in y]
    

    # Plot the graph
    plt.subplot(1, 2, 2)
    plt.plot(x, normList,label="normalized",marker="o",color='m')
    plt.title("Normalization ",color='m')
    plt.legend()
    plt.subplot(1, 2, 1)
    plt.plot(x, y,label="original",marker="o",color='#00FF00')
    plt.title("Original",color='#00FF00')
    plt.legend()
    plt.show()
  
# normalization()

def Accumulation():
    x=[]
    y=[]
    x,y=git_x_y_vals()
    Accumulated_list=[]
    for i in range(len(x)):
        Accumulated_list.append(np.cumsum(x[i]))
    # Plot the graph
    plt.subplot(1, 2, 1)
    plt.title(" Accumulation",color='m')
    plt.plot(Accumulated_list, y,label="Accumulated",marker="o",color='#00FF00')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, y,label="original",marker="o",color='c')
    plt.legend()
    plt.show() 
# Accumulation()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=50, padx=60, fill="both", expand=True)


button_add = customtkinter.CTkButton(master=frame , text="Addition", command=add)
button_add.pack(pady=12, padx=10)

button_Shift = customtkinter.CTkButton(master=frame , text="Subtraction", command=sub)
button_Shift.pack(pady=12, padx=10)

button_normalization = customtkinter.CTkButton(master=frame , text="Multiplication", command=multi)
button_normalization.pack(pady=12, padx=10)

button_accumulation = customtkinter.CTkButton(master=frame , text="Squaring", command=squared)
button_accumulation.pack(pady=12, padx=10)

button_squaring = customtkinter.CTkButton(master=frame , text="Shifting", command=shift)
button_squaring.pack(pady=12, padx=10)

button_Subtraction = customtkinter.CTkButton(master=frame , text="Normalization", command=normalization)
button_Subtraction.pack(pady=12, padx=10)

button_Multiplication = customtkinter.CTkButton(master=frame , text="Accumulation", command=Accumulation)
button_Multiplication.pack(pady=12, padx=10)
root.mainloop()

