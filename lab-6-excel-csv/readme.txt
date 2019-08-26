1. Command to execute in syntactical format, also give a working example.

       Example:

              Format:            python3  solution.py  <csv_input_file_name> <Work_No>

              Working Eg:        python3  solution.py  qqq.csv 144

2.Brief description of your code.

Assumption:-
The input must be .csv file.  

Working:-
It checks for index of the header containin 'work no' with help of re module and using that index it compare all the row containig the work number given as input.
It use create_sheet() function to add sheet and sheet.append() function to add value into sheet.

Each sheet will have the name <work no>_<index>
example:-
123_1
123_2

The 'work no' entry in the sheet will be changed as following:-
In sheet 123_1 it will change from 123 to 123_1
In sheet 123_2 it will change from 123 to 123_2
and so on..

The name of output file is changed using re
example:-
Input :- python3  solution.py  qqq.csv 144
Output file:- qqq_144.xlsx



It checks for following error:-
a. If no row contain work number given as input, it will dispay error message and no file will be returned.
b. If no header contain 'work no' given as input, it will dispay error message and no file will be returned.



3. State Assumptions if any.

The input must be .csv file. 
