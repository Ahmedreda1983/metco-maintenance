import sqlite3

# الاتصال بقاعدة البيانات بالاسم الصحيح المستخدم في app.py
conn = sqlite3.connect('data.db')
c = conn.cursor()

# إنشاء جدول الصيانة الرئيسي
c.execute('''
CREATE TABLE IF NOT EXISTS maintenance_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    sheet_name TEXT,
    row_index INTEGER,
    data TEXT,
    timestamp TEXT,
    before_images TEXT,
    after_images TEXT,
    report_images TEXT,
    cm_images TEXT,
    notes_text TEXT,
    notes_images TEXT
)
''')

# إنشاء جدول zip_files لتخزين ملفات ZIP كـ BLOB
c.execute('''
CREATE TABLE IF NOT EXISTS zip_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    content BLOB
)
''')

conn.commit()
conn.close()

print("✅ تم إنشاء قاعدة البيانات data.db بجدولي maintenance_records و zip_files بنجاح.")
