from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15, 2]
weight = [165.3, 38.4, 100]

bmi = give_bmi(height, weight)
print(bmi)
print(apply_limit(bmi, 26))