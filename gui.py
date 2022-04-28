from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.name_var = StringVar()
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name, textvariable=self.name_var)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.

        self.frame_age = Frame(self.window)
        self.age_var = StringVar()
        self.label_age = Label(self.frame_age, text ="Age")
        self.entry_age = Entry(self.frame_age, textvariable=self.age_var)
        self.label_age.pack(padx=5, side="left")
        self.entry_age.pack(padx=17, side="left")
        self.frame_age.pack(anchor="w", pady=10)


        self.frame_status = Frame(self.window)
        self.radioVar = IntVar()
        self.radioVar.set(-1)
        self.label_status = Label(self.frame_status, text="Status")
        self.radio_student = Radiobutton(self.frame_status, text="Student", variable=self.radioVar, value=0)
        self.radio_staff = Radiobutton(self.frame_status, text="Staff", variable=self.radioVar, value=1)
        self.radio_both = Radiobutton(self.frame_status, text="Both", variable=self.radioVar, value=2)
        self.label_status.pack(side="left")
        self.radio_student.pack(side="left")
        self.radio_staff.pack(side="left")
        self.radio_both.pack(side="left")
        self.frame_status.pack(anchor="w", pady=10)

        self.frame_save = Frame(self.window)
        self.save_button = Button(self.frame_save, text="SAVE", command=self.clicked)
        self.save_button.pack()
        self.frame_save.pack(anchor="n")

    def clicked(self):
        """
        - This method should only be called when the save button is clicked.
        - Retrieve the name, age, and status values.
        - The age must be doubled (e.g. if someone entered 5 for age, their age would be stored as 10).
        - Determine the person status based off the value of the radio button selected.

        - Open the records.csv file and append the new person's details.
        - I suggest first viewing the csv file's contents to understand how your data should be sent to it.

        - Clear the name and age values that were entered in the GUI.
        - Make sure you clear the status value (i.e, No status value should be selected).
        """
        
        # gets the variables and outputs an error to the CSV if a text value is inputted for age
        try:
            age = int(self.entry_age.get()) * 2
        
            name = self.entry_name.get()
            if self.radioVar.get() == 0:
                type = "Student"
            elif self.radioVar.get() == 1:
                type = "Teacher"
            elif self.radioVar.get() == 2:
                type = "Both"
            else:
                type = "N/A"
        
            # opens the file for writing and writes the proper lines
            with open(r"records.csv", "a+") as self.recordCSV:
                reader = csv.reader(self.recordCSV)
                for row in reader:
                    print(row)
            
                writer = csv.writer(self.recordCSV)
                writer.writerow([name, age, type])
        
            # resets the input boxes and radio buttons
        
            self.age_var.set("")
        
            self.name_var.set("")
            self.radioVar.set(-1)
        
        except ValueError:
            self.age_var.set("Invalid Age")