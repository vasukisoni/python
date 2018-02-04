import sys

filename = sys.argv[1]    
myfile = open(filename,'r')
for line in myfile.readlines():
        print (line)

myfile.close


#-----------------------------------------------------------------------------
# FOR THE COMMAND LINE INPUT OF THE FILE 
# 1) GOTO CMD , THEN GOTO c:\PYTHON33
# 2) THEM TYPE >>> python E:\Python\GUI\PageBreakScript3.py E:\Test.txt 
#  finally ur script gets run.
#-----------------------------------------------------------------------------
