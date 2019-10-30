def add(x, y):
    return x + y

# this function adds more than two numbers
def addMore(args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
        continue
    return sum

def multiplyMore(args):
    sum = 1
    for i in range(len(args)):
        sum *= args[i]
        continue
    return sum
