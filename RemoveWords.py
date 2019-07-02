import re

#removeWords = ['eagre', 'avera', 'vera', 'gare', 'eave', 'aver', 'areg']

sourcefile = "Words.txt" 
filename2 = "Words_reduced.txt"

def fixup(removeWords): 
    global sourcefile

    if len(removeWords[0]) == 0:
        return

    fin = open( sourcefile, "r+") 
    fout = open( sourcefile , "r+") 
    for line in fin:
        writeLine = True

        for word in removeWords:
            if re.match("^" + word + "$", line):
                writeLine = False

        if writeLine:    
            fout.write(line)
    
    fin.close()
    fout.close() 

fixup([''])