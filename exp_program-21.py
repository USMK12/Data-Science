import math

def calculate_sample_size(confidence_level, precision, population_stddev=None):
    # Z-score for the given confidence level
    z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)

    # Sample size formula
    if population_stddev:
        sample_size = (z_score ** 2 * population_stddev ** 2) / precision ** 2
    else:
        sample_size = (z_score ** 2) / precision ** 2

    return math.ceil(sample_size)

def main():
    # Get user input for sample size, confidence level, and desired precision
    sample_size = int(input("Enter the sample size: "))
    confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
    precision = float(input("Enter the desired level of precision: "))

    # Validate input
    if confidence_level <= 0 or confidence_level >= 1:
        print("Error: Confidence level must be between 0 and 1.")
        return

    if precision <= 0:
        print("Error: Precision must be greater than 0.")
        return

    # Calculate the margin of error
    margin_of_error = (precision / 2) * 100

    # Calculate the required sample size with a 95% confidence level
    required_sample_size = calculate_sample_size(confidence_level, precision)

    print(f"Margin of Error: {margin_of_error:.2f}%")
    print(f"Required Sample Size (at {confidence_level:.0%} confidence level and {precision:.2f} precision): {required_sample_size}")

if __name__ == "__main__":
    main()
