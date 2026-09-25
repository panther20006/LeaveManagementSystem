import csv
import os

def add_employee(eid, name, dept):
    file_exists = os.path.exists("employees.csv")

    with open("employees.csv", "a", newline="") as f:
        w = csv.writer(f)

        if not file_exists:
            w.writerow(["ID", "Name", "Department"])

        w.writerow([eid, name, dept])


def get_employees():
    if not os.path.exists("employees.csv"):
        return []

    with open("employees.csv", "r") as f:
        return list(csv.DictReader(f))