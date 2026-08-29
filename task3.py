def is_prime(n):
    a = ()
    for i in range(1,n):
        if n%i == 0:
            a = "False"
            break
    else:
        a = "True" 
    return(a)    
b = int(input("Enter a no:"))
print("Is the no a prime(T/F):",is_prime(b))   
     