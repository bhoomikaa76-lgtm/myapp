import mysql.connector
from flask import Flask, render_template
app = Flask(__name__)

def get_products1():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2005",   # Replace with your MySQL password
        database="product"          # Your database name
    )

    
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT id, name, price FROM products1")

    # Step 13: Fetch All Rows
    rows = cur.fetchall()

    # Step 14: Close Cursor and Connection
    cur.close()
    conn.close()

    # Step 15: Return the Data
    return rows

# Step 16: Create Home Route
@app.route("/")

def home():

    return render_template("index.html", products1=get_products1())

if __name__ == "__main__":
    app.run(debug=True)