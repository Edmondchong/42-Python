def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi_values = []
    
    if len(height) != len(weight):
        raise ValueError("Input lists must have the same length")
        
    # Calculate BMI for each pair of height and weight
    for i in range(len(height)):
        bmi = weight[i] / (height[i] * height[i])
        bmi_values.append(bmi)
    
    return bmi_values

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    # Initialize an empty list to store boolean values
    above_limit = []
    
    # Check if each BMI value is above the specified limit
    for value in bmi:
        above_limit.append(value > limit)
    
    return above_limit
