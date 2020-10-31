num = 5

def premier(n):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(False)
                break
        else:
            print(True)
       
    else:
        print(False)
    
premier(num)