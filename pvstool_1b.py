import mdfreader as mdf
from scipy.stats import linregress
import matplotlib.pyplot as plt
import os

arquivos = []
for arqv in os.listdir('C:\Users\Rafael Pitta\Documents\Projects\FCAnalysis'):
    if arqv.endswith('.mdf'):
        arquivos.append(arqv)
qtde = len(arquivos)

pedal = [0]*qtde
pvs = [0]*qtde
trend = [0]*qtde
a_trendstr = [0]*qtde
b_trendstr = [0]*qtde
y_trend = [0]*qtde
percentual = [0]*qtde
temp = 0
cnt = 0

pedal_str = 'PTC_PDL_PCT'
pvs_str = 'DELPVS'

for i in arquivos:
	pedal[cnt] = mdf.mdf(i,convertAfterRead=False).getChannelData(pedal_str)
	pvs[cnt] = mdf.mdf(i,convertAfterRead=False).getChannelData(pvs_str)
	cnt += 1

for i in xrange(cnt):
    plt.plot(pvs[i],pedal[i],'bo', ms = '0.7')
    plt.show()
    plt.xlabel(pvs_str + '(V)')
    plt.ylabel(pedal_str + '(%)')
    trend[i] = linregress(pvs[i],pedal[i])
    y_trend[i] = trend[i].intercept + trend[i].slope*pedal[i]
    a_trendstr[i] = repr(trend[i].slope)
    b_trendstr[i] = repr(trend[i].intercept)
    temp = 100*(float(b_trendstr[i]))
    print '\ny = (' + a_trendstr[i] + ') * x + (' + b_trendstr[i] + ')\tfor ' + arquivos[i]
    print 'At x = 0 :',temp,'% of PEDAL at 0V'
