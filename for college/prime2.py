 # First, we will take the input:  
value = int(input ("Please, Enter the Value: "))  
   
for number in range (2, value):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  