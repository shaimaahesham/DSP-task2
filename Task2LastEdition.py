import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

xlist = []
ylist = []
x = []
y = []

def git_x_y_vals(file):
    lines = file.readlines()

    for i in range(len(lines)):
        if i + 3 < len(lines):
            values = lines[i + 3].decode('utf-8').strip().split(' ')
            if len(values) >= 2:  # Check if values list has at least two elements
                x.append(float(values[0]))
                y.append(float(values[1]))

    return x, y

def read_multi_files(file_paths):
    if file_paths:
        for file_path in file_paths:
                with open(file_path, 'rb') as file:
                    data = git_x_y_vals(file)
                    xlist.append(list(data[0]))
                    ylist.append(list(data[1]))

# Print the extracted x and y values
if len(xlist) > 0:
    x_vals_signal1 = xlist[0] 
    x_vals_signal2 = xlist[1][1001:]
    y_vals_signal1 = ylist[0]
    y_vals_signal2 = ylist[1][1001:]
    print(f"x_vals_signal1#{x_vals_signal1},\n x_vals_signal2{x_vals_signal2}")
    print(f"y_vals_signal1#{y_vals_signal1},\n y_vals_signal2{y_vals_signal2}")
    print(len(y_vals_signal1))
else:
        x_vals_signal1 = None 
        x_vals_signal2 = None 
        y_vals_signal1 = None 
        y_vals_signal2 = None
        
def add() :
    # Calculate the sum of y_vals_signal1 and y_vals_signal2
    sum = []
    for i in range(len(y_vals_signal1)):
        sum.append(y_vals_signal1[i] + y_vals_signal2[i])

    # Plot the graph
    plt.plot(x_vals_signal1, sum,label="after addition",color='m')
    plt.plot(x_vals_signal1, y_vals_signal1,label="Original",color='#00FF00')
    plt.legend()
    plt.title("Addition")
    plt.show()
print(y_vals_signal2)
# add()
def sub():
    # Calculate the sub of y_vals_signal1 and y_vals_signal2
    sub = []
    for i in range(len(y_vals_signal1)):
        sub.append(y_vals_signal2[i] - y_vals_signal1[i])

    # Plot the graph
    plt.plot(x_vals_signal1, sub ,label="after Subtraction ",color='m')
    plt.plot(x_vals_signal1, y_vals_signal1 ,label="Original",color='#00FF00')
    plt.title("Subtraction")
    plt.legend()
    plt.show()
# sub()

def multi():
    # Calculate the multi  y_vals of num
    multip = []
    num = float(input())
    for i in range(len(y_vals_signal1)):
        multip.append(np.multiply(y_vals_signal1[i], num))

    # Plot the graph
    plt.plot(x_vals_signal1, multip,label="After Multiplication",color='m')
    plt.plot(x_vals_signal1,y_vals_signal1,label="original",color='#00FF00')
    plt.legend()
    plt.title("Multiplication")
    plt.show()   

# multi()
def squared():
    squared_list = []
    for i in range(len(y_vals_signal1)):
        squared_list.append(np.square(y_vals_signal1[i]))

    # Plot the graph
    plt.plot(x_vals_signal1, squared_list,label="After square",color='m')
    plt.plot(x_vals_signal1,y_vals_signal1,label="original",color='#00FF00')
    plt.legend()
    plt.title("squared")
    plt.show()
# squared() 
def shift():
    # Calculate the multi  y_vals of num
    shifted = []
    shifted_ather_side=[]
    num = float(input())
    for i in range(len(x_vals_signal1)):
        shifted.append(np.add(x_vals_signal1[i], num))
        shifted_ather_side.append(np.add(x_vals_signal1[i], -num))
    # Plot the graph
    plt.plot(shifted, y_vals_signal1,label="shifted_line",color='#00FF00')
    plt.plot(x_vals_signal1, y_vals_signal1,label="original_line",marker="o",color='c')
    plt.plot(shifted_ather_side, y_vals_signal1,label="shifted_line",color='#00FF00')
    plt.title("before and after shifting ")
    plt.legend()
    plt.show()   

# shift()

def normalization():
    normList=[]
    upper=max(y_vals_signal1)
    lower=min(y_vals_signal1)
    print("choose  [0:1] or [-1:1] .")
    normalization_type=input("enter your choice:")
    if normalization_type=="[0:1]":
           print("[0:1]")
           normList=[(val - lower) / (upper - lower) for val in y_vals_signal1]
    else :
           print("[-1:1]")
           normList=[(((2*(val - lower)) / (upper - lower))-1 )for val in y_vals_signal1]
    

    # Plot the graph
    plt.subplot(1, 2, 2)
    plt.plot(x_vals_signal1, normList,label="normalized",marker="o",color='m')
    plt.title("Normalization ",color='m')
    plt.subplot(1, 2, 1)
    plt.plot(x_vals_signal1, y_vals_signal1,label="original",marker="o",color='#00FF00')
    plt.title("Original",color='#00FF00')
    plt.legend()
    plt.show()
  
# normalization()

def Accumulation():
    Accumulated_list=[]
    for i in range(len(x_vals_signal1)):
        Accumulated_list.append(np.cumsum(x_vals_signal1[i]))
    # Plot the graph
    plt.subplot(1, 2, 1)
    plt.title(" Accumulation",color='m')
    plt.plot(Accumulated_list, y_vals_signal1,label="Accumulated",color='#00FF00')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x_vals_signal1, y_vals_signal1,label="original",color='c')
    plt.legend()
    plt.show() 
# Accumulation()




# upload_button = tk.Button( text="Upload Signals",command=read_multi_files)
# if upload_button:
#     root = tk.Tk()
#     root.withdraw()
#     root.call('wm', 'attributes', '.', '-topmost', True)
#     files = filedialog.askopenfilename(multiple=True) 
#     var = root.tk.splitlist(files)
#     filePaths = []
#     for f in var:
#         filePaths.append(f)
#     filePaths

#     read_multi_files(filePaths)

# # create input fields
# add_button = tk.Button( text="Add",command=add)