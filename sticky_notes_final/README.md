# Sticky Notes Task Manager

A simple Django-based task manager application that allows users to create, view, update, and delete notes. This project was built as part of the AI Bootcamp assignment to demonstrate understanding of Django models, views, templates, URL routing, CRUD operations, and unit testing.

---

## 📌 Features

### ✔ Create Notes  
Users can add new notes with a title and content.

### ✔ View Notes  
All notes are displayed in a clean list view.

### ✔ Update Notes  
Users can edit existing notes.

### ✔ Delete Notes  
Users can delete notes with a confirmation step.

### ✔ Responsive UI  
Basic styling included using a custom CSS file.

---

## 🗂 Project Structure

sticky_notes/
│
├── manage.py
├── notes/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/
│   │   └── notes/
│   │       ├── base.html
│   │       ├── note_list.html
│   │       ├── note_form.html
│   │       ├── note_detail.html
│   │       └── note_confirm_delete.html
│   ├── static/
│   │   └── notes/
│   │       └── styles.css
│   └── tests/
│       ├── test_models.py
│       ├── test_views.py
│       └── test_forms.py
│
└── sticky_notes/
├── settings.py
├── urls.py
├── wsgi.py
└── asgi.py


---

## 🧪 Unit Tests

Unit tests are included in:


### Tests cover:

- **Models**
  - `__str__` method returns the note title

- **Views**
  - Create Note (POST)
  - View Notes List (GET)
  - Update Note (POST)

- **Forms**
  - Validation for required fields

To run tests:


All tests pass successfully.
### Python manage.py test
---

## 🧪 Manual Testing Summary

### Create Note
- Added a note with valid title and content  
- Confirmed it appears in the list view  
- Status: **Pass**

### View Notes
- Verified notes display correctly  
- Verified empty list displays without errors  
- Status: **Pass**

### Update Note
- Edited an existing note  
- Confirmed updated content appears  
- Status: **Pass**

### Delete Note
- Deleted a note  
- Confirmed it no longer appears  
- Status: **Pass**

---

## 📝 Design Diagrams

All diagrams are included in the `Diagrams/` folder:

- Use Case Diagram  
- Sequence Diagram  
- Class Diagram  

---

## ▶️ How to Run the Application
### pip install -r requirements.txt

1. Install dependencies:
*(If no requirements file is provided, install Django manually.)*

2. Run migrations:

### manage.py migrate

3. Start the server:

### python manage.py runserver 

4. Open the app:

http://127.0.0.1:8000/ (127.0.0.1 in Bing)


---

## 🔗 GitHub Repository

See `sticky_github.txt` for the project repository link.

---

## 📌 Author

Created by Tammie as part of the AI Bootcamp Django assignment.
