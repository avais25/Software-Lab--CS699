import pandas as pd
import numpy as np
import sys


def topFiveCountries(dataFrameImport\
		,dataFrameExport,outputFileWriter):
	topFiveImportCountries=dataFrameImport\
	.groupby('Country')\
	.agg({'Value-INR-2011-12':'sum'})

	topFiveExportCountries=dataFrameExport\
	.groupby('Country')\
	.agg({'Value-INR-2011-12':'sum'})


	topFiveImportCountries=topFiveImportCountries.reset_index()
	topFiveExportCountries=topFiveExportCountries.reset_index()

	topFiveImportCountries=topFiveImportCountries\
	.nlargest(5, 'Value-INR-2011-12' )

	topFiveExportCountries=topFiveExportCountries\
	.nlargest(5, 'Value-INR-2011-12' )

	print("\nTop five Country in Import based on value\n")
	print(topFiveImportCountries)		


	print("\nTop five Country in Export based on value\n")
	print(topFiveExportCountries)




	topFiveImportCountries.drop(['Value-INR-2011-12'],\
	 axis=1,inplace=True)
	topFiveExportCountries.drop(['Value-INR-2011-12'],\
	 axis=1,inplace=True)



	topFiveImportCountries.to_excel(outputFileWriter,\
	sheet_name='Q1_imports', index=False)
	topFiveExportCountries.to_excel(outputFileWriter,\
	sheet_name='Q1_exports', index=False)
	return


def topFiveCommodities(dataFrameImport\
		,dataFrameExport,outputFileWriter):
	
	groupedByImportCommodity=dataFrameImport\
	.groupby('Commodity')\
	.agg({'Value-INR-2011-12':'sum'})

	groupedByExportCommodity=dataFrameExport\
	.groupby('Commodity')\
	.agg({'Value-INR-2011-12':'sum'})

	groupedByImportCommodity=groupedByImportCommodity.reset_index()
	groupedByExportCommodity=groupedByExportCommodity.reset_index()


	topFiveExportCommodities=groupedByExportCommodity\
	.nlargest(5, 'Value-INR-2011-12' )
	topFiveImportCommodities=groupedByImportCommodity\
	.nlargest(5, 'Value-INR-2011-12' )



	topFiveImportCommodities.drop(['Value-INR-2011-12'],\
	 axis=1,inplace=True)

	topFiveExportCommodities.drop(['Value-INR-2011-12'],\
	 axis=1,inplace=True)

	topFiveImportCommodities.to_excel(outputFileWriter,\
		sheet_name='Q2_imports', index=False)
	topFiveExportCommodities.to_excel(outputFileWriter,\
		sheet_name='Q2_exports', index=False)
	return



def singleTableConcatination(dataFrameImport\
		,dataFrameExport,outputFileWriter):

	ImportCountryValue=dataFrameImport.groupby('Country')\
	.agg({'Value-INR-2011-12':'sum'})
	ImportCountryValue=ImportCountryValue.reset_index()
	ImportCountryValue.columns=['Country','Total imports']

	ExportCountryValue=dataFrameExport.groupby('Country')\
	.agg({'Value-INR-2011-12':'sum'})
	ExportCountryValue=ExportCountryValue.reset_index()
	ExportCountryValue.columns=['Country','Total exports']

	mergedOutput=pd.merge(ImportCountryValue, ExportCountryValue,\
	 how='outer', on=['Country'])	
	mergedOutput['Export/import ratio']=\
	mergedOutput['Total exports']/mergedOutput['Total imports']

	mergedOutput['Export-import (trade deficit)']=\
	mergedOutput['Total exports']-mergedOutput['Total imports']
	mergedOutput=mergedOutput.replace(np.inf, 'Zero import')
	mergedOutput=mergedOutput.fillna('NotAvailable')
	mergedOutput.to_excel(outputFileWriter,sheet_name='Q3', index=False)
	print(mergedOutput)
	return mergedOutput




