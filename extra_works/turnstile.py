import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    bigdata = []
    data = []
    linex = ""
    count = 3
    first = ""
    second = ""
    third = ""
    d = 0
    while d < 2:
        with open(filenames[d],"r") as copy:
            infile = csv.reader(copy, delimiter = ',')
            for every in infile:
                for e in every:
                    if e[0] == 'A' and e[1] == '0':
                        data = []
                        count = 0
                        first = e
                    elif e[0] == 'R' and e[1] == '0':
                        second = e 
                    elif len(e) > 3 and e[2] == '-' and e[3] == '0' and e[4] == '0':
                        third = e
                    data.append(e.strip())
                #if count < 7:
                    #linex += ","
                    count += 1
                    if count == 8:
                    #data.append(linex)
                        bigdata.append(data)
                    #linex = first + ","
                        data = []
                        data.append(first)
                        data.append(second)
                        data.append(third)
                        count = 3
            
            with open(''.join(['updated_',filenames[d]]),"w") as paste:
                outfile = csv.writer(paste)
                for big in bigdata:
                    outfile.writerow(big)
                bigdata = []
                    
            d += 1
            
    #print bigdata       
            copy.close()
            paste.close()

                   
                    
  


    
