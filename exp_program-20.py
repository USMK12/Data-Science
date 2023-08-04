import numpy as np
from scipy import stats

def calculate_conversion_rate(conversions, visitors):
    return conversions / visitors

def ab_test_statistical_significance(conversions_A, visitors_A, conversions_B, visitors_B):
    # Calculate conversion rates for each design
    conversion_rate_A = calculate_conversion_rate(conversions_A, visitors_A)
    conversion_rate_B = calculate_conversion_rate(conversions_B, visitors_B)

    # Perform two-sample t-test
    t_statistic, p_value = stats.ttest_ind_from_stats(conversion_rate_A, np.sqrt(conversion_rate_A / visitors_A),
                                                     visitors_A, conversion_rate_B, np.sqrt(conversion_rate_B / visitors_B),
                                                     visitors_B)

    return p_value

def main():
    # Sample data for website design A and website design B
    conversions_A = 120
    visitors_A = 1000

    conversions_B = 150
    visitors_B = 1000

    # Perform statistical test
    p_value = ab_test_statistical_significance(conversions_A, visitors_A, conversions_B, visitors_B)

    # Define the significance level (alpha)
    alpha = 0.05

    # Compare the p-value with the significance level
    if p_value < alpha:
        print("There is a statistically significant difference in the mean conversion rates between website design A and website design B.")
    else:
        print("There is no statistically significant difference in the mean conversion rates between website design A and website design B.")

if __name__ == "__main__":
    main()
