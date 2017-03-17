import matplotlib.pyplot as plt
import analysis_functions as af
import sys

def plotting_xy(data):
	for i in xrange(len(data)):
	
		plt.plot(data[i][x_str]['data'], data[i][y_str]['data'], 'bo', ms = '0.7')
		plt.xlabel(x_str + '(' + str(data[i][x_str]['unit']) + ')')
		plt.ylabel(y_str + '(' + str(data[i][y_str]['unit']) + ')')
		plt.show()
	
		af.regression(data[i][x_str]['data'], data[i][y_str]['data'], arquivos[i])

while True:
	dat, arquivos = af.read_files()

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
