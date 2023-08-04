def calculate_age_frequency(ages):
    age_frequency = {}  # Dictionary to store the frequency of each age

    for age in ages:
        if age in age_frequency:
            age_frequency[age] += 1
        else:
            age_frequency[age] = 1

    return age_frequency

def main():
    # Replace this list with the actual ages of customers who made a purchase in the past month
    customer_ages = [25, 30, 40, 25, 35, 25, 40, 35, 30, 35]

    # Calculate the frequency distribution of ages
    age_distribution = calculate_age_frequency(customer_ages)

    # Display the frequency distribution
    print("Age\tFrequency")
    for age, frequency in age_distribution.items():
        print(f"{age}\t{frequency}")

if __name__ == "__main__":
    main()
