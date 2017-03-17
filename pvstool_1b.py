import mdfreader as mdf
from scipy.stats import linregress
import matplotlib.pyplot as plt
import os

arquivos = []
for arqv in os.listdir('D:\users\F65605B\Documents\Rafael Pitta\A Python Directory\PyData'):
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
for i in arquivos:
	pedal[cnt] = mdf.mdf('PyData/' + i,convertAfterRead=False).getChannelData('PTC_PDL_PCT')
	pvs[cnt] = mdf.mdf('PyData/' + i,convertAfterRead=False).getChannelData('LV2_PVS_NORM')
	cnt += 1

for i in xrange(cnt):
    plt.plot(pvs[i],pedal[i],'bo', ms = '0.7')
    plt.show()
    plt.xlabel('LV2_PVS_NORM (V)')
    plt.ylabel('PTC_PDL_PCT (%)')
    trend[i] = linregress(pvs[i],pedal[i])
    y_trend[i] = trend[i].intercept + trend[i].slope*pedal[i]
    a_trendstr[i] = repr(trend[i].slope)
    b_trendstr[i] = repr(trend[i].intercept)
    temp = 100*(float(b_trendstr[i]))
    print '\ny = (' + a_trendstr[i] + ') * x + (' + b_trendstr[i] + ')\tfor ' + arquivos[i]
    print 'At x = 0 :',temp,'% of PEDAL at 0V'