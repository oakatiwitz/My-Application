from tkinter import Tk, filedialog, StringVar, END
import tkinter.messagebox as messagebox
import customtkinter
import openpyxl
import PyPDF2
import os
import time
import pyautogui
import pytesseract
from PIL import ImageGrab, Image
from pytesseract import Output
import pandas as pd

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
#pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\tesseract.exe")


# Create CTk window
root = customtkinter.CTk()
root.title("EAZY")

# Setting up theme of your app
customtkinter.set_appearance_mode("dark")

# Setting up theme of your component
customtkinter.set_default_color_theme("green")

# Change the window icon
root.wm_iconbitmap("EAZY.ico")

# Set the window size
root.geometry("600x400")

# Set the window to not be resizable
root.resizable(width=False, height=False)

# Always on top
root.wm_attributes("-topmost", 1)

# Frame 
option_frame = customtkinter.CTkFrame(master=root,
                               width=150,
                               height=400,
                               fg_color = "#3E3E3E",
                               corner_radius= 0)
option_frame.pack(side = 'left')

main_frame = customtkinter.CTkFrame(master=root,
                               width=400,
                               height= 375,
                               fg_color = "#3E3E3E",
                               corner_radius= 7)
main_frame.place(relx=0.625, rely=0.5, anchor = 'center')

pic_frame = customtkinter.CTkFrame(master = main_frame, width=400, height= 375, fg_color= '#585858', corner_radius=7)
pic_frame.place(relx = 0.5, rely = 0.5, anchor = 'center')

# Background ##############################################
# Load the image file
image = customtkinter.CTkImage(Image.open("EAZY.png"), size=(100,100))

# Create a label widget with the image as the background
label = customtkinter.CTkLabel(master= pic_frame, image=image, text='')

# Set the size of the label to match the size of the image
label.place(relx = 0.5, rely = 0.35, anchor = 'center')

label2 = customtkinter.CTkLabel(pic_frame, font=('Arial', 60, 'bold' ,'italic'),text="E  A  Z  Y ",fg_color = "#585858",
                                bg_color="#3E3E3E", text_color= 'white')
label2.place(relx = 0.5, rely = 0.7, anchor ='center')

label3 = customtkinter.CTkLabel(pic_frame, font=('Arial', 12.5),text="Laziness makes things Easier",fg_color = "#585858",
                                bg_color="#585858", text_color= 'white')
label3.place(relx = 0.5, rely = 0.85, anchor ='center')
###########################################################

# Switch Page Function
def Home_page():
    # Create Frame
    pic_frame = customtkinter.CTkFrame(master = main_frame, width=400, height= 375, fg_color= '#585858', corner_radius=7)
    pic_frame.place(relx = 0.5, rely = 0.5, anchor = 'center')
    
    # Load the image file
    image = customtkinter.CTkImage(Image.open("EAZY.png"), size=(100,100))

    # Create a label widget with the image as the background
    label = customtkinter.CTkLabel(master= pic_frame, image=image, text='')

    # Set the size of the label to match the size of the image
    label.place(relx = 0.5, rely = 0.35, anchor = 'center')

    label2 = customtkinter.CTkLabel(pic_frame, font=('Arial', 60, 'bold' ,'italic'),text="E  A  Z  Y ",fg_color = "#585858",
                                    bg_color="#3E3E3E", text_color= 'white')
    label2.place(relx = 0.5, rely = 0.7, anchor ='center')

    label3 = customtkinter.CTkLabel(pic_frame, font=('Arial', 12.5),text="Laziness makes things Easier",fg_color = "#585858",
                                    bg_color="#585858", text_color= 'white')
    label3.place(relx = 0.5, rely = 0.85, anchor ='center')
    
