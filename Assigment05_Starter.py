# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# jcarnes, 11.15.2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
lstData = []  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
lstFile = []    # A list that acts as a 'table' of rows


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# Try/except block used for cases when file does not exist in working directory
try:
    objFile = open("ToDoList.txt", "r")
    for rows in objFile:
        lstData = rows.split(",")  # THIS IS A LIST - NOT STRING
        dicRow = {"Task": lstData[0], "Priority": lstData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except:
    lstTable = []

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: DONE
        if lstTable == []:
            print("To Do List is Empty - Go Have Fun!")
            continue
        else:
            for rows in lstTable:
                print('Task: ' + rows['Task'] + "\t\t\t\t\t Priority: " + rows['Priority'])
            continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: DONE
        print("Please enter a task and priority")
        strTask = input("Task: ")
        strPriority = input("Priority: ")
        dicRow = {"Task": strTask.strip(), "Priority": strPriority.strip()}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: DONE
        strTask = input("Please enter the task to be removed: ")
        IntRemovedCounter = 0  # Counter to keep track of how many rows are removed
        IntRowCounter = 0  # Index Counter
        while IntRowCounter < len(lstTable):
            if lstTable[IntRowCounter]['Task'].lower() == strTask.lower().strip():
                IntRemovedCounter += 1
                lstTable.pop(IntRowCounter)
                # Row counter should not increase if a row was removed as remaining elements have shifted indexes
            else:
                IntRowCounter += 1
        # Display message to user based on how many rows removed
        if IntRemovedCounter == 1:
            print("The row " + strTask + " was removed")
        elif IntRemovedCounter > 1:
            print(str(IntRemovedCounter) + ' Rows for ' + strTask + ' were removed!')
        else:
            print(strTask + " was not found!")
        continue
        
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: DONE
        objFile = open("ToDoList.txt", 'w')
        for rows in lstTable:
            objFile.write(rows["Task"] + ',' + rows["Priority"] + "\n")
        objFile.close()
        print("Data saved to file!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: DONE
        # Check to see if the user has saved prior to exiting
        # Load current contents of text file to lstFile then compare to lstTable
        try:
            objFile = open("ToDoList.txt", 'r')
            for rows in objFile:
                lstData = rows.split(",")  # THIS IS A LIST - NOT STRING
                dicRow = {"Task": lstData[0], "Priority": lstData[1].strip()}
                lstFile.append(dicRow)
            objFile.close()
        except:
            lstFile = []

        if lstFile == lstTable:
            print("Goodbye!")
            break  # and Exit the program
        else:
            strSave = input("File has not been saved! Would you like to save before exiting? (y/n): ")
            while True:
                if (strSave.lower() == 'y'):
                    objFile = open("ToDoList.txt", 'w')
                    for rows in lstTable:
                        objFile.write(rows["Task"] + ',' + rows["Priority"] + "\n")
                    objFile.close()
                    print("Data saved to file! Goodbye!")
                    break  # break from save loop
                elif strSave.lower() == 'n':
                    print("Goodbye!")
                    break  # break from save loop
                else:
                    strSave = input("Please enter a valid input. Would you like to save before exiting? (y/n): ")
                    continue
            break  # and Exit the program
