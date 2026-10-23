##################################################
#
# This file contains helper functions for accessing
# excel files through xlwings in a simple way
#
##################################################


import xlwings as xw
import numpy as np
import pandas as pd
from scipy.stats import triang
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import datetime
import time
import os
import shutil


def sample_triangular_distribution(lower: float, upper: float, mode: float, size: int = 1) -> np.ndarray:
    if not (lower <= mode <= upper):
        raise ValueError("Mode must be between lower and upper bounds.")

    # Compute the shape parameter c
    c = (mode - lower) / (upper - lower)

    # Generate random samples
    samples = triang.rvs(c, loc=lower, scale=(upper - lower), size=size)

    samples = np.round(samples, 4)
    
    return samples

def plot_distribution(sample):
    plt.hist(samples, bins=100, color='blue', edgecolor='black', alpha=0.7)
    
    # Labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Distribution PLot')
    
    # Show the plot
    plt.show()


# returns number of row in active excel sheet containing that variable name
def get_row_by_variable(var, sheet, num_rows):
    for row in range(1, num_rows + 1): 
        if sheet.range((row, 1)).value == var:
            return row
    return -1

# inserts new row with variable name and returns new row numbers
def insert_row_after(row, name, sheet, num_rows):
    existing_row = get_row_by_variable(name, sheet, num_rows)
    if (existing_row != -1):
        raise Exception("Sorry, row with name " + name + " already exists!")
    sheet.range(f"{row+1}:{row+1}").insert(shift="down")
    sheet.range((row + 1, 1)).value = name
    return row + 1



# returns mean and variance for each methodology in a list
# 1. AMS_IIIR, 2. GSTPDDTEC, 3. AMS_IE
#def extract_mean_and_variance(var, sheet, num_rows, num_columns, num_header_columns):
#    row_is_AMS_IIIR = get_row_by_variable("AMS-III.R", sheet, num_rows)
#    row_is_GSTPDDTEC = get_row_by_variable("GS TPDDTEC", sheet, num_rows)
#    row_is_AMS_IE = get_row_by_variable("AMS-I.E", sheet, num_rows)
#    row_var = get_row_by_variable(var, sheet, num_rows)
#
#    row_data_missing = get_row_by_variable("data_missing", sheet, num_rows)
#
#    # get variable that we want to measure
#    values = np.array(sheet.range((row_var, num_header_columns + 1), (row_var, num_columns)).value)
#
#    # get selection of methodology
#    is_AMS_IIIR = np.array(sheet.range((row_is_AMS_IIIR, num_header_columns + 1), (row_is_AMS_IIIR, num_columns)).value)
#    is_GSTPDDTEC = np.array(sheet.range((row_is_GSTPDDTEC, num_header_columns + 1), (row_is_GSTPDDTEC, num_columns)).value)
#    is_AMS_IE = np.array(sheet.range((row_is_AMS_IE, num_header_columns + 1), (row_is_AMS_IE, num_columns)).value)
#
#    # ignore projects with missing data
#    has_data_missing =  np.array(sheet.range((row_data_missing, num_header_columns + 1), (row_data_missing, num_columns)).value)
#    values = values[has_data_missing == 0]
#    is_AMS_IIIR = is_AMS_IIIR[has_data_missing == 0]
#    is_GSTPDDTEC = is_GSTPDDTEC[has_data_missing == 0]
#    is_AMS_IE = is_AMS_IE[has_data_missing == 0]
#    
#    # Extract values where methodology is 1
#    values_AMS_IIIR = values[is_AMS_IIIR == 1]
#    values_GSTPDDTEC = values[is_GSTPDDTEC == 1]
#    values_AMS_IE = values[is_AMS_IE == 1]
#    
#    # Compute mean and variance
#    return [(
#        np.mean(values_AMS_IIIR),
#        np.var(values_AMS_IIIR)
#    ), (        
#        np.mean(values_GSTPDDTEC),
#        np.var(values_GSTPDDTEC)
#    ), (
#        np.mean(values_AMS_IE),
#        np.var(values_AMS_IE)
#    )]


