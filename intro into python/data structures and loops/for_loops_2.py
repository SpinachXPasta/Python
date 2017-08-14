def html_list(strings):
    output = ["<ul>"]
    for string in strings:
        output.append("<li>" + str(string) + "</li>")
        
    output.append("</ul>")
    for out in output:
        print (out)
    
    
html_list(["strings", 2.0, True, "and other types too!"])
    
