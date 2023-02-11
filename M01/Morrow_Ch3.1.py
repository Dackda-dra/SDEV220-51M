# Chapter 3 Assignment 1
#utilizing Python 3.8.10


#create class
class ChapterThree():
    
    #create first function
    def secondsInHour(self):
        #define program
        print("This program will find out how many seconds are in an Hour")
        #assign variables
        hour = 60
        minute = 60
        self.seconds = hour * minute
        #explain process to user
        print("Each hour has 60 minutes, and each minute has 60 seconds")
        print("Take the minutes of an hour times the seconds of a minute")
        print("60 * 60")
        #print result
        print("There are: " + str(self.seconds) + " seconds in an hour.")
        
        #user prompt to next function
        continuePrompt = input("Enter 1 to continue, 0 to stop. : ")
        #create call to next function
        if continuePrompt == '1':
            self.secondsPerDay()
            
    #function 2
    def secondsPerDay(self):
        #seperate console
        print("-------------------------------------------------")
        #3.2
        self.seconds_per_hour = self.seconds
        #explain to user
        print("To find the number of seconds in a day.")
        print("Take the seconds per hour, times the number of hours in a day.")
        #define hours in a day
        hoursInDay = 24
        #calculate seconds in a day #3.3, #3.4
        self.seconds_per_day = self.seconds_per_hour * hoursInDay
        #print result
        print("There are: " + str(self.seconds_per_day) + " seconds in a day.")
        
        #user prompt to next function
        continuePrompt = input("Enter 1 to continue, 0 to stop. : ")
        #create call to next
        if continuePrompt =='1':
            self.checkwork()
            
    #function 3
    def checkwork(self):
        #seperate console
        print("------------------------------------------------")
        #explain to user
        print("Now we will make sure our numbers are correct by dividing.")
        print("We will divide seconds per day, by seconds per hour.")
        print("1. will be division by float, 2 will be division by interger ")
        #calculate #3.5, #3.6
        secondsCheck1 = self.seconds_per_day/self.seconds_per_hour
        secondsCheck2 = self.seconds_per_day//self.seconds_per_hour
        #print results
        print("1. " + str(secondsCheck1))
        print("2. " + str(secondsCheck2))
        
        endPrompt = input("Do the two numbers match?: ")
        if str(endPrompt).lower() != "yes":
            escape = ""
            while escape != "yes":
                escape = input("Aside from the .0?: ")
        
        
        print("Program Complete")
        
           
        
    
    
if __name__ == '__main__':
    Start = ChapterThree()
    Start.secondsInHour()

