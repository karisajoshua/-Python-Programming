Categorizing Values
Lab overview
With Python, you can mix types in a list. In this lab, you will create a list with different types and print the values.

In this lab, you will:

Use numeric data types
Use string data types
Use the list data type
Use a for loop
Use the print() function
Estimated completion time
30 minutes


Creating your Python exercise file
From the menu bar, choose File > New From Template > Python File

Delete the sample code from the template file.

Choose File > Save As..., and provide a suitable name for the exercise file (for example, categorize-values.py) and save it under the /home/ec2-user/environment directory.

Accessing the terminal session
In your AWS Cloud9 IDE, choose the + icon and select New Terminal.

A terminal session opens.

To display the present working directory, enter pwd. This command points to /home/ec2-user/environment.

In this directory, you should also be able to locate the file you created in the previous section.

Exercise 1: Creating a mixed-type list
You can mix data types in a Python list. In other languages, this capability is not a feature of lists. In this exercise, you will explore this capability.

From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.

Define a list with different types, like the following example:

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
Use a for loop statement to traverse the list and print the data type for each item in the list:

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
Save and run the file.

Confirm that the script runs correctly and that the output displays as you expect it to.

45 is of the data type <class 'int'>                             
290578 is of the data type <class 'int'>                         
1.02 is of the data type <class 'float'>                         
True is of the data type <class 'bool'>                          
My dog is on the bed. is of the data type <class 'str'>          
45 is of the data type <class 'str'>                                                        
This exercise reinforced the Python programming concepts that were covered in labs 1–6. Although the code has only a few lines, it is powerful. Take some time to review the code and make sure you understand everything that happens in it.

