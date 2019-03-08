"""
@author: Parag Moteria, Machine Learning Specialist & Consultant

email-id : paragmoteria@gmail.com
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import seaborn as sns
import statsmodels.formula.api as sm
from statsmodels.tools.tools import add_constant

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

Tk().withdraw()
filename = askopenfilename()
df1 = pd.read_csv(filename)

root = tk.Tk()
root.title("Python GUI - Multiple Linear Regression Analysis")
root.geometry("650x650+10+10")
root.resizable(0, 0)

scr = scrolledtext.ScrolledText(root, width=75, height=20, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

pd.set_option('display.max_columns', 500)


def create_window():
    window = tk.Toplevel(root)


def corrAll():
    '''
    Compute Correlation between all variables
    '''
    scr.insert(tk.INSERT, "Correlation between All : ")
    scr.insert(tk.INSERT, '\n\n')
    scr.insert(tk.INSERT, df1.corr())
    scr.insert(tk.INSERT, '\n\n')


def corr2():
    '''
    Compute Correlation between two variables
    '''
    val1 = combo1.get()
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = '+'.join(values)
    if(len(combo2.curselection()) == 1):
        scr.insert(tk.INSERT, "Correlation between " + val1 + " and " + val2 +
                   " : ")
        scr.insert(tk.INSERT, '\n\n')
        scr.insert(tk.INSERT, np.corrcoef(df1[val1], df1[val2]))
        scr.insert(tk.INSERT, '\n\n')
    else:
        scr.insert(tk.INSERT, 'Alert!, select only one Independent Variable')
        scr.insert(tk.INSERT, '\n\n')


def RegAna():
    '''
    Compute Multiple Regression Model
    User select one Depedended Varaible and one or more Independent Variable(s)
    '''
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    if(val2 != ""):
        scr.insert(tk.INSERT, "Regression between " + val1 + " ~ " + val2 +
                   " : ")
        scr.insert(tk.INSERT, '\n\n')
        result = sm.OLS(df1[dep_var], add_constant(df1[ind_var])).fit()
        scr.insert(tk.INSERT, result.summary())
        scr.insert(tk.INSERT, '\n\n')
    else:
        scr.insert(tk.INSERT, 'Alert!, Select Independent Variable(s)')
        scr.insert(tk.INSERT, '\n\n')


def resPlot():
    '''
    Draw Residual Plot
    '''
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    if(val2 != ""):
        scr.insert(tk.INSERT, '\n\n')
        result = sm.OLS(df1[dep_var], add_constant(df1[ind_var])).fit()
        pred_val = result.fittedvalues.copy()
        true_val = df1[val1]
        residual = true_val - pred_val
        fig, ax = plt.subplots(1, 1)
        ax.scatter(pred_val, residual)
        plt.title("Residual Plot - Residual V/S Fitted")
        plt.show()
        scr.insert(tk.INSERT, '\n\n')
    else:
        scr.insert(tk.INSERT, 'Alert!, Select Independent Variable(s)')
        scr.insert(tk.INSERT, '\n\n')


def probPlot():
    '''
    Draw Probability Plot
    '''
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    if(val2 != ""):
        scr.insert(tk.INSERT, '\n\n')
        result = sm.OLS(df1[dep_var], add_constant(df1[ind_var])).fit()
        pred_val = result.fittedvalues.copy()
        true_val = df1[val1]
        residual = true_val - pred_val
        fig, ax = plt.subplots(1, 1)
        stats.probplot(residual, plot=ax, fit=True)
        plt.title("Probability Plot")
        plt.show()
        scr.insert(tk.INSERT, '\n\n')
    else:
        scr.insert(tk.INSERT, 'Alert!, Select Independent Variable(s)')
        scr.insert(tk.INSERT, '\n\n')


def scatterPlot():
    '''
    Draw Scatter Plot
    '''
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    if(len(combo2.curselection()) > 0 and len(combo2.curselection()) < 4):
        scr.insert(tk.INSERT, '\n\n')
        sns.pairplot(df1, x_vars=ind_var, y_vars=dep_var, size=7, aspect=0.7,
                     kind='reg')
        plt.show()
        scr.insert(tk.INSERT, '\n\n')
    else:
        scr.insert(tk.INSERT, 'Alert!, Maximum Three Independent Variables')
        scr.insert(tk.INSERT, '\n\n')


# Combo Box - 1
lbl_sel1 = ttk.Label(root,
                     text="Select Dependend Variable").grid(row=1, column=0)
ch1 = tk.StringVar()
combo1 = ttk.Combobox(root, width=12, textvariable=ch1)
combo1.grid(row=1, column=1)
combo1['values'] = list(df1)[1:]
combo1.current(0)

# Combo Box - 2
lbl_sel2 = ttk.Label(root,
                     text="Select Dependend Variable").grid(row=2, column=0)
ch2 = tk.StringVar()
combo2 = Listbox(root, width=15, height=10, selectmode=tk.MULTIPLE)
combo2.grid(row=2, column=1)
for i in list(df1)[1:]:
    combo2.insert(tk.END, i)

corr2_btn = ttk.Button(root, text="Correlation between Two", command=corr2)
corr2_btn.grid(row=3, column=0)

corrAll_btn = ttk.Button(root, text="Correlation between All", command=corrAll)
corrAll_btn.grid(row=3, column=1)

reg_btn = ttk.Button(root, text="Regression", command=RegAna)
reg_btn.grid(row=3, column=2)

scatter_btn = ttk.Button(root, text="Scatter Plot (Max. Three Pairs)",
                         command=scatterPlot)
scatter_btn.grid(row=4, column=0)

resPlot_btn = ttk.Button(root, text="Residual Plot-Linearity & Equal Variance",
                         command=resPlot)
resPlot_btn.grid(row=4, column=1)

probPlot_btn = ttk.Button(root, text="Probability Plot", command=probPlot)
probPlot_btn.grid(row=4, column=2)

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.grid(row=5, column=0)

root.mainloop()
