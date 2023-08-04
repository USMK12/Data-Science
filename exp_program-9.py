import pandas as pd

# Sample data for demonstration
data = {
    'location': ['Location_A', 'Location_B', 'Location_A', 'Location_C', 'Location_B', 'Location_C', 'Location_A'],
    'listing_price': [500000, 700000, 600000, 800000, 750000, 900000, 550000],
    'bedrooms': [3, 4, 3, 5, 6, 4, 5],
    'area': [1200, 1500, 1300, 1800, 2000, 1600, 1400]
}

# Creating the DataFrame from the sample data
property_data = pd.DataFrame(data)

def main():
    # 1. Average listing price of properties in each location
    average_listing_price = property_data.groupby('location')['listing_price'].mean()
    print("Average Listing Price of Properties in Each Location:")
    print(average_listing_price)
    print()

    # 2. Number of properties with more than four bedrooms
    properties_with_more_than_four_bedrooms = property_data[property_data['bedrooms'] > 4]
    number_of_properties_with_more_than_four_bedrooms = properties_with_more_than_four_bedrooms.shape[0]
    print("Number of Properties with More Than Four Bedrooms:", number_of_properties_with_more_than_four_bedrooms)
    print()

    # 3. Property with the largest area
    property_with_largest_area = property_data.loc[property_data['area'].idxmax()]
    print("Property with the Largest Area:")
    print(property_with_largest_area)

if __name__ == "__main__":
    main()
