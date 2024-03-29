import matplotlib.pyplot as plt
from load_csv import load  # Import the load function from your first exercise

def convert_population(population):
    """
    Convert population values with 'M' for millions and 'k' for thousands to integers.

    Args:
        population (str): The population value as a string.

    Returns:
        int: The converted population as an integer.
    """
    population = population.replace(',', '')  # Remove commas
    if 'M' in population:
        # Remove 'M' and convert to millions
        return int(float(population.replace('M', '')) * 1e6)
    elif 'k' in population:
        # Remove 'k' and convert to thousands
        return int(float(population.replace('k', '')) * 1e3)
    else:
        # If no 'M' or 'k', assume it's already an integer
        return int(population)

def plot_population_comparison(data):
    """
    Plot the population of Malaysia and France from 1800 to 2050.

    Args:
        data (list of lists): The dataset containing the population data.
    """
    years = data[0][1:]  # Extract years
    malaysia_population = None
    france_population = None

    for row in data:
        if row[0] == "Malaysia":
            malaysia_population = row[1:]
        elif row[0] == "France":
            france_population = row[1:]

    if malaysia_population is None or france_population is None:
        print("Data for Malaysia and France not found in the dataset.")
        return

    years = list(map(int, years))
    malaysia_population = [convert_population(pop) for pop in malaysia_population]
    france_population = [convert_population(pop) for pop in france_population]

    plt.figure(figsize=(10, 6))
    plt.plot(years, malaysia_population, label="Malaysia")
    plt.plot(years, france_population, label="France")
    plt.title("Population Comparison: Malaysia vs. France (1800-2050)")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

def main():
    dataset = load("population_total.csv")

    if dataset is not None:
        plot_population_comparison(dataset)

if __name__ == "__main__":
    main()

