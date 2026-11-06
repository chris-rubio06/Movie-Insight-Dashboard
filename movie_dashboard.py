
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("File not found.")
        return pd.DataFrame()

def show_statistics(df):
    print("\n--- Movie Statistics ---")
    print(f"Average Rating: {df['rating'].mean():.2f}")
    print(f"Average Budget: ${df['budget'].mean():,.2f}")
    top_movie = df.loc[df['rating'].idxmax()]
    print(f"Top Rated Movie: {top_movie['title']} ({top_movie['rating']})")

def filter_movies(df):
    min_rating = float(input("Enter minimum rating (e.g., 7.0): "))
    min_year = int(input("Enter minimum release year (e.g., 2010): "))
    filtered = df[(df['rating'] >= min_rating) & (df['release_year'] >= min_year)]
    print(f"\nFound {len(filtered)} movies matching criteria.")
    return filtered

def visualize_data(df):
    print("\n--- Creating Visualizations ---")

    plt.figure(figsize=(8, 5))
    sns.histplot(df['rating'], bins=15, kde=True)
    plt.title("Distribution of Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='budget', y='revenue')
    plt.title("Budget vs Revenue")
    plt.xlabel("Budget")
    plt.ylabel("Revenue")
    plt.show()

def save_filtered_data(filtered_df):
    filename = input("Enter filename to save filtered results (e.g., filtered_movies.csv): ")
    filtered_df.to_csv(filename, index=False)
    print(f"Filtered data saved to {filename}")

def main():
    df = load_data("movies.csv")
    if df.empty:
        return

    while True:
        print("\n--- Movie Insight Dashboard ---")
        print("1. Show Movie Statistics")
        print("2. Filter Movies")
        print("3. Visualize Data")
        print("4. Save Filtered Movies")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_statistics(df)
        elif choice == '2':
            global filtered
            filtered = filter_movies(df)
        elif choice == '3':
            visualize_data(df)
        elif choice == '4':
            if 'filtered' in globals():
                save_filtered_data(filtered)
            else:
                print("No filtered data available. Please filter movies first.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
