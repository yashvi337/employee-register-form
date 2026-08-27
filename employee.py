import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    # Retrieve data from all 10 fields
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    gender = gender_var.get()
    dob = entry_dob.get().strip()
    designation = entry_designation.get().strip()
    department = combo_dept.get()
    salary = entry_salary.get().strip()
    city = entry_city.get().strip()
    address = text_address.get("1.0", tk.END).strip()

    # Form Validation
    if not name or not email or not phone:
        messagebox.showwarning("Missing Data", "Please complete all required fields (Name, Email, and Phone).")
        return

    # Messagebox content display
    info_text = (
        f"1. Full Name: {name}\n"
        f"2. Email: {email}\n"
        f"3. Phone Number: {phone}\n"
        f"4. Gender: {gender}\n"
        f"5. Date of Birth: {dob}\n"
        f"6. Designation: {designation}\n"
        f"7. Department: {department}\n"
        f"8. Salary: {salary}\n"
        f"9. City: {city}\n"
        f"10. Address: {address}"
    )
    
    messagebox.showinfo("Registration Successful", info_text)

# Main Window Initialization
root = tk.Tk()
root.title("Employee Onboarding Portal")
root.geometry("520x720")
root.configure(bg="#F3F4F6")  # Soft grey canvas background
root.resizable(False, False)

# Modern Theme Tweaks
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground="#FFFFFF", background="#E5E7EB", padding=5)

# Header Section
header_frame = tk.Frame(root, bg="#1E293B", pady=15)
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="Employee Registration", font=("Segoe UI", 16, "bold"), fg="#FFFFFF", bg="#1E293B")
title_label.pack()

subtitle_label = tk.Label(header_frame, text="Fill out the details below to register a new team member", font=("Segoe UI", 9), fg="#94A3B8", bg="#1E293B")
subtitle_label.pack()

# Centered White Card Layout
card_frame = tk.Frame(root, bg="#FFFFFF", padx=25, pady=20, highlightbackground="#E2E8F0", highlightthickness=1)
card_frame.pack(pady=20, padx=25, fill="both", expand=True)

# UI Component Helpers
def create_label(parent, text, row):
    lbl = tk.Label(parent, text=text, font=("Segoe UI", 9, "bold"), fg="#334155", bg="#FFFFFF")
    lbl.grid(row=row, column=0, sticky="w", pady=6)
    return lbl

def create_entry(parent, row):
    ent = tk.Entry(parent, font=("Segoe UI", 10), bg="#F8FAFC", fg="#0F172A", relief="flat", highlightbackground="#CBD5E1", highlightthickness=1, width=28)
    ent.grid(row=row, column=1, sticky="w", pady=6, ipady=3)
    return ent

# 1. Full Name
create_label(card_frame, "1. Full Name:", 0)
entry_name = create_entry(card_frame, 0)

# 2. Email Address
create_label(card_frame, "2. Email Address:", 1)
entry_email = create_entry(card_frame, 1)

# 3. Phone Number
create_label(card_frame, "3. Phone Number:", 2)
entry_phone = create_entry(card_frame, 2)

# 4. Gender (Radio Buttons)
create_label(card_frame, "4. Gender:", 3)
gender_var = tk.StringVar(value="Male")
gender_frame = tk.Frame(card_frame, bg="#FFFFFF")
gender_frame.grid(row=3, column=1, sticky="w", pady=6)

for g_text in ["Male", "Female", "Other"]:
    rb = tk.Radiobutton(gender_frame, text=g_text, variable=gender_var, value=g_text, font=("Segoe UI", 9), bg="#FFFFFF", activebackground="#FFFFFF", fg="#334155")
    rb.pack(side="left", padx=3)

# 5. Date of Birth
create_label(card_frame, "5. Date of Birth:", 4)
entry_dob = create_entry(card_frame, 4)

# 6. Designation
create_label(card_frame, "6. Designation:", 5)
entry_designation = create_entry(card_frame, 5)

# 7. Department (Combobox)
create_label(card_frame, "7. Department:", 6)
combo_dept = ttk.Combobox(card_frame, values=["IT & Software", "Human Resources", "Finance", "Marketing", "Sales"], state="readonly", width=26)
combo_dept.current(0)
combo_dept.grid(row=6, column=1, sticky="w", pady=6)

# 8. Salary
create_label(card_frame, "8. Salary:", 7)
entry_salary = create_entry(card_frame, 7)

# 9. City
create_label(card_frame, "9. City:", 8)
entry_city = create_entry(card_frame, 8)

# 10. Address (Multi-line Text Field)
create_label(card_frame, "10. Address:", 9)
text_address = tk.Text(card_frame, font=("Segoe UI", 9), bg="#F8FAFC", fg="#0F172A", relief="flat", highlightbackground="#CBD5E1", highlightthickness=1, width=26, height=3)
text_address.grid(row=9, column=1, sticky="w", pady=6)

# Primary Accent Submit Button
submit_btn = tk.Button(
    card_frame, 
    text="Submit Details", 
    bg="#2563EB", 
    fg="white", 
    activebackground="#1D4ED8",
    activeforeground="white",
    font=("Segoe UI", 10, "bold"), 
    relief="flat",
    cursor="hand2",
    command=submit_form
)
submit_btn.grid(row=10, columnspan=2, pady=15, ipady=5, sticky="ew")

# Run Application Loop
root.mainloop()