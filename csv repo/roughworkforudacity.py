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
            if n == (len(data1) - 1):
                data.append(output)
                n = 0
                output = {}
        
    print data
                
     


         
                
    
            
    
    
    
datafile = os.path.join(DATADIR, DATAFILE)
parse_file(datafile)



def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    #firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    #tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    #assert d[0] == firstline
    #assert d[9] == tenthline

    
test()
