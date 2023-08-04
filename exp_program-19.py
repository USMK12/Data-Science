import numpy as np
from scipy import stats

# Sample data for patients who received the new drug
new_drug_data = [10, 12, 8, 15, 11, 9, 13, 14, 10, 12]

# Sample data for patients who received the placebo
placebo_data = [5, 7, 4, 8, 6, 3, 7, 6, 4, 9]

# Calculate the mean and standard deviation for each group
mean_new_drug = np.mean(new_drug_data)
std_new_drug = np.std(new_drug_data, ddof=1)

mean_placebo = np.mean(placebo_data)
std_placebo = np.std(placebo_data, ddof=1)

# Calculate the sample size for each group
n_new_drug = len(new_drug_data)
n_placebo = len(placebo_data)

# Calculate the standard error of the mean for each group
se_new_drug = std_new_drug / np.sqrt(n_new_drug)
se_placebo = std_placebo / np.sqrt(n_placebo)

# Calculate the 95% confidence interval for the mean reduction in blood pressure
confidence_interval_new_drug = stats.t.interval(0.95, df=n_new_drug-1, loc=mean_new_drug, scale=se_new_drug)
confidence_interval_placebo = stats.t.interval(0.95, df=n_placebo-1, loc=mean_placebo, scale=se_placebo)

print("95% Confidence Interval for Mean Reduction in Blood Pressure (New Drug):", confidence_interval_new_drug)
print("95% Confidence Interval for Mean Reduction in Blood Pressure (Placebo):", confidence_interval_placebo)
