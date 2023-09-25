import tkinter as tk
from tkinter import filedialog
import pandas as pd

def wybierz_plik_1():
    global plik1
    plik1 = filedialog.askopenfilename(filetypes=[("Pliki CSV", "*.csv")])
    label_plik_1.config(text=plik1)

def wybierz_plik_2():
    global plik2
    plik2 = filedialog.askopenfilename(filetypes=[("Pliki CSV", "*.csv")])
    label_plik_2.config(text=plik2)

def scal_pliki():
    if plik1 and plik2:
        df1 = pd.read_csv(plik1)
        df2 = pd.read_csv(plik2)
        df = pd.concat([df1, df2], ignore_index=True)
        df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
        df.drop_duplicates(subset=['language','source_text'], inplace=True)

        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        label_scal.config(text=save_path)
        df.to_csv(save_path, index=False)

root = tk.Tk()
root.geometry('300x300')
root.title("Scalanie plików CSV")

button_plik_1 = tk.Button(root, text="Wybierz plik 1", command=wybierz_plik_1)
button_plik_2 = tk.Button(root, text="Wybierz plik 2", command=wybierz_plik_2)
button_scal = tk.Button(root, text="Scal", command=scal_pliki)
label_plik_1 = tk.Label(root, text="")
label_plik_2 = tk.Label(root, text="")
label_scal = tk.Label(root, text="")

button_plik_1.pack()
label_plik_1.pack()
button_plik_2.pack()
label_plik_2.pack()
button_scal.pack()
label_scal.pack()

root.mainloop()
