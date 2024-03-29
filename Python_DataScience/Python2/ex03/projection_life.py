import matplotlib.pyplot as plt
from load_csv import load  # Import the load function from your first exercise

def plot_life_expectancy_vs_income(income_data, life_expectancy_data):
    """
    Plot life expectancy versus gross national product for the year 1900 for all countries.

    Args:
        income_data (list of lists): The dataset containing income data.
        life_expectancy_data (list of lists): The dataset containing life expectancy data.
    """
    # Extract the year 1900 data from both datasets
    income_1900 = income_data[0][1:]
    life_expectancy_1900 = life_expectancy_data[0][1:]

    if not income_1900 or not life_expectancy_1900:
        print("Data for 1900 not found in the datasets.")
        return

    # Ensure that the data arrays are the same size
    min_data_size = min(len(income_1900), len(life_expectancy_1900))
    income_1900 = [float(income.replace('k', '000')) if 'k' in income else float(income) for income in income_1900[:min_data_size]]
    life_expectancy_1900 = [float(val) for val in life_expectancy_1900[:min_data_size]]

    # Create a scatter plot with blue dots for all countries in 1900
    plt.figure(figsize=(10, 6))
    plt.scatter(income_1900, life_expectancy_1900, c='blue', s=10, marker='o')
    plt.title("Life Expectancy vs. Gross Domestic Product (Year 1900)")
    plt.xlabel("Gross Domestic Product (Income) in 1900")
    plt.ylabel("Life Expectancy in 1900")

    plt.show()

def main():
    income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")

    if income_data is not None and life_expectancy_data is not None:
        plot_life_expectancy_vs_income(income_data, life_expectancy_data)

if __name__ == "__main__":
    main()
