#Drashaun Morrow
#This program completes exercises 13.1-13.3. Getting the date, saving it to a file then parsing through the file to print the date.

from datetime import date
import datetime


class thirteen():
    
    def assignment():
        
        
        now = date.today()
        
        saveDate = open("today.txt", 'w')
        saveDate.write(str(now))
        
        saveDate.close()
        print("This program has created the current date, and saved it to today.txt")
        
        cont = input("Enter yes to continue: ")
        if cont.lower() == 'yes':
            with open("today.txt",'r') as data_file:
                for line in data_file:
                    today_string = line
                    
        
                todays_date = datetime.datetime.strptime(today_string, '%Y-%m-%d')
                datetuple = todays_date.timetuple()[:3]
                
                some_day = datetime.date(*datetuple)
                fmt = "It's %A, %B %d, %Y"
                today_string = some_day.strftime(fmt)
                
                print(today_string)
                        
                        
                saveDate.close()
        
if __name__ == '__main__':
    start = thirteen
    start.assignment()