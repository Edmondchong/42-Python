import csv

def load(path: str):
    """
    Load a CSV file, display its dimensions, and return the dataset.

    Args:
        path (str): The path to the CSV file.

    Returns:
        list of lists or None: The dataset if successfully loaded, None on error.
    """
    try:
        dataset = []

        # Open the CSV file
        with open(path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                dataset.append(row)

        # Get the dimensions (number of rows and columns) of the dataset
        num_rows = len(dataset)
        num_cols = len(dataset[0])

        # Print the dimensions
        print(f"Loading dataset of dimensions ({num_rows}, {num_cols})")

        # Return the dataset
        return dataset

    except FileNotFoundError:
        # Handle the case where the file is not found
        print("Error: File not found.")
        return None
    except csv.Error:
        # Handle CSV-related errors
        print("Error: Unable to read the CSV file. Check its format.")
        return None

def main():
    # Test the load function with a CSV file
    dataset = load("life_expectancy_years.csv")

    # Check if the dataset was loaded successfully
    if dataset is not None:
        # Print the first few rows of the dataset
        for row in dataset[:5]:  # Print the first 5 rows
            print(row)

if __name__ == "__main__":
    main()