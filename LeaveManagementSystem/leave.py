import csv
import os

def add_leave(eid, ltype, start, end, days, status):
    file_exists = os.path.exists("leaves.csv")

    with open("leaves.csv", "a", newline="") as f:
        w = csv.writer(f)

        if not file_exists:
            w.writerow(["ID", "Type", "Start", "End", "Days", "Status"])

        w.writerow([eid, ltype, start, end, days, status])


def get_leaves():
    if not os.path.exists("leaves.csv"):
        return []

    with open("leaves.csv", "r") as f:
        return list(csv.DictReader(f))