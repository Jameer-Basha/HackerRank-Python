def merge_the_tools(string, k):
    # your code goes here
    a, b = '', ''
    for i in string:
        if i in a:
            b += i
        else:
            a, b = a + i, b + i
        if len(b) == k:
            print(a)
            a, b = '', ''
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(str
