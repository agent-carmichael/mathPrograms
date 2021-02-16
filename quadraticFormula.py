import sys
import math


def quadratic_formula(a, b, c):
    additionNumerator = (-1*b) + math.sqrt((b**2)-(4*a*c))
    subtractionNumerator = (-1*b) - math.sqrt((b**2)-(4*a*c))
    denominator = 2*a
    additionValue = additionNumerator / denominator
    subtractionValue = subtractionNumerator / denominator

    print("sub: " + str(subtractionValue) + " -- add: " + str(additionValue))
    return "success."


quadratic_formula(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
