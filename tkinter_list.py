import tkinter as tk
import datetime

numbers1 = []
numbers2 = []

# MAIN TKINTER FORM 
class workSpace:
    def insert_numb(self):
        root = tk.Tk()
        root.geometry('400x400')
        root.configure(background='#D3D3D3')
        root.title('Sorting Lists')

        list1 = insertNumbers()

        tk.Button(root, text="Insert Numbers", bg="#D3D3D3", command=list1.manipulation_numb).grid(row=0, column=1, sticky=tk.W, pady=6)
        root.mainloop()

# FORM FOR INSERTING NUMBERS AND MANIPULATION WITH LIST
class insertNumbers:
    def manipulation_numb(self):
        root_manipulation = tk.Tk()
        root_manipulation.geometry("400x400")
        root_manipulation.title('Insert Numbers')

        tk.Label(root_manipulation, text="Number1: ").grid(row=0)
        tk.Label(root_manipulation, text="Number2: ").grid(row=1)
        tk.Label(root_manipulation, text="Number3: ").grid(row=2)
        tk.Label(root_manipulation, text="Number4: ").grid(row=3)

        number_1 = tk.Entry(root_manipulation)
        number_2 = tk.Entry(root_manipulation)
        number_3 = tk.Entry(root_manipulation)
        number_4 = tk.Entry(root_manipulation)

        number_1.grid(row=0, column=1)
        number_2.grid(row=1, column=1)
        number_3.grid(row=2, column=1)
        number_4.grid(row=3, column=1)

        sorting = sortNumbers()

        def check_numbers():
            check_numb1 = number_1.get()
            check_numb2 = number_2.get()
            check_numb3 = number_3.get()
            check_numb4 = number_4.get()

            numbers1.append(check_numb1)
            numbers1.append(check_numb2)
            numbers1.append(check_numb3)
            numbers1.append(check_numb4)

            txt_box_numb = tk.Text(root_manipulation, width=20, height=20)
            txt_box_numb.grid(row=10, column=1, columnspan=2)
            txt_box_numb.insert('end-1c', numbers1)

            times_print = datetime.datetime.now()
            times_print_pm = datetime.datetime.now()

            print('*' * 30)
            print(f"Inserting numbers time:\n{times_print} {times_print_pm.strftime('%p')}")
            print('*' * 30)

        tk.Button(root_manipulation, text="Submit", bg="#D3D3D3", fg="red", command=check_numbers).grid(row=4, column=1, sticky=tk.W, pady=4)
                                                                                        
        tk.Button(root_manipulation, text="Sort", bg="#D3D3D3", fg="red", command=sorting.sorting_numb).grid(row=4, column=2, sticky=tk.W, pady=4)
                                                                                        

# SORTING LISTS AND SORTING, DELETING NUMBERS IN LIST AND AFTER THAT PRINT THE CORRECT NUMBERS. 
class sortNumbers:
    def sorting_numb(self):
        nested_list = numbers1
        dp_list = numbers2

        times_print = datetime.datetime.now()
        times_print_pm = datetime.datetime.now()

        myList = sorted(set(nested_list))
        dp_list.append(myList)

        print(f"Sorting numbers time: {times_print} {times_print_pm.strftime('%p')}")
        print(dp_list)
        print('*' * 30)


a = workSpace()
a.insert_numb()
