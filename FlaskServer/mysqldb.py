import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    port="33061",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses (id,longitude, latitude, speed, bearing, occupancy_status, updated_at, direction_id) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['longitude'], mbtaDict['latitude'], mbtaDict['speed'], mbtaDict['bearing'], mbtaDict['occupancy_status'], mbtaDict['updated_at'], mbtaDict['direction_id'])
        mycursor.execute(sql, val)

    mydb.commit()