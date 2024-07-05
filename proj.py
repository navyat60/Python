import tkinter as tk
from tkinter import messagebox
import sqlite3

class Worker:
    def __init__(self,id, name,age,department,Mobile_No, salary):
        self.id = id
        self.name = name
        self.age = age
        self.department = department
        self.Mobile_No = Mobile_No
        self.salary = salary


class WorkersManagementSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workers Management System")
        self.workers = []
        self.create_widgets()

    def _init_(self, root):
        # ... your existing code ...
        self.conn = sqlite3.connect('Workers.db')  # Connect to database
        self.create_table()  # Create table if it doesn't exist

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS workers (
                          id INTEGER PRIMARY KEY,
                          name TEXT NOT NULL,
                          age INTEGER NOT NULL,
                          department TEXT,
                          Mobile_No TEXT,
                          salary REAL
                        )''')
        self.conn.commit()

    def create_widgets(self):

        self.fr = tk.Frame(self.root,bg="lightblue",bd=13)
        self.fr.place(x=640,y=80,height=400,width=250)
        self.id_label = tk.Label(self.fr, text="ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self.fr)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.name_label = tk.Label(self.fr, text="Name:")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.fr)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.age_label = tk.Label(self.fr, text="Age:")
        self.age_label.grid(row=2, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.fr)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        self.department_label = tk.Label(self.fr, text="department:")
        self.department_label.grid(row=3, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(self.fr)
        self.department_entry.grid(row=3, column=1, padx=5, pady=5)

        self.Mobile_No_label = tk.Label(self.fr, text="Mobile_No:")
        self.Mobile_No_label.grid(row=4, column=0, padx=5, pady=5)
        self.Mobile_No_entry = tk.Entry(self.fr)
        self.Mobile_No_entry.grid(row=4, column=1, padx=5, pady=5)

        self.salary_label = tk.Label(self.fr, text="Salary:")
        self.salary_label.grid(row=5, column=0, padx=5, pady=5)
        self.salary_entry = tk.Entry(self.fr)
        self.salary_entry.grid(row=5, column=1, padx=5, pady=5)


        self.add_button = tk.Button(self.fr, text="Add Worker", command=self.add_worker)
        self.add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.update_button = tk.Button(self.fr, text="Update Salary", command=self.update_salary)
        self.update_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.display_button = tk.Button(self.fr, text="Display Workers", command=self.display_workers)
        self.display_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.search_button = tk.Button(self.fr, text="Search Worker", command=self.search_worker)
        self.search_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.delete_button = tk.Button(self.fr, text="Delete Worker", command=self.delete_worker)
        self.delete_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="we")


    def add_worker(self):
        try:
            id = int(self.id_entry.get())
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            department = self.department_entry.get()
            Mobile_No = self.Mobile_No_entry.get()
            salary = float(self.salary_entry.get())

            for worker in self.workers:
                if worker.id == id:
                    messagebox.showerror("Error", "ID already exists! Please enter a unique ID.")
                    return

            worker = Worker(id, name, age,department,Mobile_No,salary)
            self.workers.append(worker)

            if not name.isalpha():
                raise ValueError("Invalid input!")

            if age < 19 or age > 60:
                raise ValueError("Invalid input!")
            messagebox.showinfo("Success","Worker added successfully",)
        except ValueError:
             messagebox.showerror("Error", "Invalid input!")

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO workers VALUES (?, ?, ?, ?, ?, ?)",
                       (id, name, age, department, Mobile_No, salary))
        self.conn.commit()
        messagebox.showinfo("Success", "Worker added successfully!")

    # ... update other methods (update_salary, search_worker, display_workers, delete_worker) to use SQL queries ...

    def update_salary(self):
        try:
            id = int(self.id_entry.get())
            new_salary = float(self.salary_entry.get())

            for worker in self.workers:
                if worker.id == id:
                    worker.salary = new_salary
                    messagebox.showinfo("Success", "Salary updated successfully!")
                    return
            messagebox.showerror("Error", "Worker not found with given ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid ID and Salary.")

    def search_worker(self):
        try:
            id = int(self.id_entry.get())

            for worker in self.workers:
                if worker.id == id:
                    messagebox.showinfo("Worker Details",
                        f"Name: {worker.name}\nAge: {worker.age}\nDepartmrnt: {worker.department} \nMobile_No: {worker.Mobile_No}\nSalary: {worker.salary}")
                    return
            messagebox.showerror("Error", "Worker not found with given ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid ID.")

    def display_workers(self):
        if self.workers:
            workers_info = "Workers in the system:\n\n"
            for worker in self.workers:
                workers_info += f"->ID: {worker.id}, Name: {worker.name}, Age: {worker.age},Departmrnt:{worker.department}, Mobile_No:{worker.Mobile_No}, Salary: {worker.salary}\n"
            messagebox.showinfo("Workers", workers_info)
        else:
            messagebox.showinfo("Workers", "No workers in the system.")

    def delete_worker(self):
        try:
            id = int(self.id_entry.get())

            for i, worker in enumerate(self.workers):
                if worker.id == id:
                    del self.workers[i]
                    messagebox.showinfo("Success", "Worker deleted successfully!")
                    return
            messagebox.showerror("Error", "Worker not found with given ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid ID.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1370x700+0+0")
    app= WorkersManagementSystemApp(root)
    root.mainloop()