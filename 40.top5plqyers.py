import pandas as pd
import matplotlib.pyplot as plt

def analyze_soccer_players(file_path):
    # Read the data from the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Find the top 5 players with the highest number of goals scored
    top_5_goals = df.nlargest(5, 'GoalsScored')

    # Find the top 5 players with the highest salaries
    top_5_salaries = df.nlargest(5, 'Salary')

    # Calculate the average age of players
    average_age = df['Age'].mean()

    # Get names of players who are above the average age
    above_average_age_players = df[df['Age'] > average_age]['Name']

    # Visualize the distribution of players based on their positions using a bar chart
    position_counts = df['Position'].value_counts()

    plt.figure(figsize=(8, 6))
    plt.bar(position_counts.index, position_counts.values)
    plt.xlabel('Position')
    plt.ylabel('Number of Players')
    plt.title('Distribution of Players by Position')
    plt.show()

    return top_5_goals, top_5_salaries, average_age, above_average_age_players

def main():
    file_path = 'soccer_players_data.csv'
    top_5_goals, top_5_salaries, average_age, above_average_age_players = analyze_soccer_players(file_path)

    print("Top 5 Players with the Highest Number of Goals:")
    print(top_5_goals)

    print("\nTop 5 Players with the Highest Salaries:")
    print(top_5_salaries)

    print(f"\nAverage Age of Players: {average_age:.2f}")

    print("\nPlayers Above Average Age:")
    print(above_average_age_players)

if __name__ == "__main__":
    main()
