import pymysql


connection = pymysql.connect(host="localhost",user="root",passwd="",database="databaseName" )

shoptablesql="""CREATE TABLE Data(p_id,p_name,p_price,p_quantity,p_mdate,p_edate)"""

cursor = connection.cursor()
connection.close()

