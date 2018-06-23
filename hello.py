import csv
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
  return render_template('template.html', header_data=header_data(), body_data=body_data(), names= pathFiles())

def header_data():

	header=[]
 	for file in getFiles():
 		with open (file, 'rb') as file:
	  		createHeader(readCSVfile(file), header)

	return sortedHeader(header)


def sortedHeader(columms):
	return sorted(list(set(columms)), key=str.lower)


def readCSVfile(file):
	return csv.reader(file, delimiter=';')


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

def createHeader(first_line, header):
	for line in first_line:
	 		for l in line:
	 				header.append(l)
	 		break
	return header 							

def body_data():
	with open ('./data/acidentes-2000.csv', 'rb') as file:
 			reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
 			rownum = 0
 			body = []

 			for row in reader:
 					if rownum != 0:
	 					body.append(row)
	 				if rownum >= 4:
	 				 	break	
	 				rownum +=1	
 	return body;	

if __name__ == '__main__':
    app.run(debug=True)