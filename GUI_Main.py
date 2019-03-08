"""
@author: Parag Moteria, Machine Learning Consultant

email-id : paragmoteria@gmail.com
"""

import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import io
import os
import pandas as pd

win = tk.Tk()
win.title("Python GUI (Data Science) - Regression Model")
win.overrideredirect(False)
win.geometry("{0}x{1}+10+10".format(win.winfo_screenwidth() - 100,
             win.winfo_screenheight()-100))
win.resizable(0, 0)
scr = scrolledtext.ScrolledText(win, width=150, height=30, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)


def readBtn():
    '''
    Read data csv file
    '''
    global df
    Tk().withdraw()
    filename = askopenfilename()
    df = pd.read_csv(filename)
    scr.insert(tk.INSERT, '\n Data File ... \n\n')
    pd.set_option('display.max_columns', 500)
    df1 = df.drop(df.columns[0], axis=1)
    scr.insert(tk.INSERT, df1)


def missValue():
    '''
    Identify Missing Values
    '''
    scr.insert(tk.INSERT, '\n\n Missing Value Anaysis ... \n\n')
    pd.set_option('display.max_columns', 500)
    buf = io.StringIO()
    df.info(buf=buf)
    s = buf.getvalue()
    scr.insert(tk.INSERT, s)


def completeCase():
    '''
    It is not always feasible.
    Drop missing values
    '''
    scr.insert(tk.INSERT, '\n\n Complete Case only ... \n\n')
    df1 = df.drop(df.columns[0], axis=1)
    df1 = df1.dropna()
    if not os.path.isdir("imputedData"):
        os.mkdir("imputedData")
    path = os.getcwd() + "\\imputedData\\completeCases.csv"
    df1.to_csv(path)
    scr.insert(tk.INSERT, df1.describe())


def cleanData():
    '''
    Data Pre-Processing with Descriptive Statistics (using Median)
    It is suitable for numeric data
    '''
    df1 = df.drop(df.columns[0], axis=1)
    df1.fillna(df1.median(), inplace=True)
    if not os.path.isdir("imputedData"):
        os.mkdir("imputedData")
    path = os.getcwd() + "\\imputedData\\imputeMissingVal.csv"
    df1.to_csv(path)
    scr.insert(tk.INSERT, '\n\n Cleaning Data by Imputing Missing Value \
               using Median ... \n\n')
    scr.insert(tk.INSERT, df1.describe())


def summaryInfo():
    '''
    Explore Missing Value using Correlation
    '''
    x = df.drop(df.columns[0], axis=1)
    x.fillna(1, inplace=True)
    x[x != 1] = 0
    scr.insert(tk.INSERT, '\n\n Explore Missing Value using Correlation \n\n')
    scr.insert(tk.INSERT, x.corr())


def regAna():
    '''
    Multiple Regression Analysis
    '''
    from stat_study import create_window
    create_window()


read_btn = ttk.Button(win, text="Read Data - CSV File", command=readBtn)
read_btn.grid(row=1, column=0)

miss_btn = ttk.Button(win, text="is Missing Value?", command=missValue)
miss_btn.grid(row=3, column=0)

complete_btn = ttk.Button(win, text="Complete Cases - Descriptive Statistics",
                          command=completeCase)
complete_btn.grid(row=1, column=1)

cleanStr_btn = ttk.Button(win, text="Data Pre-Preparation - Impute Missing",
                          command=cleanData)
cleanStr_btn.grid(row=3, column=1)

missVal_corr_btn = ttk.Button(win, text="Missing Value using Correlation",
                              command=summaryInfo)
missVal_corr_btn.grid(row=1, column=2)

exit_btn = ttk.Button(win, text="Exit", command=win.destroy)
exit_btn.grid(row=3, column=2)

reg_btn = ttk.Button(win, text="Regression Model", command=regAna)
reg_btn.grid(row=11, column=0, padx=50, pady=50)

win.mainloop()
