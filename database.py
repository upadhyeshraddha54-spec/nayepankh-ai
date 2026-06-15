import sqlite3

conn = sqlite3.connect("campaigns.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    location TEXT,
    date TEXT,
    time TEXT,
    venue TEXT,
    content TEXT
)
""")

conn.commit()

def save_campaign(topic, location, date, time, venue, content):

    cursor.execute("""
    INSERT INTO campaigns
    (topic, location, date, time, venue, content)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (topic, location, date, time, venue, content))

    conn.commit()

def get_campaigns():

    cursor.execute("""
    SELECT * FROM campaigns
    ORDER BY id DESC
    """)

    return cursor.fetchall()


conn.commit()
# =========================
# VOLUNTEERS TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS volunteers (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    email TEXT,

    phone TEXT,

    city TEXT,

    skills TEXT,

    campaign TEXT
)
""")

conn.commit()
get_campaigns()
# =========================
# SAVE VOLUNTEER
# =========================

def save_volunteer(
    name,
    email,
    phone,
    city,
    skills,
    campaign
):

    cursor.execute("""
    INSERT INTO volunteers
    (name, email, phone, city, skills, campaign)

    VALUES (?, ?, ?, ?, ?, ?)
    """,

    (
        name,
        email,
        phone,
        city,
        skills,
        campaign
    ))

    conn.commit()


# =========================
# GET VOLUNTEERS
# =========================

def get_volunteers():

    cursor.execute("""
    SELECT * FROM volunteers
    ORDER BY id DESC
    """)

    return cursor.fetchall()