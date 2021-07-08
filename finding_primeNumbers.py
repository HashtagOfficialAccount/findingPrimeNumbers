#user picks the start and end number
start_num = int(input('Enter the starting number: '))
end_num = int(input('Enter the ending number: '))
primes = []

#for loop to loop from the start number to the end number 
for x in range(start_num,end_num + 1):
    if not(x % 2 == 0 and x != 2 or x % 3 == 0 and x != 3 or x % 5 == 0 and x != 5 or x % 7 == 0 and x != 7):
        primes.append(x)

print(primes)