def countriesAboveTheCondition(dataFrameExport\
		,dataFrameImport,outputFileWriter):
	print('Countries whose export is more than Rs 10,000 Cr')
	groupedTemporay=dataFrameExport
	groupedTemporay['Export']=groupedTemporay\
	.groupby('Country')['Value-INR-2011-12'].transform(sum)

	satisfyingCondition=groupedTemporay.query('Export > 1e+11')
	satisfyingCondition=satisfyingCondition[['Country']].drop_duplicates()
	satisfyingCondition.to_excel(outputFileWriter,sheet_name='Q4', index=False)
	print(satisfyingCondition)
	return

def renamingColumns(mergedOutput\
		,outputFileWriter):
	print('\nNew table with  Country, Exports, Imports')
	temporyRename = mergedOutput[mergedOutput['Total exports'] > 1e+11]	
	renamedWithConditions=temporyRename[['Country','Total imports'\
	,'Total exports']]
	renamedWithConditions.columns=['Country','Import','Export']

	print(renamedWithConditions)
	return renamedWithConditions



def topTransaction(renamedWithConditions\
		,outputFileWriter):
	print('\nNew table with  Country, Transaction,Value')
	meltedOutput=pd.melt(renamedWithConditions, id_vars=['Country']\
		, value_vars=['Export','Import'])
	meltedOutput.columns=['Country','Transaction','Value (INR)']
	meltedOutput['Value (INR)'] = meltedOutput['Value (INR)'].astype(int)	
	meltedOutput=meltedOutput.nlargest(10, 'Value (INR)' )


	renamedWithConditions.columns=['Country','Import (INR)'\
	,'Export (INR)']		

	renamedWithConditions.to_excel(outputFileWriter\
	,sheet_name='Q5', index=False)		
	meltedOutput.to_excel(outputFileWriter,sheet_name='Q6'\
		, index=False)
	print(meltedOutput)
	return



def importAndExportCommodities(dataFrameImport\
		,dataFrameExport,outputFileWriter):
	
	print('\nTable of commodities that we both export and import')

	groupedByImportCommodity=dataFrameImport\
	.groupby('Commodity')\
	.agg({'Value-INR-2011-12':'sum'})

	groupedByExportCommodity=dataFrameExport\
	.groupby('Commodity')\
	.agg({'Value-INR-2011-12':'sum'})

	groupedByImportCommodity=groupedByImportCommodity.reset_index()
	groupedByExportCommodity=groupedByExportCommodity.reset_index()

	dfExportCommodities=pd.DataFrame()
	dfImportCommodities=pd.DataFrame()

	dfExportCommodities['Commodity']=groupedByExportCommodity['Commodity']\
	.astype(str)
	dfImportCommodities['Commodity']=groupedByImportCommodity['Commodity']\
	.astype(str)

	mergedDataframe=pd.merge(dfExportCommodities, dfImportCommodities\
	, how='inner', on=['Commodity'])
	mergedDataframe.to_excel(outputFileWriter\
	,sheet_name='Q7', index=False)
	print(mergedDataframe)
	return





def main(argv):

	dataFrameImport = pd.read_excel('India_Imports_2011-12_And_2012-13.xls')

	dataFrameExport = pd.read_excel('India_Exports_2011-12_And_2012-13.xls')

	outputFileWriter = pd.ExcelWriter('173050043_solution.xls',engine = 'xlwt')


	topFiveCountries(dataFrameImport\
		,dataFrameExport,outputFileWriter)

	topFiveCommodities(dataFrameImport\
		,dataFrameExport,outputFileWriter)

	mergedOutput=singleTableConcatination(dataFrameImport\
		,dataFrameExport,outputFileWriter)

	countriesAboveTheCondition(dataFrameExport\
		,dataFrameImport,outputFileWriter)

	renamedWithConditions=renamingColumns(mergedOutput\
		,outputFileWriter)

	topTransaction(renamedWithConditions\
		,outputFileWriter)

	importAndExportCommodities(dataFrameImport\
		,dataFrameExport,outputFileWriter)

	outputFileWriter.save()
	return



if __name__ == "__main__":
     main(sys.argv)