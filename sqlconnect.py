def runQuery(sql_query):

	import mysql.connector

	cnx = mysql.connector.connect(user='program',
	    password='Prog1234!',
	    host='metro.c0ua8qyyzir2.us-east-1.rds.amazonaws.com',
	    database='metrodinerdb')
	cur = cnx.cursor()
	# example of the query
	#sql_query = "Select * from Report_T WHERE ReportDate BETWEEN \"2017-01-01\" AND \"2017-01-05\""
	cur.execute(sql_query)
	result = []
	columns = tuple( [d[0].decode('utf8') for d in cur.description] )
	for row in cur:
	  result.append(dict(zip(columns, row)))
	return(result)
	cur.close()
	cnx.close()
