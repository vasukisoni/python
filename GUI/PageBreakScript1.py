import sys,os         # system library import
 
file = input('enter file here')
file1 = open(file)
text =  file1.read()

#text = open(sys.argv[1],'r')

def more(text, numlines = 5):            
    lines = text.splitlines(5)          # like split('\n') but no '' at end
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break
if __name__ == '__main__':
                                  # when run, not imported
    more(text , 5)       # page contents of file on cmdline
