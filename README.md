# 🏫 School Fee Management System (Django)

A Django-based web application to manage student records and fee payments — built to be used in **two real schools**. Handles everything from student data to tracking monthly fee payments, with support for both **ID-based** and **Roll Number-based** workflows.

---

## 🚀 Features

### 👨‍🎓 Student Management
- **Add Student** — Add student details (Name, Class, Father’s Name, Contact, Roll Number, Fee).
- **Edit Student** — Update student data by primary key (`pk`) or `roll_number`.
- **View Student List** — View all registered students.
- **Single Student View** — View details of one student by ID or roll number.
- **Delete Student** — Remove a student record from the database.

### 💰 Fee Management
- **Record Fee** — Add fee entries per student with:
  - Amount
  - Month (e.g., "January")
  - Year (e.g., 2025)
  - Paid Status ✅❌
- **View Unpaid Fees** — List of all unpaid fees across students.
- **View Paid Fees** — List of all paid fee records.
- **Mark Paid/Unpaid** — Easily toggle payment status from:
  - Fee list
  - Individual student’s fee history
- **Fee History** — View all fee records of a particular student by `pk` or `roll_number`.

---

## 📦 Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML5, Bootstrap 5 (via Django templates)
- **Database**: SQLite (default — can be swapped for PostgreSQL in production)
- **Forms**: Django ModelForms
- **Messaging**: Django’s built-in `messages` framework for success/failure feedback

---

## ⚙️ Views Breakdown

### Student Views

| View Name | Route | Method | Purpose |
|-----------|-------|--------|---------|
| `add_student` | `/add-student/` | GET, POST | Add new student |
| `edit_student` | `/edit-student/<pk>/` | GET, POST | Edit student by ID |
| `edit_student_by_roll_number` | `/edit-student-by-roll/` | GET, POST | Edit by roll number |
| `student_list` | `/students/` | GET | View all students |
| `single_student_details` | `/student/<pk>/` | GET | View one student by ID |
| `single_student_details_by_roll_number` | `/student-by-roll/` | GET | View one student by roll |
| `delete_student` | `/delete/<pk>/` | POST | Delete by ID |
| `delete_student_by_roll_number` | `/delete-by-roll/` | POST | Delete by roll number |

---

### Fee Views

| View Name | Route | Method | Purpose |
|-----------|-------|--------|---------|
| `unpaid_fees_list` | `/fees/unpaid/` | GET | List all unpaid fees |
| `fees_paid` | `/fees/paid/<pk>/` | POST | Mark specific fee as paid |
| `fees_unpaid` | `/fees/unpaid/<pk>/` | POST | Mark specific fee as unpaid |
| `paid_fees_list` | `/fees/paid/` | GET | List all paid fees |
| `student_fee_record` | `/fees/history/<pk>/` | GET | Fee history by student ID |
| `student_fee_record_by_roll_number` | `/fees/history-by-roll/` | GET | Fee history by roll number |
| `mark_paid_from_history` | `/fees/mark-paid/<pk>/` | POST | Toggle paid from student record |
| `mark_unpaid_from_history` | `/fees/mark-unpaid/<pk>/` | POST | Toggle unpaid from student record |

---

## 📌 Notes

- `Fee_status` model uses a ForeignKey to `Students`, and has `month`, `year`, and `paid` status fields.
- Unique constraint should be enforced on `('student', 'month', 'year')` to prevent duplicate fee records for the same cycle.
- The fee status buttons work seamlessly per fee record, even for repeated months across years.

---

## 📈 To-Do / Upcoming Features

- [ ] 🔐 Admin login + authentication for staff
- [ ] 📅 Add fee creation form with month/year picker
- [ ] 📊 Dashboard with analytics (total students, unpaid counts, etc.)
- [ ] 🧾 PDF receipts/downloadable fee reports
- [ ] 📧 Optional email/SMS reminders for unpaid fees
- [ ] 🌐 Multi-school support from one dashboard (separate databases or scoped by school)

---

## 🛠 Deployment

To deploy on production:

```bash
python manage.py collectstatic
python manage.py migrate
gunicorn projectname.wsgi:application
# Use Nginx / Apache for web serving
