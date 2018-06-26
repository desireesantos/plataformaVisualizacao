import os
import csv
import operator
import collections
from heapq import merge
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_test():
	bodyValues, headerValues = generateData()

	return render_template('datavisualization.html', headerTable=headerValues, 
		bodyTable=bodyValues, names= pathFiles())


def readCSV(file):
	return csv.reader(file, delimiter=';')

def getFiles():
	return [{'name':'./data/acidentes-2000.csv', 'fileNumber': 0 },
	{'name':'./data/acidentes-2016.csv', 'fileNumber': 1 }]

def pathFiles():
	return list(map(lambda file: fileName(file), getFiles()))

def fileName(file):
	return (file.split('./data/'))[1].split('.csv')[0]

def headerNames(table):
	return list(map(lambda headerName: headerName , table.keys()))

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


def generateData():
	tableValues = []
	for number, f in enumerate(getFiles()):
		with open (f, 'r') as file:
			csvFile = readCSV(file)

			if tableValues == []:
				tableTemplate, columns = populateTable(createHeader(csvFile), collections.OrderedDict())
			else:
			  tableTemplate, columns = populateTable(createHeader(csvFile), tableTemplate)
		  
			for i, line in enumerate(csvFile):
					table = tableTemplate

					for j, lineValue in enumerate(line):
							table[columns[j]]= lineValue
											
					tableValues.append({'value': table.copy(), 'fileNumber': number})

					if i >= 10: break
	return tableValues, headerNames(tableTemplate)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)