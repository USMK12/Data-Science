import pandas as pd
import numpy as np
from scipy import stats

def calculate_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_error = stats.sem(data)

    # Calculate the critical value (t-score) for the given confidence level
    t_critical = stats.t.ppf((1 + confidence) / 2, df=n-1)

    # Calculate the margin of error
    margin_of_error = t_critical * std_error

    # Calculate the confidence interval
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    return (lower_bound, upper_bound)

def main():
    # Replace this list with the actual sample data of ratings
    ratings_data = [4.5, 4.8, 4.2, 4.9, 4.6, 4.7, 4.3, 4.8, 4.4, 4.6]

    # Calculate the confidence interval for the true population mean rating
    confidence_interval = calculate_confidence_interval(ratings_data)

    print("Sample Mean Rating:", np.mean(ratings_data))
    print("95% Confidence Interval:", confidence_interval)

if __name__ == "__main__":
    main()
