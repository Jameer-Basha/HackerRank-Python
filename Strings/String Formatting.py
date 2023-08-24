def print_formatted(number):
    # your code goes here
    res=[]
    length = len(bin(number)[2:])
    for i in range(1,number+1):
        octa=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        bina=bin(i)[2:]
        
        formatt=" "*(length-len(str(i)))
        formatt+=str(i)
        formatt+=" "*(length-len(octa)+1)
        formatt+=octa
        formatt+=" "*(length-len(hexa)+1)
        formatt+=hexa
        formatt+=" "*(length-len(bina)+1)
        formatt+=bina
        res.append(formatt)
    
    ans="\n".join(i for i in res)
    print(ans)
    return ans
