# Employee Leave Management System — P33

Student: SONI HET JATINKUMAR  
Enrollment: IU2441230424  
Roll / serial number: 33

## About this package

This package matches the implementation described in IU2441230424.pdf.
The four Python source files are unchanged from the user-supplied repository:
https://github.com/panther20006/LeaveManagementSystem
Commit: c874951ab7e9a5c529e6fa7e199e4a813aefb413

The active CSV files contain the report's synthetic demonstration dataset
(page 7), so the charts reproduce its results. The repository's original
small CSV samples are preserved separately in original_samples/.

## Run

1. Extract the ZIP.
2. Open a terminal in the extracted LeaveManagementSystem directory.
3. Use Python 3 with Tkinter installed and a graphical desktop.
4. Run:

```sh
python -m pip install -r requirements.txt
python main.py
```

On Ubuntu use python3 in place of python. If Tkinter is missing, install
python3-tk using your system package manager. Tkinter is not installed with pip.
For an isolated environment, first create and activate a Python virtual environment.

Always launch from the project directory: the CSV paths are relative to it.

## Files

- main.py: Tkinter forms, record tables, search and action buttons.
- employee.py: add_employee() and get_employees().
- leave.py: add_leave() and get_leaves().
- reports.py: total_leaves(), department_report() and type_report().
- employees.csv: four synthetic employees.
- leaves.csv: eight synthetic leave requests.
- requirements.txt: external Python dependencies.
- original_samples/: original repository CSV files, not loaded by default.

## Expected demo results

Total recorded days: 21.
Approved: 17; Pending: 3; Rejected: 1.
Department totals: Engineering 10, HR 6, Sales 5.
Type totals: Earned 9, Casual 6, Sick 4, Emergency 2.
Search for Pending to see employee 103's three-day request.

The original reports include ALL statuses, as explained in the PDF.
New records you add will change these totals and will persist in the CSV files.

## Screenshot checklist

Capture the main menu, employee table, leave table, search result,
department chart and leave-type chart on your desktop.
The code's current table layout may require enlarging the window to see columns.

## Known limitations documented in the report

There is no period comparison, dedicated employee-total report, edit/delete
screen or approval workflow. Validation only checks empty employee fields
and positive integer leave days in the GUI. Dates are stored as text; days
are entered manually. Duplicate/unknown IDs are not rejected. Report
functions do not handle missing or malformed CSV files. These limitations
are preserved so that the code agrees with the supplied report.

## Verification

The storage and reporting functions were executed on isolated data while
preparing the PDF. Both charts and the 21-day demo total were verified.
All four source files were syntax-checked. Interactive Tkinter execution
was not verified in the report-generation environment because no graphical
display was available.
