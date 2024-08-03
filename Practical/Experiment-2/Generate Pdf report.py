import csv
from fpdf import FPDF

# Open the CSV file in write mode
fh = open("student.csv", "w", newline="")
w = csv.writer(fh)

# Write the header to the CSV file
header = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of birth", "Phone_no."]
w.writerow(header)

data = []

# Take student data from the user
while True:
    try:
        n = int(input("How many student records would you like to insert? "))
        break
    except ValueError:
        print("Please enter a valid number!")

for i in range(n):
    print("Enter Student record", i + 1, ":")
    student_id = input("Student ID: ")
    name = input("Name: ")
    while True:
        try:
            roll = int(input("Roll: "))
            break
        except ValueError:
            print("Invalid Roll, please enter again.")
    semester = input("Semester: ")
    shift = input("Shift: ")
    dept = input("Department: ")
    dob = input("Date of birth (dd/mm/yyyy): ")
    phone_no = input("Phone No: ")

    # Store student data in the list
    rec = [student_id, name, roll, semester, shift, dept, dob, phone_no]
    data.append(rec)

# Write student data to the CSV file
w.writerows(data)
fh.close()

# Print student records from the stored CSV file
print("Student records stored in CSV file.")
print("If you want to see the PDF report, please open 'student.pdf' in your current directory.")

# Open the CSV file in read mode
fh = open("student.csv", "r")
r = csv.reader(fh)

pdf = FPDF()
pdf.add_page()
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', 'B', 14.0)
pdf.cell(page_width, 0.0, 'Students Data Report', align='C')
pdf.ln(10)

pdf.set_font('Courier', '', 12)

# Adjust column width according to the content
col_width = page_width / 4

pdf.ln(1)

th = pdf.font_size
for row in r:
    for item in row:
        pdf.cell(col_width, th, str(item), border=1)
    pdf.ln(th)

pdf.ln(10)

pdf.set_font('Times', '', 10.0)
pdf.cell(page_width, 0.0, '- end of report -', align='C')

# Save the PDF file
pdf.output('student.pdf', '')
fh.close()
