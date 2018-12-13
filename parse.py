def run_parse():
import csv, os, glob

    list_of_files = glob.glob('./temp/*')
    latest_file_location = max(list_of_files, key=os.path.getctime)


    with open(latest_file_location,'r') as csv_file:
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

	return(numdict)
