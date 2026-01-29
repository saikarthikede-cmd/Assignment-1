#Task 2:
'''
Given a list of numbers (as strings):
nums = ["10", "20", "abc", "30", "5"]
Tasks
Convert valid numbers to integers (ignore invalid values using exception handling).
1.keep only numbers greater than 10.
2.square the remaining numbers.
3.find the sum of squared values.
'''

nums = ["10", "20", "abc", "30", "5"]
valid_num=[]
invalid_num=[]
s=0
for x in nums:
    try:
        if x.isdigit():   #to check or validate the element
            n=int(x)
            if n>10:
                valid_num.append(n)
    except:
        if x not in valid_num:
            invalid_num.append(x)
    finally:  
        pass
for i in valid_num:
    s+=(i*i)          #30*30=900 +20*20=400=1300
print(valid_num)
print(s)
        


'''
filtered=filter(lambda i:i*i,valid_num )
print(list(filtered))
'''