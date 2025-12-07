# Exam Seating Arrangement Generator (Streamlit App)

A Streamlit-based tool to automatically generate **room-wise seating plans** and **attendance sheets** (PDF + Excel) for exams, using a single master Excel file and an optional ZIP of student photos.

This project was built for IIT Patna’s exam seating requirements, but the logic is generic enough to be adapted for other institutes.

---

## ✨ Features

- ✅ Reads a single master workbook (`input_data_tt.xlsx`) containing:
  - Timetable (dates, morning/evening subjects)
  - Course–roll mappings
  - Roll number–student name mappings
  - Room capacities & building info
- 🧮 Automatically allocates students to rooms:
  - Honors **room capacity** and configurable **buffer seats**
  - Supports two layouts:
    - **dense**: full effective capacity per subject
    - **sparse**: at most half capacity per subject (for distancing / spacing)
  - Tries to keep allocations **within the same building** and **minimal room spread**
- 🧑‍🎓 Attendance sheets per subject–room:
  - **PDF** with:
    - Student photo (or placeholder)
    - Name, roll number, signature space
    - Single header per exam and invigilator table on the last page
  - **Excel** sheet with:
    - Student info
    - Space for TA & invigilator signatures
- 🖼️ Optional student photos:
  - Accepts `images.zip` with files named by **roll number** (e.g., `2511AI26.jpg`)
  - Falls back to a generated **placeholder image** if no photo is found
- 📦 One-click download:
  - Generates a single `outputs.zip` containing:
    - PDFs & Excels per date / session / subject / room
    - `op_overall_seating_arrangement.xlsx`
    - `op_seats_left.xlsx`
    - `allocation.log` and `errors.txt` for debugging

---

## 🧱 Project Structure (Runtime)

At runtime (inside a temp directory), the app creates a structure like:

```text
outputs/
  12_12_2025/
    Morning/
      CS301_6103.pdf
      CS301_6103.xlsx
      ...
    Evening/
      ...
  13_12_2025/
    ...
  op_overall_seating_arrangement.xlsx
  op_seats_left.xlsx
  allocation.log
  errors.txt

outputs.zip   ← zipped version of the entire `outputs/` directory
