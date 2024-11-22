import tkinter as tk
from tkinter import ttk, messagebox
import os

# Helper function to calculate percentage and grade
def calculate_percentage_and_grade(coursework, exam):
    total_marks = coursework + exam
    overall_percentage = (total_marks / 160) * 100
    if overall_percentage >= 70:
        return overall_percentage, 'A'
    elif overall_percentage >= 60:
        return overall_percentage, 'B'
    elif overall_percentage >= 50:
        return overall_percentage, 'C'
    elif overall_percentage >= 40:
        return overall_percentage, 'D'
    else:
        return overall_percentage, 'F'

# Load students from the file
def load_students(file_path):
    students = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip the first line (number of students)
                parts = line.strip().split(',')
                student_code = int(parts[0])
                name = parts[1]
                coursework_marks = sum(map(int, parts[2:5]))  # Coursework marks are assumed to be 3 parts
                exam_mark = int(parts[5])
                percentage, grade = calculate_percentage_and_grade(coursework_marks, exam_mark)
                students.append({
                    'code': student_code,
                    'name': name,
                    'coursework': coursework_marks,
                    'exam': exam_mark,
                    'percentage': percentage,
                    'grade': grade
                })
    return students

# Save updated student list to the file
def save_students(file_path, students):
    with open(file_path, 'w') as file:
        file.write(f"{len(students)}\n")
        for student in students:
            coursework_marks = ','.join(map(str, [student['coursework'] // 3] * 3))  # Assume even split for coursework
            file.write(f"{student['code']},{student['name']},{coursework_marks},{student['exam']}\n")

# Display all student records
def view_all_students():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Student Records:\n\n")
    for student in students:
        output_text.insert(tk.END, f"Name: {student['name']}\n")
        output_text.insert(tk.END, f"Number: {student['code']}\n")
        output_text.insert(tk.END, f"Coursework Total: {student['coursework']}\n")
        output_text.insert(tk.END, f"Exam Mark: {student['exam']}\n")
        output_text.insert(tk.END, f"Overall Percentage: {student['percentage']:.2f}%\n")
        output_text.insert(tk.END, f"Grade: {student['grade']}\n\n")
    output_text.insert(tk.END, f"Number of Students: {len(students)}\n")
    avg_percentage = sum(student['percentage'] for student in students) / len(students) if students else 0
    output_text.insert(tk.END, f"Average Percentage: {avg_percentage:.2f}%\n")

# View individual student record
def view_individual_student():
    selected_name = student_dropdown.get()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Student Record:\n\n")
    for student in students:
        if student['name'] == selected_name:
            output_text.insert(tk.END, f"Name: {student['name']}\n")
            output_text.insert(tk.END, f"Number: {student['code']}\n")
            output_text.insert(tk.END, f"Coursework Total: {student['coursework']}\n")
            output_text.insert(tk.END, f"Exam Mark: {student['exam']}\n")
            output_text.insert(tk.END, f"Overall Percentage: {student['percentage']:.2f}%\n")
            output_text.insert(tk.END, f"Grade: {student['grade']}\n")
            return
    messagebox.showinfo("Error", "Student not found!")

# Show student with highest or lowest score
def show_highest_lowest(highest=True):
    if not students:
        messagebox.showinfo("Error", "No student records found!")
        return
    student = max(students, key=lambda s: s['percentage']) if highest else min(students, key=lambda s: s['percentage'])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Student Record:\n\n")
    output_text.insert(tk.END, f"Name: {student['name']}\n")
    output_text.insert(tk.END, f"Number: {student['code']}\n")
    output_text.insert(tk.END, f"Coursework Total: {student['coursework']}\n")
    output_text.insert(tk.END, f"Exam Mark: {student['exam']}\n")
    output_text.insert(tk.END, f"Overall Percentage: {student['percentage']:.2f}%\n")
    output_text.insert(tk.END, f"Grade: {student['grade']}\n")

# Delete a student record
def delete_student():
    selected_name = student_dropdown.get()
    global students
    if selected_name:
        # Remove the student from the list
        students = [student for student in students if student['name'] != selected_name]
        # Update the student dropdown values
        student_dropdown['values'] = [student['name'] for student in students]
        student_dropdown.set('')  # Clear the dropdown selection
        save_students(file_path, students)  # Save the updated student list to file
        view_all_students()  # Refresh the view to show updated student list
        messagebox.showinfo("Success", "Student deleted successfully!")
    else:
        messagebox.showinfo("Error", "Please select a student to delete.")

# Update a student record
def update_student():
    selected_name = student_dropdown.get()
    if not selected_name:
        messagebox.showinfo("Error", "Please select a student to update.")
        return

    student = next((s for s in students if s['name'] == selected_name), None)
    if not student:
        messagebox.showinfo("Error", "Student not found!")
        return

    def save_updated_student():
        try:
            # Update student fields
            student['name'] = name_entry.get()
            student['coursework'] = sum(map(int, coursework_entry.get().split(',')))
            student['exam'] = int(exam_entry.get())
            student['percentage'], student['grade'] = calculate_percentage_and_grade(student['coursework'], student['exam'])

            # Save updated student data to file
            save_students(file_path, students)

            # Refresh the dropdown list with updated student names
            student_dropdown['values'] = [student['name'] for student in students]
            student_dropdown.set(student['name'])  # Keep the same student selected
            messagebox.showinfo("Success", "Student updated successfully!")
            update_window.destroy()
            view_all_students()  # Refresh the output text box
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please try again.")

    # Create the Update Student window
    update_window = tk.Toplevel(root)
    update_window.title("Update Student")
    tk.Label(update_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(update_window)
    name_entry.insert(0, student['name'])
    name_entry.grid(row=0, column=1)
    tk.Label(update_window, text="Coursework (comma-separated):").grid(row=1, column=0)
    coursework_entry = tk.Entry(update_window)
    coursework_entry.insert(0, ','.join([str(student['coursework'] // 3)] * 3))  # Assume even split for coursework
    coursework_entry.grid(row=1, column=1)
    tk.Label(update_window, text="Exam:").grid(row=2, column=0)
    exam_entry = tk.Entry(update_window)
    exam_entry.insert(0, student['exam'])
    exam_entry.grid(row=2, column=1)
    tk.Button(update_window, text="Save", command=save_updated_student).grid(row=3, column=1)

# Add a new student record
def add_student():
    def save_new_student():
        try:
            new_code = int(code_entry.get())
            new_name = name_entry.get()
            coursework_marks = sum(map(int, coursework_entry.get().split(',')))
            new_exam = int(exam_entry.get())
            percentage, grade = calculate_percentage_and_grade(coursework_marks, new_exam)
            
            new_student = {
                'code': new_code,
                'name': new_name,
                'coursework': coursework_marks,
                'exam': new_exam,
                'percentage': percentage,
                'grade': grade
            }
            
            # Add new student to the list
            students.append(new_student)
            save_students(file_path, students)  # Save the updated list to the file
            student_dropdown['values'] = [student['name'] for student in students]  # Update dropdown
            student_dropdown.set(new_name)  # Set the newly added student's name in dropdown
            messagebox.showinfo("Success", "New student added successfully!")
            add_window.destroy()
            view_all_students()  # Refresh the output text box
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please try again.")

    # Create the Add Student window
    add_window = tk.Toplevel(root)
    add_window.title("Add Student")
    tk.Label(add_window, text="Code:").grid(row=0, column=0)
    code_entry = tk.Entry(add_window)
    code_entry.grid(row=0, column=1)
    tk.Label(add_window, text="Name:").grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)
    tk.Label(add_window, text="Coursework (comma-separated):").grid(row=2, column=0)
    coursework_entry = tk.Entry(add_window)
    coursework_entry.grid(row=2, column=1)
    tk.Label(add_window, text="Exam:").grid(row=3, column=0)
    exam_entry = tk.Entry(add_window)
    exam_entry.grid(row=3, column=1)
    tk.Button(add_window, text="Add", command=save_new_student).grid(row=4, column=1)

# Main application setup
file_path = "studentMarks.txt"
students = load_students(file_path)

root = tk.Tk()
root.title("Student Manager")
root.geometry("800x600")
root.configure(bg="#B3C8CF")  

# Title Label
title_label = tk.Label(root, text="Student Manager", font=("Helvetica", 16, "bold"),bg="#B3C8CF")
title_label.pack(pady=10)

# Horizontal Buttons
button_frame = tk.Frame(root, bg="#B3C8CF")
button_frame.pack(pady=10)

btn_view_all = tk.Button(button_frame, text="View All Student Records", command=view_all_students, width=20, bg="#7BD3EA")
btn_view_all.grid(row=0, column=0, padx=5)

btn_highest = tk.Button(button_frame, text="Show Highest Score", command=lambda: show_highest_lowest(highest=True), width=20, bg="#A1EEBD")
btn_highest.grid(row=0, column=1, padx=5)

btn_lowest = tk.Button(button_frame, text="Show Lowest Score", command=lambda: show_highest_lowest(highest=False), width=20, bg="#F6F7C4")
btn_lowest.grid(row=0, column=2, padx=5)

# Dropdown for individual record
dropdown_frame = tk.Frame(root)
dropdown_frame.pack(pady=10)

dropdown_label = tk.Label(dropdown_frame, text="View Individual Student Record:")
dropdown_label.pack(side=tk.LEFT)

student_names = [student['name'] for student in students]
student_dropdown = ttk.Combobox(dropdown_frame, values=student_names, state="readonly", width=30)
student_dropdown.pack(side=tk.LEFT, padx=10)

btn_view_individual = tk.Button(dropdown_frame, text="View Record", command=view_individual_student , bg="#FA4032")
btn_view_individual.pack(side=tk.LEFT)

# Button frame for add, update, and delete
button_frame2 = tk.Frame(root, bg="#B3C8CF")
button_frame2.pack(pady=10)

btn_add_student = tk.Button(button_frame2, text="Add Student", command=add_student, width=20, bg="#FFB6C1")
btn_add_student.grid(row=0, column=0, padx=5)

btn_update = tk.Button(button_frame2, text="Update Student Record", command=update_student, width=20, bg="#D4A5A5")
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(button_frame2, text="Delete Student Record", command=delete_student, width=20, bg="#F8AFA6")
btn_delete.grid(row=0, column=2, padx=5)

# Output text box with scroll bar
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

output_text = tk.Text(output_frame, width=80, height=20, wrap=tk.WORD, bg="#D8DBBD")
scrollbar = tk.Scrollbar(output_frame, orient="vertical", command=output_text.yview)
output_text.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
output_text.pack(side="left", fill="both", expand=True)

root.mainloop()
