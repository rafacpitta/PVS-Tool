import matplotlib.pyplot as plt
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
		f = mdf.mdf(i,convertAfterRead=False)
		files.append(f)
	os.chdir('..')
	
	return files, filenames
	
def regression(x,y,f):
	
	trend = linregress(x, y)
	y_trend = trend.intercept + trend.slope*y
	temp = 100*(float(trend.intercept))
	print '\ny = (' + str(trend.slope) + ') * x + (' + str(trend.intercept) + ')\tfor ' + f

def plotting_xy(data):
	for i in xrange(len(data)):
	
		try:
			plt.plot(data[i][x_str]['data'], data[i][y_str]['data'], 'bo', ms = '0.7')
			plt.xlabel(x_str + '(' + str(data[i][x_str]['unit']) + ')')
			plt.ylabel(y_str + '(' + str(data[i][y_str]['unit']) + ')')
			plt.show()
	
			regression(data[i][x_str]['data'], data[i][y_str]['data'], arquivos[i])
		except:
			print 'Variables with different raster'
			sys.exit()

while True:
	dat, arquivos = read_files()

	x_str = str(raw_input('\nType X axis variable: ')).upper()
	y_str = str(raw_input('Type Y axis variable: ')).upper()

	plotting_xy(dat)
	
	while True:
		choice = str(raw_input('\nDo you want to plot again? (Y/N) ')).lower()
		
		if choice == 'n':
			sys.exit()
			
		if choice == 'y':
			break
			
		else:
			print '\nAnswer just y for YES or n for NO!'
			continue

