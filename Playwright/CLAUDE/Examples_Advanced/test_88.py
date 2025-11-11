'''
Example 88: Database Interactions in Tests

Let's test with a SQLite database (simple, no server needed).

New concept: Database operations in tests
What it does:

Creates a test database
Inserts test data via SQL
Queries the database to get test data
Uses that data in UI testing
Cleans up after test

Common pattern:

Setup: Create DB data
Test: Use UI with that data
Verify: Check DB was updated correctly
Teardown: Clean up test data

Expected result: Test creates DB, uses data for login, then cleans up.

pytest tests/test_database.py -v -s
'''

import sqlite3
import os

def test_database_setup_and_verify(page):
    # Step 1: Create test database
    db_path = "test_users.db"
    
    # Clean up if exists
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Create database and table
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT
        )
    """)
    
    # Insert test data
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
                   ("tomsmith", "tom@example.com"))
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
                   ("janedoe", "jane@example.com"))
    
    conn.commit()
    
    # Step 2: Verify data was inserted
    cursor.execute("SELECT * FROM users WHERE username = ?", ("tomsmith",))
    user = cursor.fetchone()
    
    assert user is not None
    assert user[1] == "tomsmith"
    assert user[2] == "tom@example.com"
    
    print(f"Found user: {user[1]} with email {user[2]}")
    
    # Step 3: Use UI to simulate login with DB user
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill(user[1])  # Use DB username
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    
    # Verify login worked
    assert "secure" in page.url
    
    # Cleanup
    conn.close()
    os.remove(db_path)