# 🎓 Odoo 17 - School Management System

This is a custom module for **Odoo 17** that provides a comprehensive solution for managing school operations. It includes all necessary models, views, reports, security rules, and dashboards needed to run a school digitally.

## 📦 Module Info

- **Name**: School Management System  
- **Version**: 1.0  
- **Category**: Education  
- **Author**: Hamza  
- **License**: LGPL-3  
- **Depends on**: `base`, `web`  
- **Installable**: ✅  
- **Application**: ✅

## ⚙️ Installation Steps

1. Copy the module folder `school_management/` into your Odoo 17 addons directory.

2. Restart Odoo server and update the app list:
   ```bash
   ./odoo-bin -u school_management -d your_database
Search for School Management System in Apps and install it.

📁 Directory Structure
pgsql
Copy
Edit
school_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── class_model.py
│   ├── attendance.py
│   ├── teacher.py
│   ├── course.py
│   └── dashboard.py
├── views/
│   ├── student_views.xml
│   ├── class_views.xml
│   ├── attendance_views.xml
│   ├── teacher_views.xml
│   ├── course_views.xml
│   ├── dashboard_views.xml
│   └── school_menus_actions.xml
├── report/
│   ├── student_report.xml
│   └── attendance_report.xml
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
├── static/
│   └── src/
│       ├── css/
│       │   └── custom_styles.css
│       └── js/
│           └── charts.js
🎯 Features
📚 Student Management – Register, edit, and manage student profiles.

🏫 Class & Course Management – Assign courses to classes and organize subjects.

👩‍🏫 Teacher Management – Manage teachers and their schedules.

📅 Attendance Tracking – Record and manage daily attendance.

📊 Custom Dashboard – Visualize key statistics using charts.

🖨️ PDF Reports – Generate reports for students and attendance.

🧩 Menus & Actions – All views are neatly organized under a custom School menu.

🔐 Security
The module includes the following:

Custom security groups in security/security.xml

Access control rules via ir.model.access.csv

🧾 Manifest File
python
Copy
Edit
{
    'name': 'School Management System',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Comprehensive School Management System',
    'author': 'Hamza',
    'depends': ['base', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/class_views.xml',
        'views/teacher_views.xml',
        'views/course_views.xml',
        'views/attendance_views.xml',
        'views/school_menus_actions.xml',
        'views/dashboard_views.xml',
        'report/student_report.xml',
        'report/attendance_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'school/static/src/css/custom_styles.css',
            'school/static/src/js/charts.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'auto_install': False,
}
🧠 Author
Hamza
📧 Email: hamza@example.com
💼 GitHub: github.com/your_username
