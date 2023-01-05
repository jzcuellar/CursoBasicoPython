# MI SOLUCION
# def bmi(weight, height):
#     bod_mass_index = weight / (height**2)
#     if bod_mass_index <= 18.5:
#         return "Underweight"
#     elif bod_mass_index <= 25.0:
#         return "Normal"
#     elif bod_mass_index <= 30.0:
#         return "Overweight"
#     elif bod_mass_index > 30:
#         return "Obese"

# CLEVER SOLUTION
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)] 

"""
You can add boolean values in Python (True -> 1, False -> 0).
For example, if b == 27 then you get for (b > 30) + (b > 25) + (b > 18.5) -> False + True + True -> 0 + 1 + 1 -> 2 
['Underweight', 'Normal', 'Overweight', 'Obese'][2] -> 'Overweight'
"""

print(bmi(76,1.75))

print(['Underweight', 'Normal', 'Overweight', 'Obese'][3]) # Ejemplo de como funciona esta solucion