# This functions takes the output of extract_mean_and_variance() and plots it
def plot_methodologies(means_and_variances, title = "Monte Carlo Simulation Results"):
    # Given means and variances from Monte Carlo simulation
    variables = ["AMS III.R", "GSTPDDTEC", "AMS I.E"]
    means = [means_and_variances[0][0], means_and_variances[1][0], means_and_variances[2][0]]
    variances = [means_and_variances[0][1], means_and_variances[1][1], means_and_variances[2][1]]
    
    # Compute standard deviation (sqrt of variance)
    std_devs = np.sqrt(variances) * 1.96
    
    # X positions for the categorical variables
    x_positions = np.arange(len(variables))

    fig, ax = plt.subplots()
    ax.errorbar(x_positions, means, yerr=std_devs, fmt='o', capsize=5, capthick=1, color='darkblue', label='Mean ± 95% CI')

    ax.set_ylim(bottom=0)  # y-axis starts at 0
    ax.set_xlim(-0.5, len(variables) - 0.5)
    
    # Customize the plot
    #ax.set_xticks(x_positions, variables)  # Set categorical labels
    ax.set_xticks(x_positions)
    ax.set_xticklabels(variables)
    ax.set_ylabel("Factor")
    ax.set_title(title)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Green background between y=0 and y=1
    ax.axhspan(0, 1, facecolor='green', alpha=0.1)
    
    # Red background above y=1
    ax.axhspan(1, ax.get_ylim()[1], facecolor='red', alpha=0.2)
    
    plt.show()



def get_mean_and_variance(var_factor, var_variance, sheet, num_rows, num_columns, num_header_columns):
    row_is_AMS_IIIR = get_row_by_variable("AMS-III.R", sheet, num_rows)
    row_is_GSTPDDTEC = get_row_by_variable("GS TPDDTEC", sheet, num_rows)
    row_is_AMS_IE = get_row_by_variable("AMS-I.E", sheet, num_rows)
    row_ER_mc_functionality_factor = get_row_by_variable(var_factor, sheet, num_rows)
    row_ER_mc_functionality_factor_variance = get_row_by_variable(var_variance, sheet, num_rows)

    row_data_missing = get_row_by_variable("data_missing", sheet, num_rows)

    # get variable that we want to measure
    means = np.array(sheet.range((row_ER_mc_functionality_factor, num_header_columns + 1), (row_ER_mc_functionality_factor, num_columns)).value)
    variances = np.array(sheet.range((row_ER_mc_functionality_factor_variance, num_header_columns + 1), (row_ER_mc_functionality_factor_variance, num_columns)).value)

    # get selection of methodology
    is_AMS_IIIR = np.array(sheet.range((row_is_AMS_IIIR, num_header_columns + 1), (row_is_AMS_IIIR, num_columns)).value)
    is_GSTPDDTEC = np.array(sheet.range((row_is_GSTPDDTEC, num_header_columns + 1), (row_is_GSTPDDTEC, num_columns)).value)
    is_AMS_IE = np.array(sheet.range((row_is_AMS_IE, num_header_columns + 1), (row_is_AMS_IE, num_columns)).value)

    # ignore projects with missing data
    has_data_missing =  np.array(sheet.range((row_data_missing, num_header_columns + 1), (row_data_missing, num_columns)).value)
    means = means[has_data_missing == 0]
    variances = variances[has_data_missing == 0]
    
    is_AMS_IIIR = is_AMS_IIIR[has_data_missing == 0]
    is_GSTPDDTEC = is_GSTPDDTEC[has_data_missing == 0]
    is_AMS_IE = is_AMS_IE[has_data_missing == 0]
    
    # Extract means where methodology is 1
    means_AMS_IIIR = means[is_AMS_IIIR == 1]
    means_GSTPDDTEC = means[is_GSTPDDTEC == 1]
    means_AMS_IE = means[is_AMS_IE == 1]
    
    # Extract variances where methodology is 1
    variances_AMS_IIIR = variances[is_AMS_IIIR == 1]
    variances_GSTPDDTEC = variances[is_GSTPDDTEC == 1]
    variances_AMS_IE = variances[is_AMS_IE == 1]
    
    # Compute mean and variance
    return [(
        np.mean(means_AMS_IIIR),
        np.mean(variances_AMS_IIIR)
    ), (        
        np.mean(means_GSTPDDTEC),
        np.mean(variances_GSTPDDTEC)
    ), (
        np.mean(means_AMS_IE),
        np.mean(variances_AMS_IE)
    )]

def sample_from_discrete_distribution(arr, n):
    if len(arr) == 0:
        raise ValueError("Input array must not be empty.")
    return np.random.choice(arr, size=n, replace=True)