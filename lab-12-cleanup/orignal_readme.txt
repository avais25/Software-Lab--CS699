Changes Done:-
1. I have changed all the variable name to meannigful name.
2. I have made functions for each type of objectives .
3. I have also named function such that it defines its objective.
4. I have made the code self-explanatory removed all the comments.
5. I have made sure that each line does not contain more than 75 charactes so we dont have to scroll to see 
   the whole line. I have done this using '\' escape for new line.
6. I have created a main function and called all the function there.
7. I have not change variable name of numpy and pandas i.e. np and pd respectively as they are self-explanatory.
8. I have removed unnecessary code and reused output of function as input of another.
9. I have made Global Variables  which contain name of the input and output file names for ease of editing.
10.I have made the code more readable and easy to understand by doing proper spacing and formatting.

How to run:-
python3 cleaned_solution.py
python3 orignal_solution.py

Input files needed:-
1.India_Exports_2011-12_And_2012-13.xls
2.India_Imports_2011-12_And_2012-13.xls

Output file:-
173050043_solution.xls


EXTRA INFORMATION:-

Additioal modules needed apart from numpy and panda:-
1.xlwt:-
command to insatll:
sudo pip3 install xlwt
2.xlrd:-
command to insatll:
sudo pip3 install xlrd


Description of the problem:-
The program takes Import and Export xls file as input and give output acoording to question in a output file.
In Q1 & Q2 it calculate top 5 country and commodity resoectively based on Value of 2011-2012
In Q3 I have used outer join to merge both table. If value of import is 0 for some country in outputs "Zero Import" in export/import cell. If some value of import or export is not available it outputs "NotAvailable" in that cell and its respective ratiio and defict cell.
In Q4 the 'query' method is used show all countries to whom our export is more than Rs 10,000 Cr.
In Q5 the output of Q4 is stored along with import and export
Format- "Country ,Import (INR),Export (INR)"
In Q6 melt function (id_vars=['Country'], value_vars=['Export','Import']) is used on output of Q5 
"Country,Transaction,Value (INR)"
In Q7 Inntersection of commodities of both Import and Export is taken.

Assumptions:-
All the header and column name are taken accordinng to sample_output.xls file provided.
In Q3 outer join is done and If value of import is 0 for some country in outputs "Zero Import" in export/import cell. If some value of import or export is not available it outputs "NotAvailable" in that cell and its respective ratiio and defict cell.
Q7 contains commodities to both year.
I have not removed "unspecified" as a country name so  it is present as output in some sheet.







