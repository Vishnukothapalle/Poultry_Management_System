import csv
from database import connect_db

# Function to perform analysis and export results to CSV files
def analysis():
    conn = connect_db()
    cursor = conn.cursor()

    # Export batch feed records to CSV
    with open('outcomes/Batch_feed_records.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['batch_id', 'breed', 'date', 'feed_type', 'quantity_kg'])  # Add header
        cursor.execute("""SELECT b.batch_id, b.breed, f.date, f.feed_type, f.quantity_kg 
                          FROM Batches b 
                          JOIN FeedRecords f 
                          ON b.batch_id = f.batch_id ORDER BY b.batch_id""")
        result = cursor.fetchall()
        for row in result:
            writer.writerow(row)

    # Export vaccination records to CSV
    with open('outcomes/Vaccination_records.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['batch_id','breed','vaccine_name','date'])
        cursor.execute("""SELECT b.batch_id,b.breed,v.vaccine_name,v.date
                          FROM Batches b 
                          JOIN Vaccinations v
                          ON b.batch_id = v.batch_id""")
        result = cursor.fetchall()
        for row in result:
            writer.writerow(row)
    
    # Export weight tracking records to CSV
    with open('outcomes/WeightTacking_records.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['batch_id','breed','date','avg_weight'])
        cursor.execute("""SELECT b.batch_id,b.breed,w.date,w.avg_weight_kg
                          FROM Batches b
                          JOIN WeightTracking w
                          ON b.batch_id = w.batch_id ORDER BY b.batch_id""")
        result = cursor.fetchall()
        for row in result:
            writer.writerow(row)
    
    # Export sales records to CSV
    with open('outcomes/Sales_records.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['batch_id','breed','date','quantity','total_amount'])
        cursor.execute("""SELECT s.batch_id, b.breed, s.date, s.quantity, s.total_amount
                          FROM Sales s
                          JOIN Batches b
                          ON s.batch_id = b.batch_id""")
        result = cursor.fetchall()
        for row in result:
            writer.writerow(row)
    
    # Export feed consumption summary to CSV
    with open('outcomes/Feed_consumption.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['batch_id','consumption'])
        cursor.execute("""SELECT batch_id, SUM(quantity_kg) AS total_feed
                          FROM FeedRecords
                          GROUP BY batch_id""")
        result = cursor.fetchall()
        for row in result:
            writer.writerow(row)
    
    # Export combined batch results to CSV
    with open('outcomes/Batch_results.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['batch_id','breed','feed_date','feed_quantity','weight_date','avg_weight','sales_date','sales_quantity'])
        cursor.execute("""SELECT b.batch_id, b.breed, f.date AS feed_date, f.quantity_kg, w.date AS weight_date, w.avg_weight_kg, s.date AS sales_date, s.quantity
                        FROM Batches b
                        LEFT JOIN FeedRecords f ON b.batch_id = f.batch_id
                        LEFT JOIN WeightTracking w ON b.batch_id = w.batch_id
                        LEFT JOIN Sales s ON b.batch_id = s.batch_id""")
        result = cursor.fetchall()
        for row in result:
            writer.writerow(row)

# Run the analysis function if this script is executed directly
if __name__ == "__main__":
    analysis()