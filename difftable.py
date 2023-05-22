# Ahmet Can SENER

import array as arr

x_s = arr.array('i', [0, 1, 2, 4, 6])   # x values
fx = arr.array('i', [1, 9, 23, 93, 259]) # f(x) values

# first divided differences function
def first_div_dif(a, b): 
    result = (fx[b] - fx[a]) / (x_s[b] - x_s[a])
    return result

# second divided differences function
def second_div_dif(a, b, c):
    result = (first_div_dif(b, c) - first_div_dif(a, b)) / (x_s[c] - x_s[a])
    return result
    
# third divided differences function
def third_div_dif(a, b, c, d):
    result = (second_div_dif(b, c, d) - second_div_dif(a, b, c)) / (x_s[d] - x_s[a])
    return result
    
# fourth divided differences function
def fourth_div_dif(a, b, c, d, e):
    result = (third_div_dif(b, c, d, e) - third_div_dif(a, b, c, d)) / (x_s[e] - x_s[a])
    return result

# Newton Interpolation Polynomial
def newton_interpolation(x):
    result = fx[0] + first_div_dif(0, 1) * (x - x_s[0]) + second_div_dif(0, 1, 2) * (x - x_s[0]) * (x - x_s[1]) + third_div_dif(0, 1, 2, 3) * (x - x_s[0]) * (x - x_s[1]) * (x - x_s[2]) + fourth_div_dif(0, 1, 2, 3, 4) * (x - x_s[0]) * (x - x_s[1]) * (x - x_s[2]) * (x - x_s[3])
    return result

# print the divided difference table
def print_table():
    print("\n")
    print("|   x    |    f(x)    |   First Div. Diffs.   |   Second Div. Diffs.   |   Third Div. Diffs.   |   Fourth Div. Diffs.   |")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("| x0= " + str(x_s[0]) + "  |     " + str(fx[0]) + "      |           -           |           -            |           -           |           -            |")
    print("| x1= " + str(x_s[1]) + "  |     " + str(fx[1]) + "      |           " + str(first_div_dif(0, 1)) + "           |           -            |           -           |           -            |")
    print("| x2= " + str(x_s[2]) + "  |     " + str(fx[2]) + "     |           " + str(first_div_dif(1, 2)) + "          |           " + str(second_div_dif(0, 1, 2)) + "            |           -           |           -            |")
    print("| x3= " + str(x_s[3]) + "  |     " + str(fx[3]) + "     |           " + str(first_div_dif(2, 3)) + "          |           " + str(second_div_dif(1, 2, 3)) + "            |           " + str(third_div_dif(0, 1, 2, 3))    + "           |           -            |")
    print("| x4= " + str(x_s[4]) + "  |     " + str(fx[4]) + "    |           " + str(first_div_dif(3, 4)) + "          |           " + str(second_div_dif(2, 3, 4)) + "           |           " + str(third_div_dif(1, 2, 3, 4))   + "           |           " + str(fourth_div_dif(0, 1, 2, 3, 4)) + "            |")
    print("\n")
    
print("\n")
print("Divided Difference Table:")
print_table()

print("Newton Polynomial:\n")
print("f(x) = " + str(fx[0]) + " + " + str(first_div_dif(0, 1)) + "(x - " + str(x_s[0]) + ") + " + str(second_div_dif(0, 1, 2)) + "(x - " + str(x_s[0]) + ")(x - " + str(x_s[1]) + ") + " + str(third_div_dif(0, 1, 2, 3)) + "(x - " + str(x_s[0]) + ")(x - " + str(x_s[1]) + ")(x - " + str(x_s[2]) + ") + " + str(fourth_div_dif(0, 1, 2, 3, 4)) + "(x - " + str(x_s[0]) + ")(x - " + str(x_s[1]) + ")(x - " + str(x_s[2]) + ")(x - " + str(x_s[3]) + ")")

print("f(4.2) = " + str(newton_interpolation(4.2)))
print("\n")