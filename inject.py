def inject_sql(latest_txt):
    import csv
    import mysql.connector
    from mysql.connector import Error
    from mysql.connector import errorcode
    from datetime import datetime

    with open(latest_txt,'r') as csv_file:
    	csv_reader = csv.reader(csv_file, delimiter='=')

    	numdict = {"Net_Sales": "0",
    			   "Cash": "0",
    			   "Deposit": "0",
    			   "OVER/SHORT": "0",
    			   "Voids": "0",
    			   "Food": "0",
    			   "Retail": "0",
    			   "Total_Tips": "0",
    			   "Tip_Pull": "0",
    			   "Total_Discounts": "0",
    			   }

    	for line in csv_reader:
    		if 'Cash ' in line:
    			numdict["Cash"] = line[1]
    		if 'Voids ' in line:
    			numdict["Voids"] = line[1]
    		if 'Deposit ' in line:
    			numdict["Deposit"] = line[1]
    		if 'OVER/SHORT ' in line:
    			numdict["OVER/SHORT"] = line[1]
    		if 'Food ' in line:
    			numdict["Food"] = line[1]
    		if 'Retail ' in line:
    			numdict["Retail"] = line[1]
    		if 'Total Tips ' in line:
    			numdict["Total_Tips"] = line[1]
    		if 'Tip Pull ' in line:
    			numdict["Tip_Pull"] = line[1]
    		if 'Net Sales ' in line:
    			numdict["Net_Sales"] = line[1]
    		if 'Total Discounts ' in line:
    			numdict["Total_Discounts"] = line[1]

    try:
       connection = mysql.connector.connect(host='metro.c0ua8qyyzir2.us-east-1.rds.amazonaws.com',
                                 database='metrodinerdb',
                                 user='program',
                                 password='Prog1234!')

       cursor = connection.cursor(prepared=True)

       sql_insert_date_query = """REPLACE INTO `Report_T`
                              (`ReportDate`, `Cash`, `Voids`, `Deposit`, `OVER/SHORT`, `Food`, `Retail`, `Total_Tips` ,`Tip_Pull`, `Net_Sales`, `Total_Discounts`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

       current_Date = datetime.now()
       formatted_date = current_Date.strftime('%Y-%m-%d')
       insert_tuple = (
       formatted_date,
       numdict["Cash"],
       numdict["Voids"],
       numdict["Deposit"],
       numdict["OVER/SHORT"],
       numdict["Food"],
       numdict["Retail"],
       numdict["Total_Tips"],
       numdict["Tip_Pull"],
       numdict["Net_Sales"],
       numdict["Total_Discounts"])

       result  = cursor.execute(sql_insert_date_query,insert_tuple)
       connection.commit()
       print ("Date Record inserted successfully into report table")

    except mysql.connector.Error as error :
        print("Failed inserting date object into MySQL table {}".format(error))

    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
