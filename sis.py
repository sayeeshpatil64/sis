import sys

script_name = sys.argv[0]

if len(sys.argv) == 7:  # Changed from 3 to 7 since you need 6 arguments + script name
    name = sys.argv[1]
    mark1 = sys.argv[2]
    mark2 = sys.argv[3]
    mark3 = sys.argv[4]
    mark4 = sys.argv[5]
    mark5 = sys.argv[6]
    print("User provided input values:")
else:
    name = "sayeesh"
    mark1 = "35"
    mark2 = "35"
    mark3 = "35"
    mark4 = "35"
    mark5 = "35"
    print("No input given, using default values:")

total = int(mark1) + int(mark2) + int(mark3) + int(mark4) + int(mark5)
average = total / 5 
print("File Name:", script_name)
print("Student Name:", name)
print("Subject 1 marks :", mark1)
print("Subject 2 marks :", mark2)
print("Subject 3 marks :", mark3)
print("Subject 4 marks :", mark4)
print("Subject 5 marks :", mark5)
print("Total Marks:", total)
print("Average Marks:", average)
