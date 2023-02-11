

class chapterFour:
    
    def fourone():
        
        #explain to user
        print('This program has a secret number and you will try to guess its number.')
        #create secret number
        secret = 7
        #get user input to guess
        guess = 0
        #loop to allow for multiple guesses
        while guess != 100:
            guess = int(input("Enter a number between 1 and 10| Enter 100 to end the program: "))
            
            #guess structure
            if guess <= 10:
                if guess == secret:
                    print("Just right!")
                elif guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")
        
    
    def fourtwo():
        
        
        #initalize
        small = False
        green = False
        
        #explain to user
        print("This program will evaluate if an object is small, and or green.")
        #get user input
        check = ''
        
        #allow for multiple checks
        while check.lower() != 'done':
            
            #change boolean flags if/else structure
            check = str(input("Enter Cherry, Pea, Watermelon, or Punpkin| enter done to exit: "))
            if check.lower() == 'cherry':
                small = True
                green = False
            if check.lower() == 'pea':
                small = True
                green = True
            if check.lower() == 'watermelon':
                small = False
                green = True
            if check.lower() == 'pumpkin':
                small = False
                green = False
                
                #ensure not printing excess, and print results
            if check.lower() == 'cherry' or check.lower() == 'pea' or check.lower() == 'watermelon' or check.lower() == 'pumpkin':
                if small == True:
                    print("A " + check + ' is small.')
                else:
                    print("A " + check + ' is big.')
                if green == True:
                    print("A " + check + ' is green.')
                else:
                    print("A " + check + ' is not green.')
                
                
    def sixone():
        
        #initalize array
        array = [3,2,1,0]
        count = 0
        #explain to user
        print("This function prints a series of values using a for loop.")
        
        #create loop
        for len in array:
            
            print(str(array[count]))
            count += 1
        print("Program Complete!")
        
            
        
    def sixtwo():
        print('This program has a secret number, guess its own number using a while loop.')
        #create number
        guess_me = 7
        #get user input to guess
        number = 1
        #loop to allow for multiple guesses
            
            #guess structure
        while number != 7:
                print('Trying... ' + str(number))
                if number < guess_me:
                    print('too low!')
                elif number > guess_me:
                    break
                number += 1
                
        if number > 7:
            print('trying...' + str(number))
            print('oops')
        else:
            print('trying...' + str(number))
            print('found it!')
            
                    
                
    def sixthree():
        print('This program has a secret number, guess its own number using a for loop.')
        #create number
        guess_me = 5
        #get user input to guess
        number = 1
        #loop to allow for multiple guesses
            
            #guess structure
        for number in range(10):
                print('Trying... ' + str(number))
                if number < guess_me:
                    print('too low!')
                elif number == guess_me:
                    print('found it!')
                    break
                elif number > guess_me:
                    break
                



if __name__ == '__main__':
   start = chapterFour
   function = str(input('Enter fourone for 4.1, fourtwo for 4.2, same for 6.1, 6.2, 6.3: '))
   
   if function.lower() == 'fourone':
       print("------------------------")
       start.fourone()
   if function.lower() == 'fourtwo':
       print("------------------------")
       start.fourtwo()
   if function.lower() == 'sixone':
       print("------------------------")
       start.sixone()
   if function.lower() == 'sixtwo':
       print("------------------------")
       start.sixtwo()
   if function.lower() == 'sixthree':
       print("------------------------")
       start.sixthree()