def S2oE_page():
    # ADD Label
    label = customtkinter.CTkLabel(main_frame, font=('Arial', 30),text="S2oE BITLIST",fg_color = "#3E3E3E",
                                bg_color="#3E3E3E")

    label.place(relx=0.5, rely=0.12 , anchor='center')

    label2 = customtkinter.CTkLabel(main_frame, font=('Arial', 17.5),text="Data File(.wt2)",fg_color = "#3E3E3E",
                                    bg_color="#3E3E3E")

    label2.place(relx=0.18, rely=0.3, anchor='center')

    label3 = customtkinter.CTkLabel(main_frame, font=('Arial', 17.5),text="Excel File",fg_color = "#3E3E3E",
                                    bg_color="#3E3E3E")

    label3.place(relx=0.17, rely=0.5, anchor='center')

    # Button function
    def browse_button():
        # Allow user to select a directory and store it in global var
        # called folder_path
        global folder_path2, file_path2, Name

        filename2 = filedialog.askopenfilename()
        folder_path2.set(filename2)

        # Select only filename 
        name = filename2.split('/')[-1]
        print('filename: ', filename2)
        print('name :', name)

        # Update the Entry widget with the selected file's path
        entry.delete(0, END)
        entry.insert(0, name)
        file_path2 = filename2
        print("file_path: ", file_path2)
        #locat = file_path2.split('/')[0:-1]
        #locatw = '/'.join(locat)
        #Name = name[:-3]
        Name = file_path2[:-3]
        print(Name)
    
    def readWT2(_filename, name):
        global file_path2
        f = open(_filename)
        nonvital = False
        session = False
        session_num = 0
        input = False
        output = False
        # Create First column that is the name of each row 
        total_session_variable = {'NUMBER':['I-' + str(i) for i in range(1,257)]}
        total_session_variable['NUMBER'].extend(['C-' + str(i) for i in range(1,257)])
        current_session = ""
        excel_name = name+'xlsx'
        writer = pd.ExcelWriter(excel_name, engine='xlsxwriter')
        for line in f:

            # Checking they have non vital port
            if 'NON VITAL NETWORK PORT' in line:
                # Set State of nonvital
                nonvital = True

            # Checking for WSA S2 SERVER
            if nonvital and 'WSA_S2_SERVER' in line:
                # Set they have session
                session = True
                # Count number of session
                session_num += 1
                # Current session number 
                current_session = line[13:]
                current_session = current_session[:-25]
                # Set the session number in total_session_variable
                Name = "session " + current_session
                total_session_variable[Name] = [""]*512
                
            # Checking they have INPUT STATE
            if session and 'INPUT_STATE' in line:
                # Set they have INPUT STATE
                input = True
                # Current INPUT STATE number ([:-1] means delete '\n')
                current_INPUT_STATE = line[19:-1]
                
            # Add Mnemonics inside the line that contains 'NAME' 
            if input and ' NAME ' in line:
                # Save the Mnemonics name 
                text_input = line[17:-2]
                # Add the Mnemonics in the current session in dict total_session_variable
                total_session_variable[Name][int(current_INPUT_STATE)+255] = text_input
                    
            # Checking they have OUTPUT STATE
            if session and 'OUTPUT_STATE' in line:
                # Set they have OUTPUT STATE 
                output = True 
                # Current OUTPUT STATE number ([:-1] means delete '\n')
                current_OUTPUT_STATE = line[20:-1]
                
            # Add Mnemonics inside the line that contains 'NAME' 
            if output and ' NAME ' in line:
                # Save the Mnemonics name 
                text_output = line[17:-2]
                # Add the Mnemonics in the current session in dict total_session_variable
                total_session_variable[Name][int(current_OUTPUT_STATE)-1] = text_output
                
            # Check for END SESSION 
            if session and 'END SESSION' in line:
                # Clear the session
                session = False
                # Clear the INPUT STATE
                input = False
                # Clea the OUTPUT STATE
                output = False

                # Create excel file 
                df = pd.DataFrame(total_session_variable)
                df.to_excel(writer, index=False)

        writer.close()
        file_path2 = ''
        if session_num != 0:
            # show alert
            messagebox.showinfo("COMMAND", 'S2 BITLIST Created')

            # Create a yes/no message box
            result = messagebox.askyesno("Question", "Do you want to open the excel file?")
        
            if result:
                # user clicked "yes"
                print("User clicked Yes")
                open_file(excel_name)

            else:
                # user clicked "no"
                print("User clicked No")
        else:
            # show alert
            messagebox.showinfo("COMMAND", 'Non-Vital Session Not Found')

    def create_button():
        if len(file_path2) == 0:
            # Show alert
            messagebox.showinfo("COMMAND", 'Please select your file.')
        else:
            readWT2(file_path2, Name)
    
    def open_file(Oname):
        print('processing')
        
        # Open the selected application
        os.startfile(Oname)

    # Create an Entry widget for browse with customized appearance (wt2 file)
    entry = customtkinter.CTkEntry(main_frame,
                                    width=150,
                                    height=25,
                                    border_width=2,
                                    bg_color="#3E3E3E",
                                    corner_radius=10)
    entry.place(relx=0.53, rely=0.3, anchor='center')

    # Create the "Browse" button
    browsebutton = customtkinter.CTkButton(main_frame, text="Browse",
                                            width=80,
                                            height=32,
                                            bg_color="#3E3E3E",
                                            fg_color='#3E3E3E',
                                            border_width = 2,
                                            command= browse_button)
    browsebutton.place(relx=0.85, rely=0.3, anchor='center')

    # Create the "CONVERT" button
    createbutton = customtkinter.CTkButton(main_frame, text="CONVERT",font=("Arial", 15),
                                            width=80,
                                            height=32,
                                            bg_color="#3E3E3E",
                                            command = create_button)
    createbutton.place(relx=0.47, rely=0.5, anchor='center')

