'''
Week 09 - Team Activity - Students.py
https://byui-cse.github.io/cse111-course/lesson09/teach.html

  1 - Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, and read the other lines of the file into a dictionary. The program must store each student I-Number as a key and each I-Number name pair or each name as a value in the dictionary.
  2 - Get an I-Number from the user, use the I-Number to find the corresponding student name in the dictionary, and print the name.
  3 - If a user enters an I-Number that doesn't exist in the dictionary, your program must print the message, "No such student" (without the quotes).

Stretch 
  1 - Add code to remove dashes from the I-Number that the user enters. This will allow the user to enter I-Numbers with dashes or without dashes and still allow the computer to search in the dictionary.
  2 - When a user enters an I-Number, your program should ensure it is a valid I-Number.
    - If there are too few digits in the I-Number, your program should print, "Invalid I-Number: too few digits" (without the quotes).
    - If there are too many digits in the I-Number, your program should print, "Invalid I-Number: too many digits" (without the quotes).
    - If the given I-Number contains any characters besides digits and dashes, your program should output "Invalid I-Number" (without the quotes).
    - Add something or change something in your program that you think would make your program better, easier for the user, more elegant, or more fun. Be creative.

'''
import csv

def read_dict(filename, key_column_index=0):
  """Read the contents of a CSV file into a compound dictionary and return the dictionary.

  Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column to use as the keys in the dictionary.
  Return: a compound dictionary that contains the contents of the CSV file.
  """
  with open (filename) as file:
    next (file)
    dictionary = {}
    for line in file:
      line = line.strip()

      part = line.split(',')

      if(len(part) > 0):
      
        key = part[key_column_index]
      
        dictionary[key] = part
    return dictionary

def get_sid_input(in_msg:str = "Please enter an I-Number (xxxxxxxxx): "):
  while(True):
    in_str = input(in_msg)#.replace("-","") #- is handled by the filter too!
    
    #Keep letters only in the num_char_list
    num_char_list = ["0","1","2","3","4","5","6","7","8","9"]
    new_str = "" #New string to store only valid inputs
    for i in range(len(in_str)): #Check every letter
      if(in_str[i] in num_char_list): #Check this input letter with the numeric chalist
        new_str += in_str[i] #Add the current digit to new_str

    #String is now numbers only

    if(len(new_str) == 9): #Valid I-Number Length
      return new_str #return the new_str (not the in_str)
    elif len(new_str) < 9: #Shorter then 9 digits
      print ('Invalid I-Number: too few digits')
    elif len(new_str) > 9: #Longer then 9 digits
      print ('Invalid I-Number: too many digits')
    else: #blank or no entry
      print ('Invalid I-Number')

def main ():
  students:dict = read_dict('students.csv')

  #print (students)
  student_id_str = get_sid_input()
  print(student_id_str) #HERE!
  #if(student_id_str in list(students.keys())):
  if(students.get(student_id_str,"") != ""):
    print(students[student_id_str][1])

  else:
    print("No such student")


# Call main to start this program.
if __name__ == "__main__":
  main()

