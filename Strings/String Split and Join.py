def split_and_join(line):
    # write your code here
    lst=list(line.split())
    res="-".join(i for i in lst)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
