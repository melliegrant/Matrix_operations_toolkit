import math
import re
import sys
from tkinter import *
from tkinter import messagebox
import numpy as np

BG_COLOR = "#d0d8e7"
matrix1 = []
matrix2 = []


def initate_matrix(window, x, y, matrix):
    rows, columns = np.shape(matrix)
    for i in range(rows):
        for j in range(columns):
            Label(window, text=matrix[i, j], background=BG_COLOR).grid(row=i + x, column=j + y)


def transpose_window():
    window = Toplevel()
    window["bg"] = BG_COLOR
    rows, columns = np.shape(matrix1)
    initate_matrix(window, 1, 0, matrix1)
    Label(window, text="T", background=BG_COLOR).grid(row=0, column=columns)
    Label(window, text="=", background=BG_COLOR).grid(row=math.floor((rows + 1) / 2), column=columns + 1)

    temp = np.transpose(matrix1)

    initate_matrix(window, 1, columns + 2, temp)


def add_sub_window(sign):
    try:
        if sign == '+':
            result = matrix1 + matrix2
        else:
            result = matrix1 - matrix2
    except Exception as e:
        messagebox.showerror("Języki skryptowe", "Nie można wykonać działania na macierzy", icon=messagebox.ERROR)
    else:
        window = Toplevel()
        window["bg"] = BG_COLOR
        rows, columns = np.shape(matrix1)
        initate_matrix(window, 0, 0, matrix1)
        if sign == '+':
            Label(window, text="+", background=BG_COLOR).grid(row=math.floor(rows / 2), column=columns)
        else:
            Label(window, text="-", background=BG_COLOR).grid(row=math.floor(rows / 2), column=columns)
        initate_matrix(window, 0, columns + 1, matrix2)
        Label(window, text="=", background=BG_COLOR).grid(row=math.floor(rows / 2), column=2 * columns + 1)
        initate_matrix(window, 0, 2 * columns + 2, result)


def mult_window():
    try:
        result = matrix1.dot(matrix2)  # Materiały wykładowe, plik Np_05.py
    except Exception as e:
        messagebox.showerror("Języki skryptowe", "Nie można pomnożyć macierzy", icon=messagebox.ERROR)
    else:
        window = Toplevel()
        window["bg"] = BG_COLOR
        rows, columns = np.shape(matrix1)
        initate_matrix(window, 0, 0, matrix1)
        Label(window, text="-1", background=BG_COLOR).grid(row=0, column=columns)
        Label(window, text="=", background=BG_COLOR).grid(row=math.floor((rows + 1) / 2), column=columns + 1)
        initate_matrix(window, 0, 2 * columns + 2, result)


def det_window():
    try:
        result = np.linalg.det(matrix1)
    except Exception as e:
        messagebox.showerror("Języki skryptowe", "Nie można policzyć wyznacznika macierzy", icon=messagebox.ERROR)
    else:
        result = round(result, 2)
        window = Toplevel()
        window["bg"] = BG_COLOR
        rows, columns = np.shape(matrix1)
        Label(window, text="det", background=BG_COLOR).grid(row=math.floor(rows / 2), column=0)
        initate_matrix(window, 0, 1, matrix1)
        Label(window, text="=", background=BG_COLOR).grid(row=math.floor(rows / 2), column=columns + 1)
        Label(window, text=result, background=BG_COLOR).grid(row=math.floor(rows / 2), column=columns + 2)


def inv_window():
    try:
        result = np.linalg.inv(matrix1)  # Materiały wykładowe, plik Np_06.py
    except Exception as e:
        messagebox.showerror("Języki skryptowe", "Nie można wyznaczyć macierzy odwrotnej", icon=messagebox.ERROR)
    else:
        result = np.around(result, decimals=2)
        window = Toplevel()
        window["bg"] = BG_COLOR
        rows, columns = np.shape(matrix1)
        initate_matrix(window, 0, 0, matrix1)
        Label(window, text="=", background=BG_COLOR).grid(row=math.floor(rows / 2), column=columns + 1)
        initate_matrix(window, 0, columns + 2, result)


def rank_window():
    result = np.linalg.matrix_rank(matrix1)
    window = Toplevel()
    window["bg"] = BG_COLOR
    rows, columns = np.shape(matrix1)
    Label(window, text="R", background=BG_COLOR).grid(row=math.floor(rows / 2), column=0)
    initate_matrix(window, 0, 1, matrix1)
    Label(window, text="=", background=BG_COLOR).grid(row=math.floor(rows / 2), column=columns + 1)
    Label(window, text=result, background=BG_COLOR).grid(row=math.floor(rows / 2), column=columns + 2)


def main_window():
    root = Tk(className="Języki Skryptowe")
    root["bg"] = BG_COLOR
    root.geometry("670x400")
    root.eval("tk::PlaceWindow . center")

    frame = Frame()
    frame["bg"] = BG_COLOR
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    transpose_bt = Button(frame, text="Transponowanie macierzy", width=40, command=transpose_window)
    add_bt = Button(frame, text="Dodawanie macierzy", width=40, command=lambda: add_sub_window('+'))
    substract_bt = Button(frame, text="Odejmowanie macierzy", width=40, command=lambda: add_sub_window('-'))
    multiplication2_bt = Button(frame, text="Mnożenie macierzy", width=40, command=mult_window)
    det_bt = Button(frame, text="Wyznacznik macierzy", width=40, command=det_window)
    inv_bt = Button(frame, text="Macierz odwrotna", width=40, command=inv_window)
    rank_bt = Button(frame, text="Rząd Macierzy", width=40, command=rank_window)
    exit_bt = Button(frame, text="Wyjście", width=40, command=root.quit)

    transpose_bt.pack(pady=5)
    add_bt.pack(pady=5)
    substract_bt.pack(pady=5)
    multiplication2_bt.pack(pady=5)
    det_bt.pack(pady=5)
    inv_bt.pack(pady=5)
    rank_bt.pack(pady=5)
    exit_bt.pack(pady=5)

    root.mainloop()

def read_matrix(file):
    data = file.read()
    data = re.findall("(?:{[0-9,]+}[,\\s]*)+", data)
    data = [re.findall("(?:\\d[,\\s]*)+", tmp) for tmp in data]
    matrix1 = []
    matrix2 = []
    num_of_columns = 0
    for i in range(len(data[0])):
        matrix1.append([int(x) for x in data[0][i].split(',') if x.strip().isdigit()])
        if i == 0:
            num_of_columns = len(matrix1[0])
        else:
            if len(matrix1[i]) != num_of_columns:
                sys.exit("Nieprawidłowy format pierwszej macierzy")
    for i in range(len(data[1])):
        matrix2.append([int(x) for x in data[1][i].split(',') if x.strip().isdigit()])
        if i == 0:
            num_of_columns = len(matrix2[0])
        else:
            if len(matrix2[i]) != num_of_columns:
                sys.exit("Nieprawidłowy format drugiej macierzy")
    return np.array(matrix1), np.array(matrix2)


if __name__ == '__main__':
    file = open('matrix.txt', 'r')
    matrix1, matrix2 = read_matrix(file)
    file.close()
    main_window()