def PDF_page():

    # ADD Label
    label = customtkinter.CTkLabel(main_frame, font=('Arial', 30),text="PDF to Excel",fg_color = "#3E3E3E",
                                bg_color="#3E3E3E")

    label.place(relx=0.5, rely=0.12 , anchor='center')

    label2 = customtkinter.CTkLabel(main_frame, font=('Arial', 17.5),text="PDF File",fg_color = "#3E3E3E",
                                    bg_color="#3E3E3E")

    label2.place(relx=0.11, rely=0.3, anchor='center')

    label3 = customtkinter.CTkLabel(main_frame, font=('Arial', 17.5),text="Keyword",fg_color = "#3E3E3E",
                                    bg_color="#3E3E3E")

    label3.place(relx=0.11, rely=0.5, anchor='center')

    label4 = customtkinter.CTkLabel(main_frame, font=('Arial', 17.5),text="Excel File",fg_color = "#3E3E3E",
                                    bg_color="#3E3E3E")

    label4.place(relx=0.11, rely=0.7, anchor='center')

    # Main Function
    def ReadPDF(name, Keyword):
        # Create empty list
        T = []

        # Open the PDF file in read-only mode
        with open(name, 'rb') as file:
            # Create a PDF object
            pdf = PyPDF2.PdfReader(file)

            # Get the number of pages in the PDF
            num_pages = len(pdf.pages)

            # Iterate through the pages
            for i in range(num_pages):
                # Get the page object
                page = pdf.pages[i]

                # Extract the text from the page
                text = page.extract_text()

                # Split the text into lines
                lines = text.split("\n")

                # Iterate through the lines
                for line in lines:

                    # Search for the specific text in the line
                    if Keyword in line:
                        if ' L ' in line:
                            line = line.replace(' L ', ' ')
                        line = line.split(' ')
                        line = line[1:]
                        line = ''.join(line)
                        T.append(line)
        # sort each line 
        T.sort()    

        # Create a new workbook
        workbook = openpyxl.Workbook()

        # Get the active worksheet
        worksheet = workbook.active

        # Iterate over the list and write the elements to the worksheet
        for row in T:
            worksheet.append([row])

        # Set global save name 
        global save_name
    
        # Create PATH to save
        save_name = name.split('/')
        save_name = save_name[0:-1]
        save_name = '/'.join(save_name)

        # Save the workbook
        save_name = save_name + '/'+ str(keyword)+ ' converted from PDF.xlsx'
        print(save_name)
        workbook.save(save_name)  

        # Show the alert
        messagebox.showinfo("COMMAND", "Done!")

        # Create a yes/no message box
        result = messagebox.askyesno("Question", "Do you want to open the excel file?")
        
        if result:
            # user clicked "yes"
            print("User clicked Yes")
            open_file(save_name)

        else:
            # user clicked "no"
            print("User clicked No")

    def open_file(Oname):
        print('processing')
        
        # Open the selected application
        os.startfile(Oname)

    # Button function
    def browse_button():
        # Allow user to select a directory and store it in global var
        # called folder_path
        global folder_path1, file_path

        filename = filedialog.askopenfilename()
        folder_path1.set(filename)

        # Select only filename 
        name = filename.split('/')[-1]
        print('filename: ', filename)
        print('name :', name)

        # Update the Entry widget with the selected file's path
        entry.delete(0, END)
        entry.insert(0, name)
        file_path = filename
        print("file_path: ", file_path)

    def keyword_button():
        global keyword 

        # Store the keyword from typed word 
        keyword = entry2.get()
        print(keyword)

        # Show the alert
        messagebox.showinfo("COMMAND", "Keyword is added!")

    def create_button():
        if len(file_path) == 0:
            #show alert 
            messagebox.showinfo("COMMAND", "Please select your file.")
        
        else:
            ReadPDF(file_path, keyword)

    # Create an Entry widget for browse with customized appearance (PDF)
    entry = customtkinter.CTkEntry(main_frame,
                                    width=200,
                                    height=25,
                                    border_width=2,
                                    bg_color="#3E3E3E",
                                    corner_radius=10)
    entry.place(relx=0.475, rely=0.3, anchor='center')

    # Create an Entry widget for browse with customized appearance (Keyword)
    entry2 = customtkinter.CTkEntry(main_frame,
                                    width=200,
                                    height=25,
                                    border_width=2,
                                    bg_color="#3E3E3E",
                                    corner_radius=10)
    entry2.place(relx=0.475, rely=0.5, anchor='center')

    # Create the "Browse" button
    browsebutton = customtkinter.CTkButton(main_frame, text="Browse",
                                            width=80,
                                            height=32,
                                            bg_color="#3E3E3E",
                                            fg_color='#3E3E3E',
                                            border_width = 2,
                                            command= browse_button)
    browsebutton.place(relx=0.85, rely=0.3, anchor='center')

    # Create the "Add" button
    addbutton = customtkinter.CTkButton(main_frame, text="Add",
                                        width=80,
                                        height=32,
                                        bg_color="#3E3E3E",
                                        fg_color='#3E3E3E',
                                        border_width = 2,
                                        command= keyword_button)
    addbutton.place(relx=0.85, rely=0.5, anchor='center')

    # Create the "CONVERT" button
    createbutton = customtkinter.CTkButton(main_frame, text="CONVERT",font=("Arial", 15),
                                            width=80,
                                            height=32,
                                            bg_color="#3E3E3E",
                                            command=create_button)
    createbutton.place(relx=0.35, rely=0.7, anchor='center') 

