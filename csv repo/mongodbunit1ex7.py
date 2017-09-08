# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    data1 = []
    data2 = []
    data3 = []
    output = {}
    with open(datafile, "r") as f:
        counter = 1
        for line in f:
            if counter <= 1:
                for one in line.split(','):
                    data1.append(one.strip())
                counter += 1
            else:
                data2.append(line.strip())
        data2 = data2[0:10]        
        
        for lines in  data2:
            for x in lines.split(','):
                data3.append(x)
                
         
        n = 0
        for every in data3:
            output[data1[n]] = every.strip()
            n += 1 
            if n == (len(data1)):
                data.append(output)
                n = 0
                output = {}
        
    return data
                
     


         
                
    
            
    
    
    
datafile = os.path.join(DATADIR, DATAFILE)
print parse_file(datafile)



def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    #firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    #tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    #assert d[0] == firstline
    #assert d[9] == tenthline

    
test()
test()
