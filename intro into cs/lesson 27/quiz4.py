# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def space_check(var):
    n = 0
    output = False
    while n < len(var):
        if var[n] == " ":
            output =  True
            break
        n += 1
    return output
    
def program(link):
    location_open = []
    location_close = []
    output = []
    counter = 0
    n = 0
    klink = (link.strip())

    
    for elements in klink:
        if elements == '<':
            location_open.append(counter)
        elif elements == '>':
            location_close.append(counter)
        counter += 1
    if  len(location_close) and len(location_open) != 0:
    
        while n < len(location_open) - 1:
            var = klink[location_close[n]+1:location_open[n + 1]]
            if var.strip() != "":
                if space_check(var.strip()) == True:
                    for xyz in var.split():
                        output.append(xyz)
                else:        
                    output.append(var.strip())
        
            n += 1
    
    return output
    



def remove_tags(link):
    temp = []
    e_temp = []
    find_point = 0
    f_point = 0
    xcd = 0
    vcd = 0
    while xcd < len(link):
        if link[xcd] == "<":
            find_point = xcd
            break
        else:
            find_point = None
            xcd += 1
            
    while vcd > (-1 * len(link)):
        if link[vcd] == ">":
            f_point = vcd
            break
        else:
            f_point = None
            vcd = vcd - 1
    
    if find_point == 0 and f_point == -1:
        return program(link)
        
    elif find_point == None and f_point == None:
        for kop in link.split():
            temp.append(kop.strip())
        return temp
        
    elif find_point != 0 and f_point == -1:
        for itemx in link[0:find_point].split():
            temp.append(itemx.strip())
        return temp + program(link[find_point:])
        
    elif find_point == 0 and f_point != -1:
        print "true"
        for itx in link[f_point + 1:].split():
            temp.append(itx.strip())
        return program(link[0:f_point]) + temp
    else:
        for yyz in link[0:find_point].split():
            temp.append(yyz.strip())
        for wwe in link[f_point + 1:].split():
            e_temp.append(wwe.strip())
        return temp + program(link[find_point:f_point]) +e_temp
        
    
    


print remove_tags('x<>This line starts with a tag<>x')
#>>> ['Title','This','is','a','link','.']

#print remove_tags('''<table cellpadding='3'>
#                     <tr><td>Hello</td><td>World!</td></tr>
#                     </table>''')
#>>> ['Hello','World!']

#print remove_tags("<hello><goodbye>")
#>>> []

#print remove_tags("This is in <i>italics</i>")


#print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']