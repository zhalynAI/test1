x=float(input("Введите значение x =")) 

y=float(input("Введите значение y ="))  

z=input("Введите оператор (+, -, /, *,) =") 

if z == +:

    result=x+y  

elif z==-: 
    
    result=x-y   
elif z==pow:     
result=pow(x,y)  
elif z==*:      
result=x*y   
elif y!=0:     
    if z==/:       
result=x/y     
    elif z==div:       
result=x//y    
    elif z==mod:       
result=x%y      
    elif y==0:     
result="Деление на 0!"   
    print("Результат вычислений =",result)
 