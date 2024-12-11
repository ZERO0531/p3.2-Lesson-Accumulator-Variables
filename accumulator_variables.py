# 1. calculate the sum of the numbers from 1 to 10.
total = 0
while count <= 10:
    total += count
    count += 1
print(f"The sum of numbers from 1 to 10 is: {total}" )

# 2. calculate the sum of the numbers from 100 to 200.
count = 100
total = 0
while count <= 200:
    total += count
    count += 1
print(f"The sum of numbers from 100 to 200 is: {total}" )

# 3. calculate the difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300.
count = 100
total1 = 0
while count <= 200:
    total1 += count
    count += 1

count = 200
total2 = 0
while count <= 300:
    total2 += count
    count += 1
  
difference = total1 - total2

print(f"The sum of numbers from 100 to 200 is: {total1} )
print(f"The sum of numbers from 200 to 300 is {total2} )
print(f"The difference between the two sums is {difference})

# 4. calculate the sum of the multiples of 5 between the numbers 1000 and 10000.
total = 0
if count % 5 == 0:
total += count
print(f"The sum of multiples of 5 between 1000 and 10000 is: {total} )

# 5. calculate the sum of the multiples of 5 between 1 and 100, but do not include numbers that are multiples of 3. Modulus (%) will come in handy here.
total = 0
if count % 5 == 0 and count % 3 != 0:
    total += count
print(f"The sum of multiples of 5 between 1 and 100 (excluding multiples of 3) is: {total} )
