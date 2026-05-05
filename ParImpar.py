num = [5, 5, 6, 9, 8, 7, 3, 2, 1, 9, 5]
par = []
impar = []

for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(par)
print(impar) 
       