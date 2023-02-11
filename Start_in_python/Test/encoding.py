def encode(equation: str) -> dict:
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')\
        .replace(' -x', ' -1*x').replace(' x', ' 1*x')\
        .replace('*x ', '*x**1 ').split()[:-2]
    print(equation)
    dict_equation = {}
    for item in equation:
        i = item.split('*x**')
        print(i)
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        else:
            dict_equation[0] = int(i[0])

    return dict_equation


