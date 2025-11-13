import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class Worker:
    def __init__(self, id, name, dob, department, Mobile_No, salary, PF):
        self.id = id
        self.name = name
        self.dob = dob
        self.department = department
        self.Mobile_No = Mobile_No
        self.salary = salary
        self.PF = PF

class WorkersManagementSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workers Management System")
        self.conn = sqlite3.connect('workers.db')
        self.create_table()
        self.create_widgets()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                dob TEXT,
                department TEXT,
                Mobile_No TEXT,
                salary REAL,
                PF REAL DEFAULT 0
            )
        """)
        cursor.execute("PRAGMA table_info(workers)")
        columns = [info[1] for info in cursor.fetchall()]
        if 'PF' not in columns:
            cursor.execute("ALTER TABLE workers ADD COLUMN PF REAL DEFAULT 0")
            self.conn.commit()

    def create_widgets(self):
        font = ('Helvetica', 12)

        self.fr = tk.Frame(self.root, bg="lightblue", bd=13)
        self.fr.place(x=640, y=90, height=550, width=350)

        self.id_label = tk.Label(self.fr, text="ID:", font=font)
        self.id_label.grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self.fr, font=font)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.name_label = tk.Label(self.fr, text="Name:", font=font)
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.fr, font=font)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.dob_label = tk.Label(self.fr, text="Date of Birth:", font=font)
        self.dob_label.grid(row=2, column=0, padx=5, pady=5)
        self.dob_entry = tk.Entry(self.fr, font=font)
        self.dob_entry.grid(row=2, column=1, padx=5, pady=5)

        self.department_label = tk.Label(self.fr, text="Department:", font=font)
        self.department_label.grid(row=3, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(self.fr, font=font)
        self.department_entry.grid(row=3, column=1, padx=5, pady=5)

        self.Mobile_No_label = tk.Label(self.fr, text="Mobile No:", font=font)
        self.Mobile_No_label.grid(row=4, column=0, padx=5, pady=5)
        self.Mobile_No_entry = tk.Entry(self.fr, font=font)
        self.Mobile_No_entry.grid(row=4, column=1, padx=5, pady=5)

        self.salary_label = tk.Label(self.fr, text="Salary:", font=font)
        self.salary_label.grid(row=5, column=0, padx=5, pady=5)
        self.salary_entry = tk.Entry(self.fr, font=font)
        self.salary_entry.grid(row=5, column=1, padx=5, pady=5)

        self.PF_label = tk.Label(self.fr, text="PF:", font=font)
        self.PF_label.grid(row=6, column=0, padx=5, pady=5)
        self.PF_entry = tk.Entry(self.fr, font=font)
        self.PF_entry.grid(row=6, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.fr, text="Add Worker", command=self.add_worker, font=font)
        self.add_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.update_salary_button = tk.Button(self.fr, text="Update Salary", command=self.update_salary, font=font)
        self.update_salary_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.update_PF_button = tk.Button(self.fr, text="Update PF", command=self.update_PF, font=font)
        self.update_PF_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.display_button = tk.Button(self.fr, text="Display Workers", command=self.display_workers, font=font)
        self.display_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.search_button = tk.Button(self.fr, text="Search Worker", command=self.search_worker, font=font)
        self.search_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.delete_button = tk.Button(self.fr, text="Delete Worker", command=self.delete_worker, font=font)
        self.delete_button.grid(row=12, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def add_worker(self):
        try:
            id = int(self.id_entry.get())
            name = self.name_entry.get()
            dob = self.dob_entry.get()
            department = self.department_entry.get()
            Mobile_No = self.Mobile_No_entry.get()
            salary = float(self.salary_entry.get())
            PF = float(self.PF_entry.get())

            if not name.isalpha():
                raise ValueError("Invalid input!")
            if not Mobile_No.isdigit() or len(Mobile_No) != 10 or Mobile_No[0] not in '6789':
                raise ValueError("Invalid mobile number!")

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM workers WHERE id=?", (id,))
            if cursor.fetchone():
                messagebox.showerror("Error", "ID already exists! Please enter a unique ID.")
                return

            cursor.execute("INSERT INTO workers (id, name, dob, department, Mobile_No, salary, PF) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (id, name, dob, department, Mobile_No, salary, PF))
            self.conn.commit()

            messagebox.showinfo("Success", "Worker added successfully")

        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    def update_salary(self):
        try:
            id = int(self.id_entry.get())
            new_salary = float(self.salary_entry.get())

            cursor = self.conn.cursor()
            cursor.execute("UPDATE workers SET salary=? WHERE id=?", (new_salary, id))
            if cursor.rowcount == 0:
                messagebox.showerror("Error", "Worker not found with given ID.")
            else:
                self.conn.commit()
                messagebox.showinfo("Success", "Salary updated successfully!")

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid ID and Salary.")

    def update_PF(self):
        try:
            id = int(self.id_entry.get())
            new_PF = float(self.PF_entry.get())

            cursor = self.conn.cursor()
            cursor.execute("UPDATE workers SET PF=? WHERE id=?", (new_PF, id))
            if cursor.rowcount == 0:
                messagebox.showerror("Error", "Worker not found with given ID.")
            else:
                self.conn.commit()
                messagebox.showinfo("Success", "PF updated successfully!")

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid ID and PF.")

    def search_worker(self):
        try:
            id = int(self.id_entry.get())

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM workers WHERE id=?", (id,))
            worker = cursor.fetchone()

            if worker:
                messagebox.showinfo("Worker Details",
                                    f"Name: {worker[1]}\nDate of Birth: {worker[2]}\nDepartment: {worker[3]}\nMobile No: {worker[4]}\nSalary: {worker[5]}\nPF: {worker[6]}")
            else:
                messagebox.showerror("Error", "Worker not found with given ID.")

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid ID.")

    def display_workers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM workers")
        workers = cursor.fetchall()

        if workers:
            top = tk.Toplevel(self.root)
            top.title("Workers")

            style = ttk.Style()
            style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="lightgrey")
            style.configure("Treeview", rowheight=25)
            style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])

            tree = ttk.Treeview(top, columns=("ID", "Name", "DOB", "Department", "Mobile_No", "Salary", "PF"), show='headings')
            tree.heading("ID", text="ID")
            tree.heading("Name", text="Name")
            tree.heading("DOB", text="Date of Birth")
            tree.heading("Department", text="Department")
            tree.heading("Mobile_No", text="Mobile No")
            tree.heading("Salary", text="Salary")
            tree.heading("PF", text="PF")

            tree.column("ID", anchor="center", width=50)
            tree.column("Name", anchor="center", width=100)
            tree.column("DOB", anchor="center", width=100)
            tree.column("Department", anchor="center", width=100)
            tree.column("Mobile_No", anchor="center", width=100)
            tree.column("Salary", anchor="center", width=100)
            tree.column("PF", anchor="center", width=100)

            for worker in workers:
                tree.insert("", "end", values=(worker[0], worker[1], worker[2], worker[3], worker[4], worker[5], worker[6]))

            tree.pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showinfo("Workers", "No workers in the system.")

    def delete_worker(self):
        try:
            id = int(self.id_entry.get())

            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM workers WHERE id=?", (id,))
            if cursor.rowcount == 0:
                messagebox.showerror("Error", "Worker not found with given ID.")
            else:
                self.conn.commit()
                messagebox.showinfo("Success", "Worker deleted successfully!")

        except ValueError:
            messagebox.showerror("Error",  "Invalid input! Please enter valid ID.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1370x700+0+0")
    app = WorkersManagementSystemApp(root)
    root.mainloop()
