def calc(a, b, operator):
    if type(a) == str or type(b) == str:
        # do something
        print("sorry we are unable to calculate that querry") 
        return

    #print("Okay it is working")

    num1 = int(a) if type(a)=="int" else float(a)
    num2 = int(b) if type(b)=="int" else float(b)
    result = 0
    if operator == "+":
        result = num1+num2
        return result
    elif operator == "/":
        result = num1/num2
        return result
    elif operator == "-":
        result = num1-num2
        return result
    else:
        result = num1*num2
        return result

print(calc(34, 40, "+"))