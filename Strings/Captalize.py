#!/bin/python3


# Complete the solve function below.
def solve(s):
    l = s.split(" ")
    for i in range(len(l)):
        string = l[i]
        l[i] = string.capitalize()
        
    return " ".join(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
