import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Returns a list of bmi values given a list of heights and weights """
    try:
        if len(height) != len(weight):
            raise Exception("Height and weight must have the same length")
        for i in range(len(height)):
            if not isinstance(height[i], (int, float)) or not isinstance(weight[i], (int, float)):
                raise Exception("Height and weight must be numbers")
        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi_array = weight_array / (height_array ** 2)
        return bmi_array.tolist()
    
    except Exception as e:
        print(e)
        return None
    

def apply_limit(bmi: list[int | float], limit: int | float) -> list[bool]:
    """ check if bmi is above the limit """
    try:
        bmi_array = np.array(bmi)
        return (bmi_array > limit).tolist()
    except Exception as e:
        print(e)
        return None