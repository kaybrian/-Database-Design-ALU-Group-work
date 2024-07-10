import pandas as pd
import psycopg2

# Load the dataset
file_path = './water_potability.csv'
water_data = pd.read_csv(file_path)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="water_quality_db",
    user="alu",
    password="123456789",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert data into WaterQuality table and get the id for each row
for index, row in water_data.iterrows():
    cur.execute("""
        INSERT INTO WaterQuality (ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
        """,
        (row['ph'], row['Hardness'], row['Solids'], row['Chloramines'], row['Sulfate'], row['Conductivity'], row['Organic_carbon'], row['Trihalomethanes'], row['Turbidity'])
    )
    water_quality_id = cur.fetchone()[0]

    # Insert data into WaterPotability table
    cur.execute("""
        INSERT INTO WaterPotability (water_quality_id, Potability)
        VALUES (%s, %s)
        """,
        (water_quality_id, row['Potability'])
    )

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
