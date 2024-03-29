from give_bmi import give_bmi, apply_limit

height = [1.80]
weight = [62.5]

# Calculate BMI using the give_bmi function
bmi = give_bmi(height, weight)
print(bmi, type(bmi))  # Print the calculated BMI values and their data type

# Apply the limit using the apply_limit function
limit = 25
above_limit = apply_limit(bmi, limit)
print(above_limit)  # Print the boolean values indicating whether each BMI value is above the limit