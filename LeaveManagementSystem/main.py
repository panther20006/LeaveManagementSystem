
import tkinter as tk
from tkinter import ttk, messagebox

from employee import add_employee, get_employees
from leave import add_leave, get_leaves
from reports import total_leaves, department_report, type_report


root = tk.Tk()
root.title("Leave Management System")
root.geometry("750x550")


# ---------- ADD EMPLOYEE ----------
def employee_window():

    win = tk.Toplevel(root)
    win.title("Add Employee")

    tk.Label(win, text="Employee ID").pack()
    eid = tk.Entry(win)
    eid.pack()

    tk.Label(win, text="Name").pack()
    name = tk.Entry(win)
    name.pack()

    tk.Label(win, text="Department").pack()
    dept = tk.Entry(win)
    dept.pack()

    def save():
        if not eid.get() or not name.get() or not dept.get():
            messagebox.showerror("Error", "Fill all fields")
            return

        add_employee(eid.get(), name.get(), dept.get())
        messagebox.showinfo("Success", "Employee Added")
        win.destroy()

    tk.Button(win, text="Save", command=save).pack(pady=15)


# ---------- ADD LEAVE ----------
def leave_window():

    win = tk.Toplevel(root)
    win.title("Add Leave")

    tk.Label(win, text="Employee ID").pack()
    eid = tk.Entry(win)
    eid.pack()

    tk.Label(win, text="Leave Type").pack()
    ltype = ttk.Combobox(
        win,
        values=["Sick", "Casual", "Earned", "Emergency"]
    )
    ltype.pack()

    tk.Label(win, text="Start Date").pack()
    start = tk.Entry(win)
    start.pack()

    tk.Label(win, text="End Date").pack()
    end = tk.Entry(win)
    end.pack()

    tk.Label(win, text="Days").pack()
    days = tk.Entry(win)
    days.pack()

    tk.Label(win, text="Status").pack()
    status = ttk.Combobox(
        win,
        values=["Pending", "Approved", "Rejected"]
    )
    status.pack()

    def save():

        try:
            d = int(days.get())

            if d <= 0:
                raise ValueError

            add_leave(
                eid.get(),
                ltype.get(),
                start.get(),
                end.get(),
                d,
                status.get()
            )

            messagebox.showinfo("Success", "Leave Added")
            win.destroy()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Days must be a number"
            )

    tk.Button(win, text="Save", command=save).pack(pady=15)


# ---------- VIEW EMPLOYEES ----------
def view_employees():

    win = tk.Toplevel(root)
    win.title("Employees")
    win.geometry("500x300")

    table = ttk.Treeview(
        win,
        columns=("ID", "Name", "Department"),
        show="headings"
    )

    for c in ("ID", "Name", "Department"):
        table.heading(c, text=c)

    table.pack(fill="both", expand=True)

    for e in get_employees():
        table.insert(
            "",
            "end",
            values=(e["ID"], e["Name"], e["Department"])
        )


# ---------- VIEW LEAVES ----------
def view_leaves():

    win = tk.Toplevel(root)
    win.title("Leaves")
    win.geometry("700x300")

    cols = ("ID", "Type", "Start", "End", "Days", "Status")

    table = ttk.Treeview(
        win,
        columns=cols,
        show="headings"
    )

    for c in cols:
        table.heading(c, text=c)

    table.pack(fill="both", expand=True)

    for l in get_leaves():
        table.insert(
            "",
            "end",
            values=(
                l["ID"],
                l["Type"],
                l["Start"],
                l["End"],
                l["Days"],
                l["Status"]
            )
        )


# ---------- SEARCH / FILTER ----------
def search_leave():

    win = tk.Toplevel(root)
    win.title("Search / Filter Leaves")
    win.geometry("750x400")

    tk.Label(
        win,
        text="Search by Employee ID / Leave Type / Status"
    ).pack(pady=10)

    search = tk.Entry(win, width=40)
    search.pack()

    cols = ("ID", "Type", "Start", "End", "Days", "Status")

    table = ttk.Treeview(
        win,
        columns=cols,
        show="headings"
    )

    for c in cols:
        table.heading(c, text=c)

    table.pack(fill="both", expand=True, pady=10)

    def show_data():

        for item in table.get_children():
            table.delete(item)

        value = search.get().lower()

        for l in get_leaves():

            if (
                value in l["ID"].lower()
                or value in l["Type"].lower()
                or value in l["Status"].lower()
            ):

                table.insert(
                    "",
                    "end",
                    values=(
                        l["ID"],
                        l["Type"],
                        l["Start"],
                        l["End"],
                        l["Days"],
                        l["Status"]
                    )
                )

    tk.Button(
        win,
        text="Search",
        command=show_data
    ).pack()


# ---------- MAIN GUI ----------

tk.Label(
    root,
    text="EMPLOYEE LEAVE MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
).pack(pady=25)

tk.Button(
    root,
    text="Add Employee",
    width=25,
    command=employee_window
).pack(pady=4)

tk.Button(
    root,
    text="Add Leave",
    width=25,
    command=leave_window
).pack(pady=4)

tk.Button(
    root,
    text="View Employees",
    width=25,
    command=view_employees
).pack(pady=4)

tk.Button(
    root,
    text="View Leaves",
    width=25,
    command=view_leaves
).pack(pady=4)

tk.Button(
    root,
    text="Search / Filter Leave",
    width=25,
    command=search_leave
).pack(pady=4)

tk.Button(
    root,
    text="Total Leave Days",
    width=25,
    command=lambda: messagebox.showinfo(
        "Statistics",
        f"Total Leaves = {total_leaves()}"
    )
).pack(pady=4)

tk.Button(
    root,
    text="Department Report",
    width=25,
    command=department_report
).pack(pady=4)

tk.Button(
    root,
    text="Leave Type Report",
    width=25,
    command=type_report
).pack(pady=4)


root.mainloop()

