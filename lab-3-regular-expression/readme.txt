The script is reading the input file "input.txt" and writing in the file called "output.txt".
It performs the following operations:-
1.
Detect any mobile number starting from +91 and should contain 10 digits.
It will mask +91 and first four digits with "*".
eg.Input= +919044334699
Output=******334699

2.
Detect any email id , the email could contain letters , digits , and following special characters "."(dot)  "_"(underscore) "-"(minus). It should contain atleadt one dot after @.
It will mask the user id before @.
Input= peter2@gmail.com
Output=******@gmail.com

3.
It will detect a fullstop and a space and change the first letter on next word to capital.
There should be a space after fullstop.
Input= window. linux
Output= window. Linux

4.
It will detect any website starting from www and append http:// before it.
Input= www.google.com
Output= http://www.google.com

5.
It will detect any occurence of word "color"/"Color" and will replace it with "colour"/"Colour".
Input= color
Output= colour
