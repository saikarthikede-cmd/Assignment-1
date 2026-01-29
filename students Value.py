#Task1:
students = [("Anil", 8),("Ravi", 45),("Meena", 88),("Sita", 62),("Raj", 49)]
Value_st={} 
pass_cnt=0  #to count no of passed and failed students
fail_cnt=0
for name,marks in students:  
    if marks>=50:
        Value_st[name]="pass"
        pass_cnt +=1
    else:
        Value_st[name]="fail"
        fail_cnt+=1
print(Value_st)
print("no of students passed ",pass_cnt)
print("no of students failed ",fail_cnt)