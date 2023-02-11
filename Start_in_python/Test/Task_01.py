from c_task_01 import create_equation
from Coding import decode
from encoding import encode
from addition import addition

if __name__ == '__main__':
    equation = create_equation()
    print(equation)
    str_equation = decode(equation)
    print(str_equation)
    dict_equation = encode(str_equation)
    print(dict_equation)

    # equation1 = create_equation()
    # equation2 = create_equation()
    # print(decode(equation1))
    # print(decode(equation2))
    # print(decode(addition(equation1, equation2)))



