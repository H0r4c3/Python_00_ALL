'''
Example 89: Database Fixture (Reusable DB Setup)
Let's make database setup reusable with fixtures!

New concept: Database fixture for reusable setup
What it does:

test_db fixture creates database once per test
yield conn provides database connection to test
After test completes, cleanup happens automatically
No more duplicate DB setup code!
Multiple tests can use the same fixture

Expected result: All 3 tests pass, each gets fresh database!
'''

# Update tests/conftest.py (add to existing content):
'''
import pytest
import sqlite3
import os

@pytest.fixture
def test_db():
    """Creates a test database with sample data"""
    db_path = "test_users.db"
    
    # Setup: Create database
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            is_active INTEGER
        )
    """)
    
    # Insert test data
    test_users = [
        ("tomsmith", "tom@example.com", 1),
        ("janedoe", "jane@example.com", 1),
        ("inactive_user", "inactive@example.com", 0)
    ]
    
    cursor.executemany("INSERT INTO users (username, email, is_active) VALUES (?, ?, ?)", 
                       test_users)
    conn.commit()
    
    # Yield connection to test
    yield conn
    
    # Teardown: Cleanup after test
    conn.close()
    if os.path.exists(db_path):
        os.remove(db_path)
'''



def test_active_users_only(test_db):
    """Test that only active users can be retrieved"""
    cursor = test_db.cursor()
    
    # Query active users
    cursor.execute("SELECT username FROM users WHERE is_active = 1")
    active_users = cursor.fetchall()
    
    assert len(active_users) == 2
    usernames = [user[0] for user in active_users]
    assert "tomsmith" in usernames
    assert "janedoe" in usernames
    assert "inactive_user" not in usernames
    
    print(f"Active users: {usernames}")

def test_user_count(test_db):
    """Test total user count"""
    cursor = test_db.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    
    assert count == 3
    print(f"Total users in DB: {count}")

def test_login_with_db_user(test_db, page):
    """Test UI login using DB user data"""
    cursor = test_db.cursor()
    
    # Get user from database
    cursor.execute("SELECT username, email FROM users WHERE username = ?", ("tomsmith",))
    user = cursor.fetchone()
    
    # Use in UI test
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill(user[0])
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    
    assert "secure" in page.url
    print(f"Successfully logged in with DB user: {user[0]}")