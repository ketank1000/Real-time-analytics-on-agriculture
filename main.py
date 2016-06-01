from bs4 import BeautifulSoup
import lxml
import urllib
import re
#from pylab import *
import matplotlib.pyplot as plt
import numpy as np
#import plotly.plotly as py

link = "http://ketan.net16.net/"
f = urllib.urlopen(link)           
html = f.read()  
soup = BeautifulSoup(html,'lxml')
flag=0

table=soup.find_all('td')
cr_n=''
cr_r=0
cr_i=0
cr_rate={}
cr_init={}
for l in table:
    if(flag==0):
        cr_n=str(l.decode_contents(formatter="html"))
        flag=1
    elif(flag==1):
        cr_r=int(l.decode_contents(formatter="html"))
        flag=2
        cr_rate.update({cr_n:cr_r})
    elif(flag==2):
        cr_i=int(l.decode_contents(formatter="html"))
        flag=0
        cr_init.update({cr_n:cr_i})

cr_f=open('crop_info.txt','r')
text=cr_f.read(150)
print text
l=re.split(' |\n',text)

while '' in l:
    l.remove('')

cr_dur={}
cr_yield={}
cr_profit={}
i=0
while(i<len(l)):
    t1=str(l[i])
    t2=int(l[i+1])
    t3=int(l[i+2])
    cr_dur.update({t1:t2})
    cr_yield.update({t1:t3})
    i=i+3
cr_f.close()
init_a=int(input('Enter Bank Balance: '))
init_t=int(input('Enter Duration: '))

try:
	print "Crop\tInvestment\tProfit"
	for key in cr_rate:
		if(cr_init[key]<=init_a and cr_dur[key]<=init_t):
			t1=(cr_rate[key]*cr_yield[key])
			#print t1
			cr_profit.update({key:t1})
			print key+'\t'+str(cr_init[key])+'\t'+str(t1)

	n_groups = len(cr_profit)

	pr = cr_profit.values()


	fig, ax = plt.subplots()

	index = np.arange(n_groups)
	bar_width = 0.2

	rects1 = ax.bar(index, pr, bar_width,color='b',label='crops profit')

	ax.set_xlabel('crops')
	ax.set_ylabel('profit in Rs')
	ax.set_title('Crops profit')
	#ax.set_xticks(n_groups + bar_width)
	ax.set_xticklabels(cr_profit.keys())

	ax.legend()

	plt.show()
	#print cr_rate,cr_dur,cr_yield,cr_profit
except Exception, e:
	print 'no crop found'
