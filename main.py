# computing the area of a trapezoid
import string
from pyscript import display, document


def area_trapezoid(e):
    base1 = float(document.getElementById('num1').value)
    base2 = float(document.getElementById('num2').value)
    height = float(document.getElementById('num3').value)
    area = ((base1 + base2) / 2) * height

    display(f'The area of this trapezoid is {area}')