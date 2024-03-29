from load_csv import load
import csv
import matplotlib.pyplot as plt

def plot_life_expectancy(data): # the data here is a parameters
    """
    Plot life expectancy data for Malaysia over the years.

    Args:
        data (list of lists): The dataset containing the CSV data.
    """
    # Extract years and life expectancy values for Malaysia
    years = data[0][1:]  # Years start from the second column (index 1)
    malaysia_data = None

    for row in data:
        if row[0] == "Malaysia":
            malaysia_data = row[1:]
            break

    if malaysia_data is None:
        print("Malaysia data not found in the dataset.")
        return

    # Convert years and data to integers and floats
    years = list(map(int, years))
    malaysia_data = list(map(float, malaysia_data))

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, malaysia_data, label="Malaysia")
    plt.title("Life Expectancy in Malaysia Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Load the CSV data
    dataset = load("life_expectancy_years.csv")

    if dataset is not None:
        # Plot life expectancy for Malaysia
        plot_life_expectancy(dataset)

if __name__ == "__main__":
    main()