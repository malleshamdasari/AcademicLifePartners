import os
import dblp
import numpy as np

totalpapers = []

def getActiveResearchers():
    files = os.listdir('data/')
    people = []
    for f in files:
        lines = open('data/'+f, 'r')
        for line in lines:
            people.append(line.strip().split(',')[0])
    people = list(set(people))
    return people

def getAuthorsFromVenue(conf, year, conf_short):
    global totalpapers
    papersandauthors = dblp.getvenueauthorsbypaper("/conf/" + conf.lower() + "/" + str(year), conf_short)
    for authorsperpaper in papersandauthors:
        totalpapers.append(authorsperpaper[1])
getAuthorsFromVenue("nsdi", "2017", "NSDI")
getAuthorsFromVenue("nsdi", "2016", "NSDI")
getAuthorsFromVenue("nsdi", "2015", "NSDI")
getAuthorsFromVenue("sigcomm", "2017", "SIGCOMM")
getAuthorsFromVenue("sigcomm", "2016", "SIGCOMM")
getAuthorsFromVenue("sigcomm", "2015", "SIGCOMM")
getAuthorsFromVenue("sigcomm", "2014", "SIGCOMM")
getAuthorsFromVenue("mobicom", "2017", "MobiCom")
getAuthorsFromVenue("mobicom", "2016", "MobiCom")
getAuthorsFromVenue("mobicom", "2015", "MobiCom")
getAuthorsFromVenue("mobicom", "2014", "MobiCom")

people = getActiveResearchers()

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
                    print i, j, partnership[i][j]
    return partnership

x = getAcademicLifePartners(people, totalpapers)
#print x