def Type_page():
    # ADD Label
    label = customtkinter.CTkLabel(main_frame, font=('Arial', 30),text="AUTOTYPING",fg_color = "#3E3E3E",
                                bg_color="#3E3E3E")

    label.place(relx=0.5, rely=0.12 , anchor='center')

    label2 = customtkinter.CTkLabel(main_frame, font=('Arial', 15),text="Select Mode",fg_color = "#3E3E3E",
                                bg_color="#3E3E3E")

    label2.place(relx=0.2, rely=0.3, anchor='center')

    label3 = customtkinter.CTkLabel(main_frame, font=('Arial', 15),text="Select Function",fg_color = "#3E3E3E",
                                bg_color="#3E3E3E")
    
    label3.place(relx=0.222, rely=0.5, anchor='center')

    # Main Function (Text)
    def extractData():
        # Collect the data 
        clipboard = customtkinter.CTk().clipboard_get()
        time.sleep(1)

        # Split data with \n then use the data except the last index and save it in list
        clipboard = clipboard.split('\n')[:-1]

        # Return List of data
        return clipboard

    # Main2 Function (Screenshot)
    def extractData2():
        screen =  ImageGrab.grabclipboard()  # screenshot
        cap = screen.convert('L')   # make grayscale
        data_text = pytesseract.image_to_string(cap)
        data = data_text.split('\n')
        lent = len(data)

        # Create empty list 
        data2 = []
        for j in range(lent):
            # Select only text and store in the list
            if len(data[j]) >= 1:
                data2.append(data[j])
        return data2

    # Typing Function (Housing Module)
    def typeData(_data):
        global State
        while State == False:
            # Show the alert
            messagebox.showinfo("COMMAND", "The process will start in 5 second")

            # Delay funtion
            time.sleep(5)

            # Typing the data
            for i in _data:
                if 'SPARE' not in i.upper():
                    pyautogui.typewrite(i)
                #pyautogui.press('down')
                pyautogui.press('enter')        
            print("Data Typed!")
            State = True

        # Show the alert
        messagebox.showinfo("COMMAND", "Done!")

        # Auto RESET after typed
        reset_operation()

    # Typing Function (MODBUS Register)
    def typeData2(_data):
        global State
        while State == False:
            # Show the alert
            messagebox.showinfo("COMMAND", "The process will start in 5 second")

            # Delay funtion
            time.sleep(5)

            # Count
            s = 0
            # Typing the data
            for i in _data:
                s += 1
                if 'SPARE' not in i.upper():
                    pyautogui.typewrite(i)
                pyautogui.press('down')

                # Ask for every typing 16 line
                if s%16 == 0 and s != len(_data):
                    messagebox.showinfo("COMMAND", "Select next register!")
                    time.sleep(5)

            
            print("Data Typed!")
            State = True

        # Show the alert
        messagebox.showinfo("COMMAND", "Done!")

        # Auto RESET after typed
        reset_operation()    

    # Define the button callback functions
    def start_operation():
        # Start the operation here
        print("Operation started")

        # Call Variable
        global mode_var, func_var 

        # Condition
        # For Module
        if  mode_var.get() == '1':
            if func_var.get() == '1':
                # Collect the data
                data = extractData() 
            
                # Show the alert
                messagebox.showinfo("COMMAND", "Save data from clipboard: Done!")

                # Typing
                typeData(data)

                # The operation is done
                print("Operation done")

            elif func_var.get() == '2':
                data2 = extractData2()

                # Show the alert
                messagebox.showinfo("COMMAND", "Save data from clipboard: Done!")

                # Typing the data
                typeData(data2)

                # The operation is done
                print("Operation done")

            else:
                # The operation is done
                print("Operation is interrupted")

                # Alert respone 
                messagebox.showinfo("COMMAND", "Please choose the types of functions!")

        # For Register
        elif mode_var.get() == '2':
            if func_var.get() == '1':
                # Collect the data
                data = extractData() 
    
                # Show the alert
                messagebox.showinfo("COMMAND", "Save data from clipboard: Done!")

                # Typing
                typeData2(data)

                # The operation is done
                print("Operation done")

            elif func_var.get() == '2':
                data2 = extractData2()

                # Show the alert
                messagebox.showinfo("COMMAND", "Save data from clipboard: Done!")

                # Typing the data
                typeData2(data2)

                # The operation is done
                print("Operation done")

            else:
                # The operation is done
                print("Operation is interrupted")

                # Alert respone 
                messagebox.showinfo("COMMAND", "Please choose the types of functions!") 
        else:
                # The operation is done
                print("Operation is interrupted")

                # Alert respone 
                messagebox.showinfo("COMMAND", "Please choose the types of modes!")   

    def stop_operation():
        # Show the alert
        messagebox.showinfo("COMMAND", "STOPPPPPPPPPPPPPPP!")

    def reset_operation():
        # Reset State
        global State, mode_var, func_var
        State = False
        mode_var = StringVar()
        func_var = StringVar()


    # Add Ratio Button for Mode
    Modebutton_1 = customtkinter.CTkRadioButton(master=main_frame, text="Module",
                                                 variable= mode_var, value= '1')
    Modebutton_2 = customtkinter.CTkRadioButton(master=main_frame, text="Register",
                                                 variable= mode_var, value= '2')

    Modebutton_1.place(relx=0.55, rely=0.3, anchor='center')
    Modebutton_2.place(relx=0.8, rely=0.3, anchor='center')

    # Add Ratio Button for Function
    Funcbutton_1 = customtkinter.CTkRadioButton(master=main_frame, text="Text",
                                                 variable= func_var, value= '1')
    Funcbutton_2 = customtkinter.CTkRadioButton(master=main_frame, text="Screenshot",
                                                 variable= func_var, value= '2')

    Funcbutton_1.place(relx=0.55, rely=0.5, anchor='center')
    Funcbutton_2.place(relx=0.8, rely=0.5, anchor='center')

    # Add Process Button
    run_button = customtkinter.CTkButton(master=main_frame,
                                         width=80,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8,
                                         text="Start",
                                         font=('Arial',15),command= start_operation)
    run_button.place(relx=0.2, rely=0.7, anchor='center')

    stop_button = customtkinter.CTkButton(master=main_frame,
                                         width=80,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8,
                                         text="Stop",
                                         font=('Arial',15),
                                         fg_color = '#FA2323' ,
                                         hover_color = '#C31C1C', command= stop_operation)
    stop_button.place(relx=0.5, rely=0.7, anchor='center')

    reset_button = customtkinter.CTkButton(master=main_frame,
                                         width=80,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8,
                                         text="Reset",
                                         font=('Arial',15),
                                         fg_color = '#5CB0FB',
                                         hover_color = '#0C82EB',command= reset_operation)
    reset_button.place(relx=0.8, rely=0.7, anchor='center')

