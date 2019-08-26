import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#opening the file

df1 = pd.read_excel('India_Imports_2011-12_And_2012-13.xls')	#reading import file

df2 = pd.read_excel('India_Exports_2011-12_And_2012-13.xls')	#reading export file

writer=open('table.tex','w')

#top five import and export destination by total import and export (based on value)


op1=df1.groupby('Country').agg({'Value-INR-2011-12':'sum'})		#grouping sum of values of ech country

op2=df2.groupby('Country').agg({'Value-INR-2011-12':'sum'})


op1=op1.reset_index()
op2=op2.reset_index()

op1=op1.nlargest(5, 'Value-INR-2011-12' )		#extraction top 5 values from the results
op2=op2.nlargest(5, 'Value-INR-2011-12' )



#for import
total=df1['Value-INR-2011-12'].sum()
sum1=op1['Value-INR-2011-12'].sum()

other=total-sum1				#calculating sum of other countries
op1.loc[5]=['Others',other]

slices=op1['Value-INR-2011-12']

country=op1['Country']

plt.pie(slices, labels=country)


plt.title('Top 5 Country pie chart for import of year 2011-12')


plt.savefig('image1.jpg', bbox_inches='tight')
plt.clf()

#for export

total=df2['Value-INR-2011-12'].sum()
sum2=op2['Value-INR-2011-12'].sum()

other=total-sum2				#calculating sum of other countries
op2.loc[5]=['Others',other]

slices=op2['Value-INR-2011-12']

country=op2['Country']

plt.pie(slices, labels=country)


plt.title('Top 5 Country pie chart for export of year 2011-12')


plt.savefig('image2.jpg', bbox_inches='tight')
plt.clf()


#bar chart for top 5 commodity
com1=df1.groupby('Commodity').agg({'Value-INR-2011-12':'sum'})				#grouping sum of values of ech country

com2=df2.groupby('Commodity').agg({'Value-INR-2011-12':'sum'})

com1=com1.reset_index()						#resettin index of both
com2=com2.reset_index()

com1=com1.nlargest(5, 'Value-INR-2011-12' )			#returning commodities with top 5 values
com2=com2.nlargest(5, 'Value-INR-2011-12' )

com1=com1.reset_index()						#resettin index of both
com2=com2.reset_index()

#for import

x=com1.index
y=com1['Value-INR-2011-12']



plt.bar(x,y, label='bar1', color='r')
plt.xticks(x, com1['Commodity'],rotation='vertical')
plt.title('Import bar chart of commodity of year 2011-12')

plt.xlabel('Commodity')
plt.ylabel('Value-INR-2011-12')
plt.savefig('image3.jpg', bbox_inches='tight')
plt.clf()

#for export
x=com2.index
y=com2['Value-INR-2011-12']



plt.bar(x,y, label='bar1', color='c')
plt.xticks(x, com2['Commodity'],rotation='vertical')
plt.title('Export bar chart of commodity of year 2011-12')

plt.xlabel('Commodity')
plt.ylabel('Value-INR-2011-12')
plt.savefig('image4.jpg', bbox_inches='tight')
plt.clf()


#linegraph of 'TEA' between quantity and value , plotted for  stat of  each coountry

tea1=df1[df1['Commodity']=='TEA']
tea2=df2[df2['Commodity']=='TEA']

#import

tea1=tea1.sort_values(['Quantity-2011-12'])

plt.plot(tea1['Quantity-2011-12'],tea1['Value-INR-2011-12'],label='Year 2011-12')

tea1=tea1.sort_values(['Quantity-2012-13'])

plt.plot(tea1['Quantity-2012-13'],tea1['Value-INR-2012-13'], label='Year 2012-13')

plt.title('Import plot for TEA')

plt.xlabel('quantity')
plt.ylabel('value')
plt.legend()
plt.savefig('image5.jpg', bbox_inches='tight')
plt.clf()

#export

tea2=tea2.sort_values(['Quantity-2011-12'])

plt.plot(tea2['Quantity-2011-12'],tea2['Value-INR-2011-12'],label='Year 2011-12')

tea2=tea2.sort_values(['Quantity-2012-13'])

plt.plot(tea2['Quantity-2012-13'],tea2['Value-INR-2012-13'], label='Year 2012-13')

plt.title('Export plot for TEA')

plt.xlabel('quantity')
plt.ylabel('value')
plt.legend()
plt.savefig('image6.jpg', bbox_inches='tight')
plt.clf()


#Scatterplot of 'RICE' between quantity and value , plotted for  stat of  each coountry

rice1=df1[df1['Commodity']=='TEA']
rice2=df2[df2['Commodity']=='TEA']

#import

rice1=rice1.sort_values(['Quantity-2011-12'])

plt.scatter(rice1['Quantity-2011-12'],rice1['Value-INR-2011-12'],label='Year 2011-12' , marker='x',s=10)

rice1=rice1.sort_values(['Quantity-2012-13'])

plt.scatter(rice1['Quantity-2012-13'],rice1['Value-INR-2012-13'], label='Year 2012-13',marker='o',s=10)

plt.title('Import scatter plot for RICE')

plt.xlabel('quantity')
plt.ylabel('value')
plt.legend()
plt.savefig('image7.jpg', bbox_inches='tight')
plt.clf()

#Export

rice2=rice2.sort_values(['Quantity-2011-12'])

plt.scatter(rice2['Quantity-2011-12'],rice2['Value-INR-2011-12'],label='Year 2011-12' , marker='x',s=10)

rice2=rice2.sort_values(['Quantity-2012-13'])

plt.scatter(rice2['Quantity-2012-13'],rice2['Value-INR-2012-13'], label='Year 2012-13',marker='o',s=10)

plt.title('Export scatter plot for RICE')

plt.xlabel('quantity')
plt.ylabel('value')
plt.legend()
plt.savefig('image8.jpg', bbox_inches='tight')
plt.clf()


#histogram
com1=df1.groupby('Country').agg({'Value-INR-2011-12':'sum'})				#grouping sum of values of ech country

com2=df2.groupby('Country').agg({'Value-INR-2011-12':'sum'})

com1=com1.reset_index()						#resettin index of both
com2=com2.reset_index()

#for import


y=com1['Value-INR-2011-12']



plt.hist(y , color='y',histtype='bar', rwidth=0.7)
#plt.xticks(x, com1['Commodity'],rotation='vertical')
plt.title('Import histogram of commodity of year 2011-12')

plt.xlabel('Range of value')
plt.ylabel('Number of countries ')
plt.savefig('image9.jpg', bbox_inches='tight')
plt.clf()

#for export


y=com2['Value-INR-2011-12']



plt.hist(y , color='b',histtype='bar', rwidth=0.7)
#plt.xticks(x, com1['Commodity'],rotation='vertical')
plt.title('Export histogram of commodity of year 2011-12')

plt.xlabel('Range of value')
plt.ylabel('Number of countries ')
plt.savefig('image10.jpg', bbox_inches='tight')
plt.clf()


#table to latex file
tea1=tea1.reset_index()	
tea1.to_latex(writer)
