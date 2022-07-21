# Finding largest number 
largest_no = -1
print('Before', largest_no)
for num in [9,41,12,3,74,15]:
    if largest_no < num:
        largest_no = num
    print(largest_no, num)
print('After', largest_no)