def read_files():
	import os
	import mdfreader as mdf
	
	filenames = []
	files = []
	
	for i in os.listdir('Files'):
		if i.endswith('.mdf'):
			filenames.append(i)
	
	os.chdir('Files')
	for i in filenames:
		f = mdf.mdf(i,convertAfterRead=False)
		files.append(f)
	os.chdir('..')
	
	return files, filenames
	
def regression(pv,pdl,f):
	from scipy.stats import linregress
	
	trend = linregress(pv, pdl)
	y_trend = trend.intercept + trend.slope*pdl
	temp = 100*(float(trend.intercept))
	print '\ny = (' + str(trend.slope) + ') * x + (' + str(trend.intercept) + ')\tfor ' + f