# Create a Textbox to display the selected file for PDF page
folder_path1 = StringVar()
folder_path2 = StringVar()
# Initial Variable
mode_var = StringVar()
func_var = StringVar()
State = False
file_path = ''
file_path2 = ''

# Indication function
def hide_indicate():
    PDF_indicate.configure(bg_color = '#3E3E3E')
    Type_indicate.configure(bg_color = '#3E3E3E')
    Home_indicate.configure(bg_color = '#3E3E3E')
    S2_indicate.configure(bg_color = '#3E3E3E')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
    global mode_var, func_var, file_path, file_path2
    mode_var = StringVar()
    func_var = StringVar()
    file_path = ''
    file_path2 = ''

def indicate(lb, page):
    hide_indicate()
    lb.configure(bg_color = 'green')
    delete_pages()
    page()

# Create Navigate Button
PDFbutton = customtkinter.CTkButton(option_frame, text="CONVERTING",
                                        font = ("Arial", 15, 'bold'),
                                        width=40,
                                        height=16,
                                        bg_color="#3E3E3E",
                                        fg_color='#3E3E3E',
                                        border_width = 2,
                                        command=lambda: indicate(PDF_indicate, PDF_page))
PDFbutton.place(relx=0.5, rely=0.12 , anchor='center')

PDF_indicate = customtkinter.CTkLabel(option_frame, text='', bg_color= '#3E3E3E')
PDF_indicate.place(relx=0, rely=0.087, width = 5, height=37)

