#Student marks,Percentage and Grade
name=input("Enter student name:")
n=int(input("Enter number of subject:"))
total=0
for i in range(1,n+1):
    mark=float(input("Enter mark for subject{i}: "))
    total+=mark
percentage=total/n
if percentage >=90:
    grade="A+"
    performance="Outstandig"
elif percentage>=80:
    grsde="A"
    performance="Execellent"
elif percentage>=70:
    grade="B"
    performance="Very good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else:
    grade="F"
    performance="Average or needs Improvement"
print("\n Academic performance")
print("student name:",name)
print("total marks:",total)
print("percentage:",round(percentage,2),"%")
print("Grade:",grade)
print("performance:",performance)