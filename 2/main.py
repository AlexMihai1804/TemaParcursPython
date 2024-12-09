import tkinter as tk

import matplotlib.pyplot as plt
import pandas as pd


def ex1(df):
    df.plot()
    plt.savefig('grafic1.png')


def ex2(df):
    df.head(8).plot()
    plt.savefig('grafic2.png')


def ex3(df):
    df.tail(16)[['Durata', 'Puls']].plot()
    plt.savefig('grafic3.png')


def main():
    df = pd.read_csv("data.csv")
    ex1(df)
    ex2(df)
    ex3(df)
    root = tk.Tk()
    root.title("Grafice")
    text1 = tk.Label(root, text="Grafic 1")
    text1.grid(row=0, column=0)
    img1 = tk.PhotoImage(file="grafic1.png")
    label1 = tk.Label(root, image=img1)
    label1.grid(row=1, column=0)
    text2 = tk.Label(root, text="Grafic 2")
    text2.grid(row=0, column=1)
    img2 = tk.PhotoImage(file="grafic2.png")
    label2 = tk.Label(root, image=img2)
    label2.grid(row=1, column=1)
    text3 = tk.Label(root, text="Grafic 3")
    text3.grid(row=0, column=2)
    img3 = tk.PhotoImage(file="grafic3.png")
    label3 = tk.Label(root, image=img3)
    label3.grid(row=1, column=2)
    root.mainloop()


if __name__ == "__main__":
    main()
