#Average of numbers using loop
sum = 0
count = 0 
print('Before' , sum, count)
for num in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + num
    print(count , sum , num)
print('After : Average =', sum/count)