import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from itertools import accumulate

xlist = []
ylist = []
x = []
y = []


def read_files():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        for file_path in file_paths:
            #  i = 0
            file = open(file_path, 'r')
            lines = file.readlines()
            for l in lines:
                tmp = l.split(" ")
                x.append(float(tmp[0]))
                y.append(float(tmp[1].replace("\n", " ")))

            xlist.append(list(x))
            ylist.append(list(y))

            x.clear()
            y.clear()
    print(ylist)


def addition_signals():
    res = []
    #  Y=[1,2,3,4,5]
    res.append(np.add(ylist[0], ylist[1]))

    print("result", res)
    print(len(res[0]))
    print(len(ylist[0]))
    print(len(xlist[0]))

    plt.subplot(2, 2, 1)
    plt.plot(xlist[0], ylist[0])

    plt.subplot(2, 2, 2)
    plt.plot(xlist[0], ylist[1])

    # plt.plot(xlist[0],res[0])
    plt.subplot(2, 2, 3)
    plt.plot(xlist[0], res[0])

    plt.show()


def subtraction_signals():
    res = []
    #  Y=[1,2,3,4,5]
    res.append(np.absolute(np.subtract(ylist[0], ylist[1])))

    #  print("result",res)
    #  print(len(res[0]))
    #  print(len(ylist[0]))
    #  print(len(xlist[0]))

    plt.subplot(2, 2, 1)
    plt.plot(xlist[0], ylist[0])

    plt.subplot(2, 2, 2)
    plt.plot(xlist[0], ylist[1])

    #  plt.subplot(1,2,3)
    #  plt.plot(xlist[0],res[0])

    plt.subplot(2, 2, 3)
    plt.plot(xlist[0], res[0])

    plt.show()


def multiply():
    res = []
    scaler = float(muliply_entry.get())
    res.append(np.multiply(ylist[0], scaler))

    # print(res[0])

    plt.subplot(2, 2, 1)
    plt.plot(xlist[0], ylist[0])

    plt.subplot(2 , 2 ,2)
    plt.plot(xlist[0], res[0])
    plt.title("Multiplication")

    plt.show()


def squared():
    res = []
    res.append(np.square(ylist[0]))
    print(res[0])

    plt.subplot(1, 2, 1)
    plt.plot(xlist[0], ylist[0])

    plt.subplot(1, 2, 2)
    plt.plot(xlist[0], res[0])
    plt.title("Squared")

    plt.show()


def shifting():
    res = []
    shift_val = float(shifiting_entry.get())
    res.append(np.add(xlist[0], shift_val))
    print(res[0])

    plt.subplot(1, 2, 1)
    plt.plot(xlist[0], ylist[0])
    plt.title("Original")

    plt.subplot(1, 2, 2)
    plt.plot(res[0], ylist[0])
    plt.title("Shifting")

    plt.show()


def normalization_signal():

    norm_option = normalization_var.get()

    if norm_option == 1:  # Normalize to [0, 1]
        min_val = min(ylist[0])
        max_val = max(ylist[0])
        res = [(val - min_val) / (max_val - min_val) for val in ylist[0]]
    else:  # Normalize to [-1, 1]
        min_val = min(ylist[0])
        max_val = max(ylist[0])
        res = [(2 * (val - min_val) / (max_val - min_val) - 1) for val in ylist[0]]

    plt.subplot(1, 2, 1)
    plt.plot(xlist[0], ylist[0])
    plt.title("Original Signal")

    plt.subplot(1, 2, 2)
    plt.plot(xlist[0], res)
    if norm_option == 1:
        plt.title("Normalization [0, 1] Result")
    else:
        plt.title("Normalization [-1, 1] Result")

    plt.show()


def Accumulation():
    res = []
    res.append(np.cumsum(ylist[0]))
    plt.subplot(1, 2, 1)
    plt.plot(xlist[0], ylist[0])
    plt.title("Original Signal")

    plt.subplot(1, 2, 2)
    plt.plot(xlist[0], res[0])
    plt.title("Accumulation Result")

    plt.show()
    print(res[0])


# def gui():
root = tk.Tk()
# Create and configure the frame
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

upload_button = ttk.Button(frame, text="Upload Signals", command=read_files)
upload_button.grid(row=0, column=1)
# create input fields
add_button = ttk.Button(frame, text="Add", command=addition_signals)
add_button.grid(row=1, column=1)

subtraction_button = ttk.Button(
    root, text="subtract", command=subtraction_signals)
subtraction_button.grid(row=2, column=1)

label_muliply = ttk.Label(frame, text="multiply:")
label_muliply.grid(row=3, column=0)
muliply_entry = ttk.Entry(frame, width=10)
muliply_entry.grid(row=3, column=1)

muliply_button = ttk.Button(frame, text="muliply", command=multiply)
muliply_button.grid(row=4, column=1)

square_button = ttk.Button(frame, text="Squaring", command=squared)
square_button.grid(row=5, column=1)

label_shifiting = ttk.Label(frame, text="Shifting:")
label_shifiting.grid(row=6, column=0)

shifiting_entry = ttk.Entry(frame, width=10)
shifiting_entry.grid(row=6, column=1)

shifiting_button = ttk.Button(frame, text="Shifting", command=shifting)
shifiting_button.grid(row=7, column=0)

ACCumelation_button = ttk.Button(
    frame, text="Acummelation", command=Accumulation)
ACCumelation_button.grid(row=8, column=0)


normalization_label = ttk.Label(frame, text="Normalization:")
normalization_label.grid(row=9, column=0)

normalization_var = tk.IntVar()
normalization_var.set(1)  # Default to [0, 1] normalization

normalization_option1 = ttk.Radiobutton(
    frame, text="0 to 1", variable=normalization_var, value=1)
normalization_option1.grid(row=9, column=1)

normalization_option2 = ttk.Radiobutton(
    frame, text="-1 to 1", variable=normalization_var, value=2)
normalization_option2.grid(row=9, column=2)

normalization_button = ttk.Button(
    frame, text="normalization", command=normalization_signal)
normalization_button.grid(row=10, column=0)

root.mainloop()