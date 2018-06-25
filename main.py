import os
import csv
import collections
from heapq import merge
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_test():
	header, body = body_data()
	return render_template('template.html', header_data=header, body_data=body, names= pathFiles())

def header_data():
	headerValues=[]
	for f in getFiles():
		with open (f, 'r') as file:
			headerValues = createHeader(readCSVfile(file))
	return headerValues

def readCSVfile(file):
	return csv.reader(file, delimiter=';')

def sortedHeader(columms):
	return list(set(columms))

def getFiles():
	return ['./data/acidentes-2000.csv', './data/acidentes-2016.csv']

def pathFiles():
	names = []
	for file in getFiles():
		names.append(fileName(file))
	return names

def fileName(file):
	name = (file.split('./data/'))[1]
	return name.split('.csv')[0]  

def createHeader(first_line):
	header = list()

	for line in first_line:
		for l in line:
			header.append(l)
		break
	return header

def populateTable(header, tableValues):
	columns = []
	if (len(header) != 0):
					for h in header:
							tableValues[header[ header.index(h)] ] = ""
							columns.append(h)

	return tableValues, columns

def getTableHeader(table):
	value = []
	for key, value in table.items():
	   value.append(key)
	return value

def body_data():
	tableValues = []
	for f in getFiles():
		with open (f, 'r') as file:
		
			csvFile = readCSVfile(file)

			if tableValues == []:
				tableTemplate, columns = populateTable(createHeader(csvFile), collections.OrderedDict())
			else:
			  tableTemplate, columns = populateTable(createHeader(csvFile), tableTemplate)
		  
			for i, line in enumerate(csvFile):
					table = tableTemplate

					for j, lineValue in enumerate(line):
							table[columns[j]]= lineValue
											
					tableValues.append(table.copy())

					if i >= 10: break
	return tableValues, getTableHeader(tableTemplate)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)