import re

listofspecies = open("Bacteria_Species_extremo37.txt").readlines()
do_print = False
with open("Bac16s.faa") as f:
    for line in f:
        if do_print:
            print (do_print + line.strip())
            do_print = False
            continue
        for x in listofspecies:
            names = x.split("_")
            if re.findall(names[0].strip(), line):
                if re.findall(names[1].strip(), line):
                    do_print = ">" + x
                    break
