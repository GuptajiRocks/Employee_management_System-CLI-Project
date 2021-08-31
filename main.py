import pandas as pd
#The library to facilitate the creation of Dataframe and Data Analysis
import time
#An extra module imported by us, to make the project little bit interesting
import webbrowser as wb
#To open links
import matplotlib.pyplot as plt
#Data Visualisation facilitation
import numpy as np
#Helps in graph plotting and creation of arrays
import pyttsx3
#Text-to-speech enhancement, need to install to run. Command is: pip install pyttsx3
from matplotlib.pyplot import figure
#This was imported so as to increase the size of the plotted line graph


plt.rcParams.update({'font.size': 6}) #TO shorten the X-axis and Y-axis elements so as to fit in the graph


#The below 3 lines of code, help to widen the window of displaying the running code.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


engine = pyttsx3.init('sapi5')  #Defining variable engine
voices = engine.getProperty('voices') #Calling the voice module from 'pyttsx3'
engine.setProperty('voice', voices[1].id) #Selecting the second voice type(female voice) from the voice module of 2 voice packs.


#defining 'speak' function so as to convert text-to-speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


ns = 0.5


#BEGINNING OF THE PROJECT
time.sleep(1)
print('-----------------------------------------------------------------------------|Project|----------------------------------------------------------------------------------------------')
time.sleep(1)
print()
print()
print('                                                                       WELCOME TO THE PROJECT                                                                          ')
time.sleep(1)
print()
print()
print('                                                            CREATORS: Ashutosh Asthana and Arihant Gupta                                                               ')
time.sleep(1)
print()
print()

time.sleep(2)

speak('Some basic instructions before the program starts')
time.sleep(ns)

speak('Please do install the following python modules before running this program')
time.sleep(1)

speak('pandas')
speak('matplotlib')
speak('p y t t s x 3')
speak('pyaudio')


