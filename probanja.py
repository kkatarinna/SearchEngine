import os
for (root, dirs, file) in os.walk("/Users/katarinakrstin/Documents/Fakultet/II semestar/Algoritmi/Projekat2/python-2.7.7-docs-html/_sources"):
        
        for f in file:
            if 'sorting.txt' in f:
                print(f)
                fajl = open(root + "/"+ f, "r")
                content = fajl.readlines()
                linije = len(content)
                fajl.close()
                fajl = open(root + "/"+ f, "r")

                for i in range(14):
                    if i < linije:
                        line = fajl.readline()
                        print(line)
                
                
                
                
     