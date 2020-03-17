# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106081021.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
   		data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.









# my code
#=================
#for i in data[:10]:
#	if (data[i]['PRES']== -99.000 or data[i]['PRES']== -999.000 ): del(data[i])


#for i in data[0:3]:
#	del(i)
	#i.remove('PRES')

#for i in range(0, 2):
	#if data[i]['PRES']== '-99.000' or data[i]['PRES']== '-999.000' :
	#	data.pop(i)
#	print(data[i]['PRES'])


#for i in data:	
#	if i['PRES']=='-99.000' or i['PRES']=='-999.000':
#		data.remove(i)



#for i in range(len(data)):
#	if data[i]["PRES"]=='-99.000':
#		print(i)
#		data.pop(i)
	

	
#list(data.keys())

#filter -99, -999, and the five station
target_data = list(filter(lambda item: item['PRES'] != '-99.000',data))  
target_data = list(filter(lambda item: item['PRES'] != '-999.000',target_data))
station_C0A880  = list(filter(lambda item: item['station_id']=='C0A880',target_data))
station_C0F9A0 = list(filter(lambda item: item['station_id']=='C0F9A0', target_data))
station_C0G640 = list(filter(lambda item: item['station_id']=='C0G640', target_data))
station_C0R190 = list(filter(lambda item: item['station_id']=='C0R190', target_data))
station_C0X260 = list(filter(lambda item: item['station_id']=='C0X260', target_data))

#start calculating
C0A880=0
if(len(station_C0A880)==0):
	C0A880='None'
else:
	for i in range(len(station_C0A880)):
		C0A880=C0A880+float (station_C0A880[i]['PRES'])
	C0A880=C0A880/len(station_C0A880)
	
C0F9A0=0
if(len(station_C0F9A0)==0):
	C0F9A0='None'
else:
	for i in range(len(station_C0F9A0)):
		C0F9A0=C0F9A0+float (station_C0F9A0[i]['PRES'])
	C0F9A0=C0F9A0/len(station_C0F9A0)
	

C0G640=0
if(len(station_C0G640)==0):
	C0G640='None'
else:
	for i in range(len(station_C0G640)):
		C0G640=C0G640+float (station_C0G640[i]['PRES'])
	C0G640=C0G640/len(station_C0G640)
	

C0R190=0
if(len(station_C0R190)==0):
	C0R190='None'
else:
	for i in range(len(station_C0R190)):
		C0R190=C0R190+float (station_C0R190[i]['PRES'])
	C0R190=C0R190/len(station_C0R190)
	

C0X260=0
if(len(station_C0X260)==0):
	C0X260='None'
else:
	for i in range(len(station_C0X260)):
		C0X260=C0X260+float (station_C0X260[i]['PRES'])
	C0X260=C0X260/len(station_C0X260)
	

a=[ ['C0A880', C0A880],['C0F9A0', C0F9A0],['C0G640', C0G640],['C0R190', C0R190],['C0X260', C0X260]]

#C0X260=0
#for i in range(len(station_C0X260)):
#	C0X260=C0X260+float (station_C0X260[i]['PRES'])
#C0X260=C0X260/len(station_C0X260)



#target_data = data[:10]
#=================








#=======================================

# Part. 4
#=======================================
# Print result
#print(target_data)
print(a)

#print(len(data))
#========================================