Step to step instruction of how to create bmi calculator and instructions for task 

create a file named `bmi.csv`

import csv # 
file = open("bmi.csv", "a") # variable (file) opens the file and appends the file bmi.. etc
# here is more help on it https://www.w3schools.com/python/python_file_write.asp
-----------------------------------------------------------------------------------------------
 # record input from user 
  name 
  weight in kg 
  height in centimetres 
  
  must be to 2 decimal places e.g (round(weight, 2)
 
  # the formula is complex and hard but I figured it out.
                                   
  height in centimetres divide by 100 to get height in metres 
  then to get bmi = weight (kg) divide then do (height in metres * height in metres) # * means multiplication 
                                   
                                   
  Then with the bmi answer you must classify wihich category the person is in.
  # This part must be in a function named main()
                                   
  bmi < 18.5 UnderWeight
                                   
  bmi >= 18.5 and bmi < 25.0 Healthy
                                   
  bmi >= 25.0 and bmi < 30.0 OverWeight
                                   
  bmi >= 30.0 Obese
  
  define results and give the user the category they are in and their categorisation e.g healthy etc 
  
  ---------------------------------------------------------------------------
 # you must record the data in the bmi.csv example below
                                   
file.write("\nYour name is " + name) # \n will space out the data to the next line below 
file.close()
file = open("bmi.csv", "r")
print(file.read())
                                   
# THis should make it 10x easier to understand 
                                   
  
