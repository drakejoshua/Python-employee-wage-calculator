# welcome text
print("welcome to the employee wage calculator \n")

# the variable for the recalculation
recalculate = True
isEmployeeLevelSet = False


# the calculateEmployeeWage function
# this is used to calculate the employee wage based on the employee level and the 
# number of hours worked by that employee
def calculateEmployeeWage( employeeLevel, hoursWorked ):
    if employeeLevel == "manager":
        print("\tThe wage for this employee is:", int( hoursWorked ) * 12 )
    elif employeeLevel == "supervisor":
        print("\tThe wage for this employee is:", int( hoursWorked ) * 8 )
    else:
        print("\tThe wage for this employee is:", int( hoursWorked ) * 4 )



# get the employee level details and the number of hours worked 
while recalculate: 
    # prompt the user for the employee level
    employeeLevel = input("Enter an employee level > ")

    # verify that the right string was entered for the employeeLevel
    while isEmployeeLevelSet != True:
        if employeeLevel == 'manager':
            isEmployeeLevelSet = True
        elif employeeLevel == 'supervisor':
            isEmployeeLevelSet = True
        elif employeeLevel == 'worker':
            isEmployeeLevelSet = True
        else:
            print("Invalid Value, Please enter a valid employeee level\n")
            employeeLevel = input("Enter an employee level > ")

    # prompt the user for the number of hours worked
    hoursWorked = input("Enter the number of hours worked by this employee > ")

    # calculate and display the employee's wage
    calculateEmployeeWage( employeeLevel, hoursWorked )

    # prompt and check if the user wants to perform another employee wage calculation
    # otherwise end the loop
    performRecalculation = input("Do you want to re-calculate the wage for another employee? Enter YES to calculate > ")
    # add new line to display
    print("\n")

    if performRecalculation != 'YES':
        recalculate = False
