import cx_Oracle

conn = cx_Oracle.connect('test/system@//localhost:1521/orcl')
print(conn.version)

cur = conn.cursor()

sql_create="""
CREATE TABLE chartered_flight(flight_no NUMBER(4) PRIMARY KEY
, customer_id NUMBER(6) REFERENCES customer(customer_id)
, aircraft_no NUMBER(4) REFERENCES aircraft(aircraft_no)
, flight_type VARCHAR2 (12)
, flight_date DATE NOT NULL
, flight_time INTERVAL DAY TO SECOND NOT NULL
, takeoff_at CHAR (3) NOT NULL
, destination CHAR (3) NOT NULL)
"""
cur.execute(sql_create)
print('table created.')
