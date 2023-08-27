import textwrap

def wrap(string, max_width):
    res=[]
    loop = len(string)//max_width +1
    for i in range(loop):
        res.append(string[max_width*i:max_width*(i+1)])
    ans="\n".join(i for i in res)
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
