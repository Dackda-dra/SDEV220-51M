# Drashaun Morrow
# Programming assignments 7.4-7.7  -- 9.1,9.2
# 7.4 will execute consecutively


class homework ():
    
  
    #create function
    def sevenfour(self):
        #create lists to be used in all functions
       self.things = ['mozarella', 'cinderella','salmonella' ]
       print(self.things)
       
       continuePrompt = input('Enter 1 to continue, 0 to stop: ')
       if continuePrompt == '1':
           print('---------------------')
           start.sevenfive()
          
    def sevenfive(self):
        #capitalize
        self.things[1] = self.things[1].capitalize()
        print(self.things)
        print('The element did change.')
        
        continuePrompt = input('Enter 1 to continue, 0 to stop: ')
        if continuePrompt == '1':
            print('---------------------')
            start.sevensix()
        
        
    def sevensix(self):
        #utilize .upper function
        self.things[0] = self.things[0].upper()
        self.things[2] = self.things[2].upper()
        print(self.things)
        
        continuePrompt = input('Enter 1 to continue, 0 to stop: ')
        if continuePrompt == '1':
            print('---------------------')
            start.sevenseven()
        
    def sevenseven(self):
        #utilize del function
        del self.things[2]
        print(self.things)
        print('====<Nobel Prize>====')
    
       
    
    def good():
        print('-----------------------')
        alist = ['Harry','Ron','Hermione']
        print(alist)
        
        
        
        
        
        
    


# new class for generator
class ninetwo():
    
    #create nest for two functions
    def assignment():
        
        #create generator
        def get_odds(first=1, last=10, step=2):
            number = first
            while number < last:
                yield number
                number += step
        #assign generator
        ranger = get_odds(1,10)
        #assign count to get third value
        count = 0
        for x in ranger:
            
            if count == 2:
                print(x)
            count = count + 1
        

if __name__ == '__main__':
    start = homework()
    start2 = homework
    start3 = ninetwo
    choice = input('Enter sevenfour for 7.4-7.7, or nineone for 9.1, and ninetwo for 9.2: ')
    
    if choice.lower() == 'sevenfour':    
             start.sevenfour()
    elif choice.lower() == 'nineone':
             start2.good()
    elif choice.lower() == 'ninetwo':
            start3.assignment()
            
          
                
         
     
print('Program Complete')