#Starting of the master loop.
while True:

    print('''Welcome to the Program
    Enter the number preceeding your choice: 
    1. Read CSV
    2. Data Analysis
    3. Visualisation
    4. Credits
    5. Project Synopsis
    Press Any Number more than 5, to end the program.
    
    Cheers!''')
    #CSV has to be in the same folder as the source code file
    #Menu 2 takes us to the data analysis menu
    #Menu 3 takes us to the data visualisation menu
    #Menu 4 The Credits

    choice = int(input('Enter your Choice: ')) #Variable to take the value from the user of his/her respective menu choice

    if choice == 1:
        #The user chooses 1, the CSV is read and stored in the variable 'file'.
        file = pd.read_csv('true.csv') #The main DataFrame variable that is to be used via the whole project.
        print(file)

        #Checking that if the CSV is read properly or not...
        if file.empty == True:
            print('Error in reading file')
            break
        else:
            print()
            print()
            print('File Successfully Read')
            #File has been successfully read and the above message is displayed
            print()
            print()

    elif choice == 2:
        #The user chooses Menu 2, and the Data Analysis menu begins.
        print()
        print()
        print('WELCOME TO DATA ANALYSIS')
        print()
        print()

        while True:

            print('                                                         WELCOME TO DATA ANALYSIS                                                                                    ')
            print()
            print('''
            Enter the number preceding your choice:-
			1. Display Top Records
			2. Display Bottom Records
			3. To Print Particular Column
			4. To Print Multiple Columns
			5. Display DataFrame Info
			6. Addition of Column to DataFrame
                        7. Addition of Records to DataFrame
			8. Deletion of Column from DataFrame
                        9. Deletion of Records from DataFrame
                        10. Display Highest Work Experience
			11. Display All Records
			12. Exit''')

            #Printing all the menus in the Data Analysis menu.
            
            dchoice = int(input('Enter the number preceeding your choice: ')) #Variable to the menu number input from the user in the Data Analysis column..

            if dchoice == 1:
                #Program to print the first n records.
                print()
                print()
                print('Printing Top Records....')
                nt = int(input('How many top records?: ')) #Variable storing the number of top records to be displayed.
                print(file.head(nt))
                print()
                print()

            elif dchoice == 2:
                #Program to print the last n records
                print()
                print()
                print('Printing bottom records...')
                bt = int(input('How many bottom records?: ')) #vairable storing the number of bottom records to be displayed.
                print(file.tail(bt))
                print()
                print()

            elif dchoice == 3:
                #Program to print a whole particular column
                print()
                print()
                print('Printing a particular column...')
                print('These are the columns...')
                print(file.columns) #Printing all the columns so as to facilitate the user
                scp = str(input('Enter the Column name correctly: ')) #variable storing the column name
                if scp in file.columns:
                    #Iterating the columns to check if name is correct.
                    print(file[scp]) #Printing the particular column entered by user.
                    print()
                else:
                    print('Wrong name') #Stating what to happen in name entered is wrong.
                print()
                print()

            elif dchoice == 4:
                #Program to print multiple columns
                print()
                print()
                print('Printing multiple columns...')
                print()
                print('These are the columns')
                print(file.columns) #Printing all the columns so as to facilitate the user
                nmcp = int(input('How many columns, you want to print: ')) #Variable storing the number of columns to be printed.
                colname = [] #List to store column names
                #Starting a loop to input variable as per the range given by user
                for i in range(nmcp):
                    cname = str(input('Enter the column name: ')) #variable storing the name of the column
                    colname.append(cname)
                print(file[colname]) #Printing the respective columns
                print()
                print()

            elif dchoice == 5:
                print()
                print()
                print('Printing file info...')  #Printing the file info
                print()
                print(file.describe()) #Description of DataFrame
                print(file.info) #Information about the DataFrame including metadata
                print()
                print()

            elif dchoice == 6:
                #Program to add a new column
                print()
                print()
                ncne = str(input('Enter the Name of Column: '))
                #Vairable storing the name of new column
                num1 = len(file.index)
                listval = []
                for i in range(num1):
                    val = str(input('Enter the Value: ')) #Variable asking the user to insert values of the the corresponding records in the column
                    listval.append(val)
                file[ncne] = listval
                #Creating the new column in dataframe
                print(file)
                print()
                print()

            elif dchoice == 7:

                #Program to add a new row in the Data Frame
                print()
                print()
                x = len(file.columns)
                print(file)
                addr = []
                for i in range(x):
                    rval = eval(input('Enter the Value: ')) #Variable asking the user to input values of the records
                    addr.append(rval)
                newin = len(file.index) #Variable telling us the value of the total number of records in the Dataframe
                file.loc[newin+1] = addr #As the record is to be added at the end, newin + 1 will be the place and added using loc
                print(file) #Printing the new dataframe with the added record
                print()
                print()

            elif dchoice == 8:

                #Program to Delete a column or specific columns from the existing dataframe
                print()
                print()
                print('Deleting Column...')
                print()
                print('''Welcome to Deleting Columns...''')
                print()
                time.sleep(0.5)
                print()

                #Asking the user that if he/she wants to delete just a single column or multiple columns..
                print('''
Press 1 : TO DELETE SINGLE COLUMN
Press 2 : TO DELETE MULTIPLE COLUMNS''')
                time.sleep(1)
                print()
                print()
                delcolc = int(input('Enter Your choice: ')) #Variable storing the number choice of deletion of columns.
                if delcolc == 1:
                    print(file.columns)
                    #If user chooses 1, single column will be deleted as per user
                    delcol1 = str(input('Enter the Name: '))#Variable storing the single column to be deleted
                    file = file.drop(delcol1, axis = 1) # Hashtag 1 statement of deletion of single column
                if delcolc == 2:
                    print(file.columns)
                    #If user chooses 2, multiple columns will be deleted as per user.
                    print()
                    print('How many Columns do you want to delete?: ') # Statement Asking the user the number of columns to be deleted.
                    print()
                    time.sleep(0.5)
                    print()
                    delcolcn = int(input('How many?: ')) #The variable of the previous statement
                    delcolcl = []
                    for i in range(delcolcn):
                        delcolcv = str(input('Enter the Name: '))
                        delcolcl.append(delcolcv)
                    file = file.drop(delcolcl, axis = 1) # Hashtag 2 statement of deletion of multiple columns..


            elif dchoice == 9:

                #Deleting a specfic record
                print()
                print()
                print('Deleting Records...')
                print(file.index)
                rdel = eval(input('Enter the name of record to be deleted: '))
                file=file.drop(rdel)
                print(file)
                print()
                print()

            elif dchoice == 10:
                print()
                print()
                print('Printing the Highest Work Experience')
                print()
                column = file['EXP']
                print(column.max())
                print()
                print()
                                
                

            elif dchoice == 11:
                print()
                print()
                print('Printing all the Records')
                print(file.values)
                print()
                print(file)
                print()

            elif dchoice > 11:
                print('Going back to main menu...')
                break


    elif choice == 3:
        print()
        print()
        time.sleep(1)
        print('                                                                     WELCOME TO DATA VISUALISATION                                                                       ')
        print()
        print()
        time.sleep(1)

        while True:
            print()
            print()
            print('DATA VISUALISATION')
            print('''
1. Plot a Line Graph
2. Plot a Bar Graph
3. Plot a Histogram

Enter any digit greater than 3 to go back to main menu...''')
            
            vchoice = int(input('Enter the Number Preceeding your choice: '))

            if vchoice == 1:

                print()
                print()
                print('Plotting Line Graph')
                time.sleep(1)
                print()
                print()
                
                
                time.sleep(0.5)
                z = file.columns
                print(z)

                
                pltlx = str(input('What do you want on X Axis? (Only 1 column accepted): '))
                if pltlx in z:
                    pltlyn = int(input('How many items do you want on Y-Axis: '))
                    pltlynlist = []
                    for i in range(pltlyn):
                        pltly = str(input('Enter the Name of Column: '))
                        pltlynlist.append(pltly)
                else:
                    print('The column you entered is wrong')

                plt.figure(figsize = (20, 20))
                #figure(figsize=(8, 6), dpi=80)
                plt.plot(file[pltlx], file[pltlynlist])

                gh = np.arange(len(file[pltlx]))                                

                plt.xticks(gh, file[pltlx], rotation = 80)
                plt.xlabel('X-Axis')
                plt.ylabel('Y-Axis')
                

                plt.show()

                

            elif vchoice == 2:
                 print()
                 print()
                 print('Plotting Bar Graph')
                 time.sleep(1)
                 print()
                 print()

                 time.sleep(0.5)
                 print('Column names: ', file.columns)

                 pltbx = str(input('Enter the Name of the Column on X-Axis: '))
                 pltbyn = int(input('How many parameters on Y-Axis?: '))

                 pltbylist = []
                 
                 for i in range(pltbyn):
                     pltby = str(input('Enter the Y-Axis column(s): '))
                     pltbylist.append(pltby)

                 file.plot(kind = 'bar', x = pltbx, y = pltbylist)
                 gh = np.arange(len(file[pltbx]))                                

                 plt.xticks(gh, file[pltbx], rotation = 80)

                 
                 plt.xlabel('X-Axis: Employee Name')
                 plt.ylabel('Y-Axis: Money')
                 plt.legend()

                 plt.show()


            elif vchoice == 3:

                time.sleep(0.5)
                
                print()
                print()
                print('Plotting Histogram')
                print()
                print()

                print('''
Press 1: To plot Histogram of Numeric columns of your choice in the table
Press 2: To plot Histogram of all Numeric columns in the DataFrame''')

                hchoice = int(input('Enter the number preceeding your choice: '))

                if hchoice == 1:

                    print()
                    print()

                    time.sleep(0.5)
                    print('The Columns: ', file.columns)

                    print()
                    print()

                    damn = str(input('Enter the Column you wish to see on X-Axis: '))
                    print()

                    plt.hist(x = file[damn])

                    plt.xticks(rotation = 90)
                    plt.title('HISTOGRAM')
                    plt.xlabel('X-Axis')
                    plt.ylabel('Y-Axis')

                    plt.show()


                elif hchoice == 2:
                    print()
                    print()

                    time.sleep(ns)

                    print('Printing the Histogram of all numeric columns..')

                    print()

                    file.hist(grid = False)
                    plt.xticks(rotation = 90)

                    plt.show()

                
                    
                    

            elif vchoice > 3:
                break
            
                
             
                        

    elif choice == 4:
        print()
        print()
        time.sleep(0.5)
        print('--------------------------------------|CREDITS|-----------------------------------------------')
        time.sleep(0.5)
        print('Submitted to: Mrs. Mona Batra, PGT Computer Science')
        time.sleep(0.5)
        print('Completiton Date: 31 August 2021')
        time.sleep(0.5)
        print('Completion By: Arihant Gupta and Ashutosh Asthana')
        time.sleep(0.5)
        print('Principal of the School: Mrs Ruchika Sharma')
        time.sleep(0.5)
        print()
        print()
        


    elif choice == 5:
        print()
        print()
        time.sleep(0.5)
        print()

        while True:
            print('''Press number according to your preferred action:
1. Read the Synopsis
2. Listen to the Synopsis
3. Download the Synopsis file as Word File

Enter any number greater than 3, to go back to main menu.''')
            print()
            schoice = int(input('Enter the number preeceding your choice: '))

            if schoice == 1:
                print()
                print()

                
                print('                                                        PROJECT SYNOPSIS                                                  ')
                print('''
Using our knowledge of Python, and the modules pandas, matplotlib, numpy, etc; we have created a program, which performs Data Analysis like displaying specific records and columns,
addition and deletion of columns and records, and Data Visualisation via plotting Line and Bar graphs along with histogram. We have used functions like head(), tail(), loc[], iloc[],
drop in Data Analysis. In data visualisation we have plotted graphs with the help of the matplotlib library of python mainly using its 'pyplot' module. We have also added some extra
features also like text-to-speech and delaying the code execution so as to shape the program in a more interactive manner. The whole program is Menu driven and totally user input based,
the analysis and visualisation that is being performed is strictly according to what the user is entering. The programming for this Project has been done by Arihant Gupta and
Ashutosh Asthana. We have used IDLE Python 3.9.6 version to write the program and execute it as well.''')
                print()
                print()
                print('Thank You')

            elif schoice == 2:
                print()
                print()

                
                print('                                                        PROJECT SYNOPSIS                                                  ')
                speak('''
Using our knowledge of Python, and the modules pandas, matplotlib, numpy, etc; we have created a program, which performs Data Analysis like displaying specific records and columns,
addition and deletion of columns and records, and Data Visualisation via plotting Line and Bar graphs along with histogram. We have used functions like head(), tail(), loc[], iloc[],
drop in Data Analysis. In data visualisation we have plotted graphs with the help of the matplotlib library of python mainly using its 'pyplot' module. We have also added some extra
features also like text-to-speech and delaying the code execution so as to shape the program in a more interactive manner. The whole program is Menu driven and totally user input based,
the analysis and visualisation that is being performed is strictly according to what the user is entering. The programming for this Project has been done by Arihant Gupta and
Ashutosh Asthana. We have used IDLE Python 3.9.6 version to write the program and execute it as well.''')
                print()
                print()
                speak('Thank You')


            elif schoice == 3:
                print('The File')
                wb.open('https://docs.google.com/document/d/1MfjNP111QsPKxUbK7WS0vVIpXCJEFHacvELa8J5Hj9o/edit?usp=sharing')


            elif schoice > 3:
                
                break
          

        
        

    

    elif choice > 5:
        break

    


                
            




                
                 
             
             

        
