import tkinter as tk

import matplotlib.pyplot as plt
import pandas as pd


def ex1(df):
    df.plot()  # cream graficul
    plt.savefig('grafic1.png')  # salvam graficul ca imagine
    plt.close()


def ex2(df):
    df.head(8).plot()  # cream graficul cu primele 8 inregistrari
    plt.savefig('grafic2.png')  # salvam graficul ca imagine
    plt.close()


def ex3(df):
    df.tail(16)[['Durata', 'Puls']].plot()  # cream graficul cu ultimele 16 inregistrari pentru coloanele Durata si Puls
    plt.savefig('grafic3.png')  # salvam graficul ca imagine
    plt.close()


def main():
    df = pd.read_csv("data.csv")  # citim datele din fisierul csv
    ex1(df)  # apelam functia ex1 pt a crea graficul 1
    ex2(df)  # apelam functia ex2 pt a crea graficul 2
    ex3(df)  # apelam functia ex3 pt a crea graficul 3
    root = tk.Tk()  # cream o fereastra
    root.title("Grafice")  # setam titlul ferestrei
    text1 = tk.Label(root, text="Grafic 1")  # cream un label pentru graficul 1
    text1.grid(row=0, column=0)  # plasam labelul in fereastra
    img1 = tk.PhotoImage(file="grafic1.png")  # cream o imagine pentru graficul 1
    label1 = tk.Label(root, image=img1)  # cream un label pentru imagine
    label1.grid(row=1, column=0)  # plasam labelul in fereastra
    text2 = tk.Label(root, text="Grafic 2")  # cream un label pentru graficul 2
    text2.grid(row=0, column=1)  # plasam labelul in fereastra
    img2 = tk.PhotoImage(file="grafic2.png")  # cream o imagine pentru graficul 2
    label2 = tk.Label(root, image=img2)  # cream un label pentru imagine
    label2.grid(row=1, column=1)  # plasam labelul in fereastra
    text3 = tk.Label(root, text="Grafic 3")  # cream un label pentru graficul 3
    text3.grid(row=0, column=2)  # plasam labelul in fereastra
    img3 = tk.PhotoImage(file="grafic3.png")  # cream o imagine pentru graficul 3
    label3 = tk.Label(root, image=img3)  # cream un label pentru imagine
    label3.grid(row=1, column=2)  # plasam labelul in fereastra
    root.mainloop()  # afisam fereastra


if __name__ == "__main__":
    main()
