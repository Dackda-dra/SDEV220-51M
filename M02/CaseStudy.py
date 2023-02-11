#Author: Drashaun Morrow
#Filename: CaseStudy
#Description: This app will take a students first name, last name
# and GPA into a list and display whether they have made the Honor Roll, 
# or Dean's list, or Neither.




#imports
import tkinter as tk
import tkinter.messagebox

# create global variables
studentFirstName = []
studentLastName = []
studentGPA = []
studentPlace = []

class caseStudy():
    
    
    def studentInfo(self):
        
        #create window
        self.infoWindow = tk.Tk()
        self.infoWindow.title('Student Placement')
        #create frames
        firstNameFrame = tk.Frame(self.infoWindow)
        lastNameFrame  = tk.Frame(self.infoWindow)
        gpaFrame  = tk.Frame(self.infoWindow)
        infoButtonFrame  = tk.Frame(self.infoWindow)
        
        #create widgets----- First Name
        firstNamePrompt = tk.Label(firstNameFrame,
                                    text='Students first name: ')
        self.getFirstName = tk.Entry(firstNameFrame,
                                        width=10,
                                        borderwidth=1,
                                        relief='solid')
        #pack
        firstNamePrompt.pack(side='left')
        self.getFirstName.pack(side='right')
        # Last Name -----------------------------------------
        lastNamePrompt = tk.Label(lastNameFrame,
                                    text='Students last name: ')
        self.getLastName = tk.Entry(lastNameFrame,
                                        width=10,
                                        borderwidth=1,
                                        relief='solid')
        #pack
        lastNamePrompt.pack(side='left')
        self.getLastName.pack(side='right')
        # GPA ------------------------------------------
        gpaPrompt = tk.Label(gpaFrame,
                                    text='          Students GPA: ')
        self.getGPA = tk.Entry(gpaFrame,
                                        width=10, 
                                        borderwidth=1,
                                        relief='solid')
        #pack
        self.getGPA.insert(0, '0.0')
        gpaPrompt.pack(side='left')
        self.getGPA.pack(side='right')
        
        # Buttons ---------------------------------------
        addButton = tk.Button(infoButtonFrame,
                                 text='Save',
                                 command=self.processInfo)
        quitButton = tk.Button(infoButtonFrame,
                                    text='Done',
                                    command=self.displayInfo)
        #pack
        addButton.pack(side='left')
        quitButton.pack(side='right')
        #--------------------------------------------------
        
        
        #pack frames
        lastNameFrame.pack()
        firstNameFrame.pack()
        gpaFrame.pack()
        infoButtonFrame.pack()
        
        #loop
        
        tk.mainloop()
        
        #insert float into text
        
        
        
    def processInfo(self):
        
        
        #get inputs
        studentLastNameLocal = str(self.getLastName.get())
        studentFirstNameLocal = str(self.getFirstName.get())
        studentGPALocal = float(self.getGPA.get())
        studentPlaceLocal = ''
        
        
        
        # destroy command flag
        if studentLastNameLocal.upper() == 'ZZZ':
            self.infoWindow.destroy()
            studentLastNameLocal = ' '
            studentFirstNameLocal = ' '
            studentGPALocal = 0
            studentPlaceLocal = 'End of List'
            
        # Calculate placement
        if studentGPALocal < 3.25:
            studentPlaceLocal = 'None'
        elif studentGPALocal >= 3.25 and studentGPALocal < 3.5:
            studentPlaceLocal= 'Honor Roll'
        else:
            studentPlaceLocal = 'Deans List'
            
        # add to lists
        studentLastName.append(studentLastNameLocal)
        studentFirstName.append(studentFirstNameLocal)
        studentGPA.append(studentGPALocal)
        studentPlace.append(studentPlaceLocal)
        
        # provide feedback to user
        tk.messagebox.showinfo('',studentLastNameLocal + ' ' + studentFirstNameLocal + ' has been added.')
        
        
    
    def displayInfo(self):
        self.infoWindow.destroy()
        #create window
        placementWindow = tk.Tk()
        placementWindow.title('Students Placement')
        
        #create scroll
        placementScroll = tk.Scrollbar(placementWindow, orient='vertical')
        #create listbox and scrollcmd
        placementBox = tk.Listbox(placementWindow, height='10', width='20', yscrollcommand=placementScroll.set)
        placementScroll.config(command=placementBox.yview)
        placementBox.pack(fill='both',
                          expand='1')
        
        #create exit frame and button
        quitFrame = tk.Frame(placementWindow)
        doneButton = tk.Button(quitFrame,
                                  text='Done',
                                command=placementWindow.destroy)
        doneButton.pack()
        quitFrame.pack()                            
        #-------------------------------------------------
        # insert information into listbox
        
        insertInfo = ['','','','']
        count = 0
        
        for len in studentLastName:
            insertInfo[0] = studentLastName[count]
            insertInfo[1] = studentFirstName[count]
            insertInfo[2] = studentGPA[count]
            insertInfo[3] = studentPlace[count]
            insertInfoList = str(insertInfo[0] + ' ' + str(insertInfo[1]) + ' ' + str(insertInfo[2]) + ' ' + str(insertInfo[3]))
            placementBox.insert('end',insertInfoList)
            count = count + 1
            
        
            
        
    
    
    
    
    
if __name__ == '__main__':
    start = caseStudy()
    start.studentInfo()