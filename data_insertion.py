import csv
from database import connect_db

# Function to insert data from CSV files into the database tables
def insertion():
    conn = connect_db()
    cursor = conn.cursor()
    # Insert data into Batches table from batches.csv
    with open('data/batches.csv', 'r') as file:
        contents = csv.reader(file)
        data = list(contents)
        cleaned_data = data[1:]  # Skip header row
        cursor.executemany(
            "INSERT OR IGNORE INTO Batches(batch_id,breed,arrival_date,initial_count) VALUES (?,?,?,?)",
            cleaned_data
          )
        conn.commit()

    # Insert data into FeedRecords table from feed_records.csv
    with open('data/feed_records.csv','r') as file:
        contents = csv.reader(file)
        data = list(contents)
        cleaned_data = data[1:]  # Skip header row
        cursor.executemany(
            "INSERT OR IGNORE INTO FeedRecords(batch_id,date,feed_type,quantity_kg,cost) VALUES(?,?,?,?,?)",cleaned_data
        )
        conn.commit()
    # Insert data into Vaccinations table from vaccinations.csv
    with open('data/vaccinations.csv','r') as file:
        contents = csv.reader(file)
        data = list(contents)
        cleaned_data = data[1:]  # Skip header row
        cursor.executemany("INSERT OR IGNORE INTO Vaccinations(batch_id,date,vaccine_name) VALUES(?,?,?)",cleaned_data
        )
        conn.commit()

    # Insert data into WeightTracking table from weight_tracking.csv
    with open('data/weight_tracking.csv','r') as file:
        contents = csv.reader(file)
        data = list(contents)
        cleaned_data = data[1:]  # Skip header row
        cursor.executemany("INSERT OR IGNORE INTO WeightTracking(batch_id,date,avg_weight_kg) VALUES(?,?,?)",cleaned_data)
        conn.commit()
    
    # Insert data into Sales table from sales.csv
    with open('data/sales.csv','r') as file:
        contents = csv.reader(file)
        data = list(contents)
        cleaned_data = data[1:]  # Skip header row
        cursor.executemany("INSERT OR IGNORE INTO Sales(batch_id,date,quantity,avg_weight_kg,rate_per_kg,total_amount) VALUES(?,?,?,?,?,?)",cleaned_data)
        conn.commit()

# Run the insertion function if this script is executed directly
if __name__ == "__main__":
    insertion()
