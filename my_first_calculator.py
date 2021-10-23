try:
    f = open(input("Enter filename to save calculator: "), 'w')

    c = int(input("Max. number: ")) + 1

    f.write("num_1 = int(input('Enter first number: '))\n")
    f.write("num_2 = int(input('Enter second number: '))\n")
    f.write("calc = input('What do you want? (-, /, +, *) ')\n")
        
    for x in range(c):
        for y in range(c):
            if x == 0 or y == 0:
                c_div = 'Cannot divide by zero!'
            else:
                c_div = x / y

            c_sum = x + y
            c_min = x - y
            c_inc = x * y

            f.write(f"if num_1 == {x} and num_2 == {y} and calc == '+': print('{x} + {y} = {c_sum}')\n")
            f.write(f"if num_1 == {x} and num_2 == {y} and calc == '-': print('{x} - {y} = {c_min}')\n")
            f.write(f"if num_1 == {x} and num_2 == {y} and calc == '*': print('{x} * {y} = {c_inc}')\n")
            f.write(f"if num_1 == {x} and num_2 == {y} and calc == '/': print('{x} / {y} = {c_div}')\n")    
finally:
    f.close()
