# -*- coding: utf-8 -*-
import random

countries_list = [ "Brasil",
"México",
"Argentina",
"Colombia",
"Venezuela",
"Perú",
"Chile",
"Ecuador",
"República Dominicana",
"Guatemala",
"Costa Rica Uruguay",
"Bolivia",
"Panamá",
"El salvador",
"Paraguay",
"Honduras",
"Nicaragua",
"Haití",
"El Congo",
"Somalia"]

regions = ["Norte", "Sur", "Este", "Oeste"]

for x in range(20):
    random_ong = random.randint(0,10)
    random_action = random.randint(0,20)
    random_region = random.choice(regions)
    random_benef = random.randint(1, 1000)
    if random_ong < 10 and random_action < 10:
        print "00" + str(random_ong) + " " + str(x+1) + " " + "00" + str(random_action) + " " + countries_list[x] + " " + \
              random_region + " " + str(random_benef)
    elif random_ong == 10 and random_action < 10:
        print "0" + str(random_ong) + " " + str(x + 1) + " " + "00" + str(random_action) + " " + countries_list[x] + " " + \
              random_region + " " + str(random_benef)
    elif random_ong < 10 and random_action >= 10:
        print "00" + str(random_ong) + " " + str(x + 1) + " " + "0" + str(random_action) + " " + countries_list[
            x] + " " + \
              random_region + " " + str(random_benef)

#Not finished