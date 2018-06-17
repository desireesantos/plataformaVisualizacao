import csv
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
  return render_template('template.html', header_data=header_data(), body_data=body_data(), name="acidentes-2000 | acidentes-2016")

def header_data():
	header = []
	files = ['./data/acidentes-2000.csv', './data/acidentes-2016.csv']

 	for file in files:
 			with open (file, 'rb') as file:
 				reader = csv.reader(file, delimiter=';')
 			
	 			for row in reader:
	 					for r in row:
	 						header.append(r)
	 					break			
	 		
	return header;

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