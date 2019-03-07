# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:29:51 2018

@author: ap
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import seaborn as sns
from sklearn import linear_model,feature_selection,preprocessing
import statsmodels.formula.api as sm
from statsmodels.tools.eval_measures import mse
from statsmodels.tools.tools import add_constant
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#df = pd.read_csv('Data/sleep.csv')
Tk().withdraw() 
filename = askopenfilename()
#df = pd.read_csv('Data/states.csv')
df1 = pd.read_csv(filename)
#df1 = df.dropna()

root = tk.Tk()
root.title("Python GUI - Multiple Linear Regression Analysis")
root.geometry("650x650+10+10")
root.resizable(0,0)

scr = scrolledtext.ScrolledText(root, width=75, height=20, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

pd.set_option('display.max_columns', 500)

def create_window():
    window = tk.Toplevel(root)

#Correlation Between All Variables
def corrAll():
    #val1 = combo1.get()
    #values = [combo2.get(idx) for idx in combo2.curselection()]
    #val2 = ','.join(values)
    #scr.insert(tk.INSERT , val1 + ' , ' + val2)
    #ok_btn.configure(text = val2)
    scr.insert( tk.INSERT , "Correlation between All : ")
    scr.insert( tk.INSERT , '\n\n')
    scr.insert( tk.INSERT , df1.corr())
    scr.insert( tk.INSERT , '\n\n')

#Correlation Between Two Variables
def corr2():
    val1 = combo1.get()
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = '+'.join(values)
    #scr.insert(tk.INSERT , len(combo2.curselection()))# + ' , ' + val2)
    #ok_btn.configure(text = val2)
    #if(val2!=""):
    if( len(combo2.curselection())==1 ):
        scr.insert( tk.INSERT , "Correlation between " + val1 + " and " + val2 + " : ")
        scr.insert( tk.INSERT , '\n\n')
        scr.insert( tk.INSERT , np.corrcoef(df1[val1], df1[val2]))
        scr.insert( tk.INSERT , '\n\n')
    else:
        scr.insert( tk.INSERT , 'Alert!, select only one variable from Indepedent Variable list')
        scr.insert( tk.INSERT , '\n\n')

#Regression Model        
def RegAna():
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    if(val2!=""):
        scr.insert( tk.INSERT , "Regression between " + val1 + " ~ " + val2 + " : ")
        scr.insert( tk.INSERT , '\n\n')
        result = sm.OLS(df1[dep_var], add_constant(df1[ind_var]) ).fit()
        scr.insert( tk.INSERT , result.summary())
        scr.insert( tk.INSERT , '\n\n')
    else:
        scr.insert( tk.INSERT , 'Alert!, Select Indepedent Variable(s)')
        scr.insert( tk.INSERT , '\n\n')

#Residual Plot
def resPlot():
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    if(val2!=""):
        #scr.insert( tk.INSERT , "Regression between " + val1 + " ~ " + val2 + " : ")
        scr.insert( tk.INSERT , '\n\n')
        result = sm.OLS(df1[dep_var], add_constant(df1[ind_var]) ).fit()
        pred_val = result.fittedvalues.copy()
        true_val = df1[val1]
        residual = true_val - pred_val
        fig,ax = plt.subplots(1,1)
        ax.scatter(pred_val,residual)
        plt.title("Residual Plot - Residual V/S Fitted")
        plt.show()
        #scr.insert( tk.INSERT , residual)
        scr.insert( tk.INSERT , '\n\n')
    else:
        scr.insert( tk.INSERT , 'Alert!, Select Indepedent Variable(s)')
        scr.insert( tk.INSERT , '\n\n')

#Probability Plot
def probPlot():
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    if(val2!=""):
        #scr.insert( tk.INSERT , "Regression between " + val1 + " ~ " + val2 + " : ")
        scr.insert( tk.INSERT , '\n\n')
        result = sm.OLS(df1[dep_var], add_constant(df1[ind_var]) ).fit()
        pred_val = result.fittedvalues.copy()
        true_val = df1[val1]
        residual = true_val - pred_val
        fig,ax = plt.subplots(1,1)
        stats.probplot(residual, plot=ax, fit=True)
        plt.title("Probability Plot")
        plt.show()
        #scr.insert( tk.INSERT , residual)
        scr.insert( tk.INSERT , '\n\n')
    else:
        scr.insert( tk.INSERT , 'Alert!, Select Indepedent Variable(s)')
        scr.insert( tk.INSERT , '\n\n')

#Scatter Plot
def scatterPlot():
    val1 = combo1.get()
    dep_var = val1.split(" ")
    values = [combo2.get(idx) for idx in combo2.curselection()]
    val2 = ','.join(values)
    ind_var = val2.split(",")
    #val1 = combo1.get()
    #values = [combo2.get(idx) for idx in combo2.curselection()]
    #val2 = '+'.join(values)
    #scr.insert(tk.INSERT , len(combo2.curselection()))# + ' , ' + val2)
    #ok_btn.configure(text = val2)
    #if(val2!=""):
    if( len(combo2.curselection())> 0 and len(combo2.curselection()) < 4 ):
        scr.insert( tk.INSERT , '\n\n')
        #scr.insert( tk.INSERT , type(ind_var))
        ##fig, ax = plt.subplots(1, 1)
        ##ax.scatter(df1[val1],df1[val2])
        ##ax.set_xlabel(val1)
        ##ax.set_ylabel(val2)
        ##plt.title("Scatter Plot of " + val1 + " and " + val2)
        sns.pairplot(df1, x_vars=ind_var, y_vars=dep_var, size=7, aspect=0.7 , kind='reg')
        plt.show()
        scr.insert( tk.INSERT , '\n\n')
    else:
        scr.insert( tk.INSERT , 'Alert!, select maximum three variables from Indepedent Variable list')
        scr.insert( tk.INSERT , '\n\n')

# Combo Box - 1
lbl_sel1 = ttk.Label(root, text="Select Dependend Variable").grid(row=1,column=0)
ch1 = tk.StringVar()
combo1 = ttk.Combobox(root , width=12 , textvariable=ch1)
combo1.grid(row=1,column=1)
combo1['values'] = list(df1)[1:]
combo1.current(0)

# Combo Box - 2
lbl_sel2 = ttk.Label(root, text="Select Dependend Variable").grid(row=2,column=0)
ch2 = tk.StringVar()
#combo2 = ttk.Combobox(root , width=12 , textvariable=ch1)
combo2 = Listbox(root , width=15 , height=10 , selectmode = tk.MULTIPLE)
combo2.grid(row=2,column=1)
#combo2['values'] = list(df1)[1:]
for i in list(df1)[1:]:
    combo2.insert(tk.END,i)
#combo2.current(0)

corr2_btn = ttk.Button(root , text="Correlation between Two" , command = corr2)
corr2_btn.grid(row=3,column=0)

corrAll_btn = ttk.Button(root , text="Correlation between All" , command = corrAll)
corrAll_btn.grid(row=3,column=1)

reg_btn = ttk.Button(root , text="Regression" , command = RegAna)
reg_btn.grid(row=3,column=2)

scatter_btn = ttk.Button(root , text="Scatter Plot with Least Square Line (Max. Three Pairs)" , command = scatterPlot)
scatter_btn.grid(row=4,column=0)

resPlot_btn = ttk.Button(root , text="Residual Plot - Linearity & Equal Variance" , command = resPlot)
resPlot_btn.grid(row=4,column=1)

probPlot_btn = ttk.Button(root , text="Probability Plot" , command = probPlot)
probPlot_btn.grid(row=4,column=2)

root.mainloop()
