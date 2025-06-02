import sqlite3

# Establishes a connection to the SQLite database
def connect_db():
    return sqlite3.connect('poultry.db')

# Creates all necessary tables for the poultry farm management system
def table_creation():
    conn = connect_db()
    cursor = conn.cursor()

    # Create Birds batch table to store batch details
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Batches (
        batch_id TEXT PRIMARY KEY,
        breed TEXT,
        arrival_date TEXT,
        initial_count INTEGER
    );
    """)

    # Create Feed records table to log feed usage and costs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FeedRecords (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        batch_id TEXT,
        date TEXT,
        feed_type TEXT,
        quantity_kg REAL,
        cost REAL,
        FOREIGN KEY (batch_id) REFERENCES Batches(batch_id)
    );
    """)

    # Create Vaccination table to track vaccinations for each batch
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vaccinations (
        vaccination_id INTEGER PRIMARY KEY AUTOINCREMENT,
        batch_id TEXT,
        date TEXT,
        vaccine_name TEXT,
        FOREIGN KEY (batch_id) REFERENCES Batches(batch_id)
    );
    """)

    # Create Weight Tracking table to monitor average weight of birds in each batch
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS WeightTracking (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        batch_id TEXT,
        date TEXT,
        avg_weight_kg REAL,
        FOREIGN KEY (batch_id) REFERENCES Batches(batch_id)
    );
    """)

    # Create Sales table to record sales transactions for each batch
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        batch_id TEXT,
        date TEXT,
        quantity INTEGER,
        avg_weight_kg REAL,
        rate_per_kg REAL,
        total_amount REAL,
        FOREIGN KEY (batch_id) REFERENCES Batches(batch_id)
    );
    """)

    conn.commit()
    conn.close()
    print("tables created sucessfully")