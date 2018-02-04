#print asterisk triangle with 10 rows

import sys

def main():

    num_rows = int(input("How many rows? "))

    for i in range(num_rows):
        row = ""
        for j in range(i+1): #adding one even though we didn't in class
                             # so that all methods work
            row = row + "*"
        print (row)


        #Method #2---uncomment to test
        #num_asterisks = i
        #while num_asterisks >= 0:
        #    triangle_row = triangle_row + "*"
        #    num_asterisks = num_asterisks-1
        #print triangle_row

        #Method #3 --- uncomment to test
        #triangle_row="*" * (i+1)
        #for num_asterisks in range(i):
        #    sys.stdout.write("*")
        #print
        
    #one of the ways without nested loops
    #row=""
    #for i in range(10):
    #    row = row + "*"
    #    print row

main()
#easy way to test?  replace "*" with i
#what if the use of i in both places is confusing?  How can we change it?
#how do we make it a variable number of rows?
#how do we do it without a nested loop?
#what if we only print the triangle at the end?
#what if we want to print every time? (no strings)  Can we do that?
   
