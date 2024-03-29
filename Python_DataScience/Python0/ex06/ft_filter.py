def ft_filter(function, iterable):
    # Use list comprehension to filter elements based on the given function
    filtered_elements = [item for item in iterable if function(item)]
    
    return filtered_elements