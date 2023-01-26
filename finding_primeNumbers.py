#user picks the start and end number
start_num = int(input('Enter the starting number: '))
end_num = int(input('Enter the ending number: '))
primes = []

#for loop to loop from the start number to the end number 
for x in range(start_num,end_num + 1):
    t = 0
    for i in range(1, x + 1):
        if x % i == 0:
            t += 1
    if t == 2:
        primes.append(x)

print(primes)
