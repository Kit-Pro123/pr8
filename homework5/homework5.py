t=0
T=True
while T:
    print("Введите число")
    n=input()
    if n=="end" or n=='stop':
        T=False
        break
    else:
        for i in range(len(n)):
            if n[i] in "0123456789,.-":
                b=1
            else:
                b=0
                break
        if b==1:
            t+=float(n)
        else:
            print("введите число, а не буквы")
            T=False
            break
print(t)