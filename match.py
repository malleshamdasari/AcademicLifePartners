import os
import dblp
import numpy as np

totalpapers = []
people = []

def getActiveResearchers():
    files = os.listdir('data/')
    people = []
    for f in files:
        lines = open('data/'+f, 'r')
        for line in lines:
            people.append(line.strip().split(',')[0])
    people = list(set(people))
    return people

def getCorrectAuthorNames(wrongNames):
    global people
    rightNames = []
    for name in wrongNames:
        if '00' in name:
            name = name.split(' ')[:-1]
            name = ' '.join(name)
        rightNames.append(name)
    for i in rightNames:
        if i not in people:
            people.append(i)
    return rightNames

def getAuthorsFromVenue(conf, year, conf_short):
    global totalpapers
    papersandauthors = dblp.getvenueauthorsbypaper("/conf/" + conf.lower() + "/" + str(year), conf_short)
    for authorsperpaper in papersandauthors:
        totalpapers.append(getCorrectAuthorNames(authorsperpaper[1]))

for i in range(2005, 2017):
    getAuthorsFromVenue("sigcomm", str(i), "SIGCOMM")
    getAuthorsFromVenue("nsdi", str(i), "NSDI")
    getAuthorsFromVenue("mobicom", str(i), "MobiCom")
    getAuthorsFromVenue("mobisys", str(i), "MobiSys")
    getAuthorsFromVenue("sosp", str(i), "SOSP")
    getAuthorsFromVenue("imc", str(i), "IMC")
    getAuthorsFromVenue("hotnets", str(i), "HotNets")
    getAuthorsFromVenue("infocom", str(i), "INFOCOM")
    getAuthorsFromVenue("conext", str(i), "CoNEXT")
    getAuthorsFromVenue("sigmetrics", str(i), "SIGMETRICS")

#people = getActiveResearchers()
print len(people)

def getAcademicLifePartners(people, totalpapers):
    partnership = {}
    for i in people:
        partnership[i] = {}
    for i in people:
        for j in people:
            if i != j:
                partnership[i][j] = 0
    for i in people:
        for j in people:
            for k in totalpapers:
                if i in k and j in k and i != j:
                    partnership[i][j] += 1
                    if partnership[i][j] > 4:
                        print i, j, partnership[i][j]
    return partnership

x = getAcademicLifePartners(people, totalpapers)
