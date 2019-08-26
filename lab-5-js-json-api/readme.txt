1.
Command to execute in syntactical format:-

Format:

python3 solution.py <Village_Name>

Working example:

python3 solution.py Asoli
python3 solution.py Borkanhar
python3 solution.py Borkanhar

2.
Brief description of code

We have to enter the name of the villege. The name of the village is case sensitive (i.e. it should start witha capital letter).
It will promt to select specific village from a list all the village with same name.

eg:-

0 .  Amravati-->Yevatmal-->Kelapur-->Asoli
1 .  Amravati-->Yevatmal-->Pusad-->Asoli
2 .  Kokan-->Sindhudurg-->Vengurla-->Asoli
3 .  Nagpur-->Nagpur-->Kamthi-->Asoli
4 .  Nagpur-->Nagpur-->Ramtek-->Asoli
5 .  Nagpur-->Nagpur-->Hingana-->Asoli
6 .  Nagpur-->Gondia-->Amgaon-->Asoli
7 .  Nagpur-->Gondia-->Arjuni Morgaon-->Asoli
8 .  Nashik-->Nashik-->Kalwan-->Asoli



Enter the index to select specific index. Example enter 6 to select Nagpur-->Gondia-->Amgaon-->Asoli.
It will then download its map on current directory and open it using webbrowser module.

If there is no such file. It will show messege.

3.
Assumptions:

Village name are case sensitive.
