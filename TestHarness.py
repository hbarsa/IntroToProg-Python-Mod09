# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# HBarsa,9.7.2022,Modified script for assignment 09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    #from DataClasses import Person as D  # Person class only!
    from DataClasses import Employee as Emp  # Employee class only!
    #import ProcessingClasses as P  # processing classes
    from ProcessingClasses import FileProcessor as Fp   # FileProcessor class only!
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module - Person Class
#objP1 = D.Person("Bob", "Smith")
#objP2 = D.Person("Sue", "Jones")
#lstTable = [objP1, objP2]
#for row in lstTable:
#    print(row.to_string(), type(row))

# Test data module - Employee Class
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))


# Test processing module - Person Data
#P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
#lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
#for row in lstFileData:
#    p = D.Person(row[0], row[1])
#    print(p.to_string().strip(), type(p))

# Test processing module - Employee Data
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))


# Test IO classes
# TODO: create and test IO module
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())