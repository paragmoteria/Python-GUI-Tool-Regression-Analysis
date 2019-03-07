import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import io
import os
import pandas as pd
import numpy as np

win=tk.Tk()
win.title("Python GUI (Data Science) - Regression Model, k-Mean & Neural Network")
#win.geometry("550x550+10+10")
win.overrideredirect(False)
win.geometry("{0}x{1}+10+10".format(win.winfo_screenwidth()-100, win.winfo_screenheight()-100))
win.resizable(0,0)

#res_label = ttk.Label(win , text = "Result Text")
#res_label.grid(row=2,column=1)

scr = scrolledtext.ScrolledText(win, width=150, height=30, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Load Data
def readBtn():
    global df
    Tk().withdraw() 
    filename = askopenfilename()
    df = pd.read_csv(filename)
    scr.insert(tk.INSERT , '\n Data File ... \n\n')
    pd.set_option('display.max_columns', 500)
    df1 = df.drop(df.columns[0], axis=1)
    scr.insert(tk.INSERT , df1)

# is Missing Value?
def missValue():
    scr.insert( tk.INSERT , '\n\n Missing Value Anaysis ... \n\n')
    pd.set_option('display.max_columns', 500)
    buf = io.StringIO()
    df.info(buf=buf)
    s = buf.getvalue()
    scr.insert(tk.INSERT , s)

## Complete Case with Descriptive Statistics
def completeCase():
    scr.insert( tk.INSERT , '\n\n Complete Case only ... \n\n')
    df1 = df.drop(df.columns[0], axis=1)
    df1 = df1.dropna()
    path = os.getcwd() + "\\datasets\\completeCases.csv"
    df1.to_csv(path)
    scr.insert(tk.INSERT , df1.describe())

## Data Pre-Processing with Descriptive Statistics (using Median)
def cleanData():
    df1 = df.drop(df.columns[0], axis=1)
    df1.fillna(df1.median() , inplace=True)
    path = os.getcwd() + "\\datasets\\imputeMissingVal.csv"
    df1.to_csv(path)
    scr.insert( tk.INSERT , '\n\n Cleaning Data by Imputing Missing Value using Median ... \n\n')
    scr.insert(tk.INSERT , df1.describe())

## Explore Missing Value using Correlation
def summaryInfo():
    x = df.drop(df.columns[0], axis=1)
    x.fillna(1 , inplace=True)
    x[x!=1] = 0
    scr.insert( tk.INSERT , '\n\n Explore Missing Value using Correlation \n\n')
    scr.insert(tk.INSERT , x.corr())

## Multiple Regression Analysis
def regAna():
    from stat_study import create_window
    create_window()
    
read_btn = ttk.Button(win , text = "Read Data - CSV File" , command = readBtn)
read_btn.grid(row=1,column=0)

miss_btn = ttk.Button(win , text = "is Missing Value?" , command = missValue)
miss_btn.grid(row=3,column=0)

complete_btn = ttk.Button(win , text = "Complete Cases - Descriptive Statistics" , command = completeCase)
complete_btn.grid(row=1,column=1)

cleanStr_btn = ttk.Button(win , text = "Data Pre-Preparation - Impute Missing Value (Summary)" , command = cleanData)
cleanStr_btn.grid(row=3,column=1)

missVal_corr_btn = ttk.Button(win , text = "Explore Missing Value using Correlation" , command = summaryInfo)
missVal_corr_btn.grid(row=1,column=2)

exit_btn = ttk.Button(win , text = "Exit" , command=win.destroy)
exit_btn.grid(row=3,column=2)

reg_btn = ttk.Button(win , text = "Regression Model" , command = regAna)
reg_btn.grid(row=11,column=0,padx=50,pady=50)

#kmean_btn = ttk.Button(win , text = "Cluster Analysis - (k-Mean)" , command = regAna)
#kmean_btn.grid(row=11,column=1)

#neural_btn = ttk.Button(win , text = "Classification Model - (Neural Network)" , command = regAna)
#neural_btn.grid(row=11,column=2)

#scr = scrolledtext.ScrolledText(win, width=60, height=20, wrap=tk.WORD)
#scr.grid(column=0, columnspan=3)

win.mainloop()
