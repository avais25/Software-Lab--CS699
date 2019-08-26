import pandas as pd
import numpy as np


#opening the file

df1 = pd.read_excel('India_Imports_2011-12_And_2012-13.xls')	#reading import file

df2 = pd.read_excel('India_Exports_2011-12_And_2012-13.xls')	#reading export file

writer = pd.ExcelWriter('173050043_solution.xls',engine = 'xlwt')	#creating writer object for output

#top five import and export destination by total import and export (based on value)


op1=df1.groupby('Country').agg({'Value-INR-2011-12':'sum'})		#grouping sum of values of ech country

op2=df2.groupby('Country').agg({'Value-INR-2011-12':'sum'})


op1=op1.reset_index()
op2=op2.reset_index()

op1=op1.nlargest(5, 'Value-INR-2011-12' )		#extraction top 5 values from the results
op2=op2.nlargest(5, 'Value-INR-2011-12' )

print("\nTop five Country in Import based on value\n")
print(op1)		


print("\nTop five Country in Export based on value\n")
print(op2)




op1.drop(['Value-INR-2011-12'], axis=1,inplace=True)	#dropping the value column
op2.drop(['Value-INR-2011-12'], axis=1,inplace=True)



op1.to_excel(writer,sheet_name='Q1_imports', index=False)		#writing sheet to excel file
op2.to_excel(writer,sheet_name='Q1_exports', index=False)


#top five import and export commodities (based on quantity)

icomm=df1.groupby('Commodity').agg({'Value-INR-2011-12':'sum'})			#grouping sum of values of ech country

ecomm=df2.groupby('Commodity').agg({'Value-INR-2011-12':'sum'})

icomm=icomm.reset_index()					#resettin index of both
ecomm=ecomm.reset_index()


ecomm1=ecomm.nlargest(5, 'Value-INR-2011-12' )			#returning commodities with top 5 values
icomm1=icomm.nlargest(5, 'Value-INR-2011-12' )


print("\nTop five Commodities in Import based on Value\n")
print(icomm)

print("\nTop five Commodities in Export based on Value\n")
print(ecomm)



icomm1.drop(['Value-INR-2011-12'], axis=1,inplace=True)		#dropping the value column
ecomm1.drop(['Value-INR-2011-12'], axis=1,inplace=True)

icomm1.to_excel(writer,sheet_name='Q2_imports', index=False)	#writing sheet to excel file
ecomm1.to_excel(writer,sheet_name='Q2_exports', index=False)


#single table that shows total imports, total exports, export/import ratio, export-import (trade deficit) for each country.


print('\nTable Containing total imports, total exports, export/import ratio, export-import (trade deficit) for each country \n')
##temp1=df1
##temp2=df2
##temp1['Import']=temp1.groupby('Country')['Value-INR-2011-12'].transform(sum)



##temp2['Export']=temp2.groupby('Country')['Value-INR-2011-12'].transform(sum)

temp1=df1.groupby('Country').agg({'Value-INR-2011-12':'sum'})		#grouping sum of values of ech country
temp1=temp1.reset_index()
temp1.columns=['Country','Total imports']

temp2=df2.groupby('Country').agg({'Value-INR-2011-12':'sum'})


temp2=temp2.reset_index()
temp2.columns=['Country','Total exports']						#renaming the columns



#temp3=pd.concat(temp1[['Country', 'Import']],temp2[['Country', 'Emport']])

##temp3=temp1[['Country', 'Import']].set_index('Country').join(temp2[['Country', 'Export']].set_index('Country'))
#temp3=temp1[['Country', 'Import']].join(temp2[['Country', 'Export']])
#temp3=pd.concat([temp1, temp2], ignore_index=True ,axis=1)



temp3=pd.merge(temp1, temp2, how='outer', on=['Country'])			#merging two data frames
#temp3=temp3.drop_duplicates()
temp3['Export/import ratio']=temp3['Total exports']/temp3['Total imports']			#creating new column for ratio
temp3['Export-import (trade deficit)']=temp3['Total exports']-temp3['Total imports']	#creating new column for trade defict
temp3=temp3.replace(np.inf, 'Zero import')			#replacing infinite values with 'Zero import'
temp3=temp3.fillna('NotAvailable')					#replacing Nan with NotAvailabe
#temp3[np.isinf(temp3)] = np.nan
temp3.to_excel(writer,sheet_name='Q3', index=False)			#writing sheet to excel file
#temp4=temp3['Country'].drop_duplicates()
#temp4.to_excel(writer,sheet_name='Q5', index=False)
#temp3=temp3.reset_index()
print(temp3)






#Use the 'query' method to show all countries to whom our export is more than Rs 10,000 Cr
print('Countries whose export is more than Rs 10,000 Cr')
temp2=df2
temp2['Export']=temp2.groupby('Country')['Value-INR-2011-12'].transform(sum)			#grouping sum of values of ech country

op1=temp2.query('Export > 1e+11')			#running query to find export  more than Rs 10,000 Cr
op2=op1[['Country']].drop_duplicates()			#dropping duplicate
op2.to_excel(writer,sheet_name='Q4', index=False)	#writing sheet to excel file
print(op2)


#Save the answer to 4 in a new table  'Country', 'Exports', 'Imports'

print('\nNew table with  Country, Exports, Imports')
op1 = temp3[temp3['Total exports'] > 1e+11]		#running query to find export  more than Rs 10,000 Cr
#op1=temp3.query('Total exports > 1e+11')
#op1=op1[['Country','Export','Import']].drop_duplicates()
op2=op1[['Country','Total imports','Total exports']]		#extracing columns
op2.columns=['Country','Import','Export']		#renaming the columns

print(op2)



#6th Using the table in 5, create a new table with column headings 'Country' 'Transaction''Value'
print('\nNew table with  Country, Transaction,Value')
temp4=pd.melt(op2, id_vars=['Country'], value_vars=['Export','Import'])
temp4.columns=['Country','Transaction','Value (INR)']
temp4['Value (INR)'] = temp4['Value (INR)'].astype(int)		#typecasting to integer
temp4=temp4.nlargest(10, 'Value (INR)' )					#returning county with top 10 trasaction values


op2.columns=['Country','Import (INR)','Export (INR)']		#renaming columns	

op2.to_excel(writer,sheet_name='Q5', index=False)		#writing sheet to excel file
temp4.to_excel(writer,sheet_name='Q6', index=False)
print(temp4)


#7th Make a table of commodities that we both export and import

print('\nTable of commodities that we both export and import')
#ixe=pd.Index([ecomm['Commodity'].drop_duplicates()])
#ixi=pd.Index([icomm['Commodity'].drop_duplicates()])
#common=ixe.intersection(ixi)

#ixe=ecomm['Commodity'].drop_duplicates()
#ixi=icomm['Commodity'].drop_duplicates()
#ixi.columns=['Commodity']
#ixe.columns=['Commodity']
ixe=pd.DataFrame()			#creating new data frame
ixi=pd.DataFrame()

ixe['Commodity']=ecomm['Commodity'].astype(str)				#typecasting the column
ixi['Commodity']=icomm['Commodity'].astype(str)

c=pd.merge(ixe, ixi, how='inner', on=['Commodity'])			#taking the intersection of two table
c.to_excel(writer,sheet_name='Q7', index=False)		#writing sheet to excel file
#ixe.merge(ixi)
print(c)



writer.save()
