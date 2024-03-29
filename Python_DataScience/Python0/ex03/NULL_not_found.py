import math

def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing:", (obj), type(obj))
    elif isinstance(obj, float) and math.isnan(obj):
        print(f"Cheese:", (obj), type(obj))
    elif obj is False:
        print(f"Fake: ", (obj), type(obj))
    elif obj == 0:
        print(f"Zero: ", (obj), type(obj))
    elif isinstance(obj, str) and len(obj) == 0:
        print(f"Empty:", type(obj))
    else:
        print("Type not Found")
        return 1 
    return 0