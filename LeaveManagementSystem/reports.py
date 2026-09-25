import pandas as pd
import matplotlib.pyplot as plt


def total_leaves():
    df = pd.read_csv("leaves.csv")
    return df["Days"].sum()


def department_report():
    leaves = pd.read_csv("leaves.csv")
    emp = pd.read_csv("employees.csv")

    data = leaves.merge(emp, on="ID")
    data.groupby("Department")["Days"].sum().plot(kind="bar")

    plt.title("Department Wise Leave")
    plt.ylabel("Days")
    plt.show()


def type_report():
    df = pd.read_csv("leaves.csv")

    df.groupby("Type")["Days"].sum().plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Leave Type Report")
    plt.ylabel("")
    plt.show()