def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            monty = line.split(',')
            cast_list.append(monty[0])
            
        
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

print (create_cast_list('flying_circus_cast.txt'))