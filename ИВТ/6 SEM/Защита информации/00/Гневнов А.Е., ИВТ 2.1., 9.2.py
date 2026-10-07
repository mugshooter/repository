def Rem(n, m, b):
    # если m 0   
    if m == 0:  
        return 1  
    elif m % 2 == 0:  
        # если m чётное  
        return Rem((n * n) % b, m // 2, b)  
    else:  
        # если m нечётное  
        return (n * Rem((n * n) % b, (m - 1) // 2, b)) % b  


n = 4  
m = 12
b = 7  
print(Rem(n, m, b)) 