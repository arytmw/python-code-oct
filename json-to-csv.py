import pandas

f = open("sample.json","r")
data = f.read()
f.close()

outputfile = pandas.read_json(data)
outputfile.to_csv('output.csv')
