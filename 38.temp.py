import csv
import statistics

def calculate_mean_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

def calculate_standard_deviation(temperatures):
    return statistics.stdev(temperatures)

def calculate_temperature_range(temperatures):
    return max(temperatures) - min(temperatures)

def read_temperature_data(file_path):
    data = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = row['City']
            temperature = float(row['Temperature'])
            if city not in data:
                data[city] = []
            data[city].append(temperature)
    return data

def find_city_with_lowest_standard_deviation(data):
    min_std_dev = float('inf')
    most_consistent_city = None
    for city, temperatures in data.items():
        std_dev = calculate_standard_deviation(temperatures)
        if std_dev < min_std_dev:
            min_std_dev = std_dev
            most_consistent_city = city
    return most_consistent_city

def main():
    file_path = 'path/to/your/dataset.csv'
    data = read_temperature_data(file_path)

    # Task 1: Calculate the mean temperature for each city.
    mean_temperatures = {city: calculate_mean_temperature(temperatures) for city, temperatures in data.items()}

    # Task 2: Calculate the standard deviation of temperature for each city.
    std_deviations = {city: calculate_standard_deviation(temperatures) for city, temperatures in data.items()}

    # Task 3: Determine the city with the highest temperature range.
    city_with_highest_range = max(data, key=lambda city: calculate_temperature_range(data[city]))

    # Task 4: Find the city with the most consistent temperature (the lowest standard deviation).
    most_consistent_city = find_city_with_lowest_standard_deviation(data)

    print("Mean temperatures:")
    print(mean_temperatures)

    print("\nStandard deviations:")
    print(std_deviations)

    print("\nCity with the highest temperature range:", city_with_highest_range)

    print("\nCity with the most consistent temperature (lowest standard deviation):", most_consistent_city)

if __name__ == "__main__":
    main()