Typebutton = customtkinter.CTkButton(option_frame, text="AUTOTYPING",
                                        font = ("Arial", 15, 'bold'),
                                        width=40,
                                        height=16,
                                        bg_color="#3E3E3E",
                                        fg_color='#3E3E3E',
                                        border_width = 2,
                                        command=lambda: indicate(Type_indicate, Type_page))
Typebutton.place(relx=0.5, rely=0.25 , anchor='center')

Type_indicate = customtkinter.CTkLabel(option_frame, text='', bg_color= '#3E3E3E')
Type_indicate.place(relx=0, rely=0.217, width = 5, height=37)

Home_button = customtkinter.CTkButton(option_frame, text="HOME",
                                        font = ("Arial", 15, 'bold'),
                                        width=40,
                                        height=16,
                                        bg_color="#3E3E3E",
                                        fg_color='#3E3E3E',
                                        border_width = 2,
                                        command=lambda: indicate(Home_indicate, Home_page))
Home_button.place(relx=0.5, rely=0.8 , anchor='center')
Home_indicate = customtkinter.CTkLabel(option_frame, text='', bg_color= '#3E3E3E')
Home_indicate.place(relx=0, rely=0.76, width = 5, height=37)

S2_button = customtkinter.CTkButton(option_frame, text="S2oE BITLIST",
                                        font = ("Arial", 15, 'bold'),
                                        width=40,
                                        height=16,
                                        bg_color="#3E3E3E",
                                        fg_color='#3E3E3E',
                                        border_width = 2,
                                        command=lambda: indicate(S2_indicate, S2oE_page))
S2_button.place(relx=0.5, rely=0.38 , anchor='center')

S2_indicate = customtkinter.CTkLabel(option_frame, text='', bg_color= '#3E3E3E')
S2_indicate.place(relx=0, rely=0.347, width = 5, height=37)

root.mainloop()