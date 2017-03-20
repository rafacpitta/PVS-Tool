import matplotlib.pyplot as plt
import mdfreader as mdf
from scipy.stats import linregress
import os
import sys

def read_files():
	
	filenames = []
	files = []
	
	for i in os.listdir('Files'):
		if i.endswith('.mdf') or i.endswith('.dat'):
			filenames.append(i)
	
	os.chdir('Files')
	for i in filenames:
		f = mdf.mdf(i)
		files.append(f)
	os.chdir('..')
	
	return files, filenames
	
def regression(x,y,f):
	
	trend = linregress(x, y)
	y_trend = trend.intercept + trend.slope*y
	temp = 100*trend.intercept
	print '\ny = (' + str(trend.slope) + ') * x + (' + str(trend.intercept) + ')\tfor ' + f

def plotting_xy(data,x,y):
	
	for i in xrange(len(data)):
	
		try:
			plt.plot(data[i][x]['data'], data[i][y]['data'], 'bo', ms = '0.7')
			plt.xlabel(x + '(' + data[i][x]['unit'] + ')')
			plt.ylabel(y + '(' + data[i][y]['unit'] + ')')
			plt.show()
	
			regression(data[i][x_str]['data'], data[i][y_str]['data'], arquivos[i])
		except:
			print 'Variables with different raster'
			sys.exit()

#while True:
data, arquivos = read_files()

x_str = str(raw_input('\nType X axis variable: ')).upper()
y_str = str(raw_input('Type Y axis variable: ')).upper()

data[0].resample()
crit = []
j = 0
fcrit = open('critical.txt','w')

for i in xrange(data[0][x_str]['data'].shape[0]):
	if (1.33 < data[0][x_str]['data'][i] < 1.36) and (0.50 < data[0][y_str]['data'][i] < 0.52):
		crit.append(i)
		j += 1
		fcrit.write(str(i) + '\n')

fcrit.close()
plotting_xy(data,x_str,y_str)
	
"""	while True:
		choice = str(raw_input('\nDo you want to plot again? (Y/N) ')).lower()
		
		if choice == 'n':
			sys.exit()
			
		if choice == 'y':
			break
			
		else:
			print '\nAnswer just y for YES or n for NO!'
			continue"""


