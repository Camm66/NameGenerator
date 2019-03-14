import random
from numpy.random import choice

class NameGenerator:
    def __init__(self):
        # List of imported names
        self.boyNames = []
        self.girlNames = []
        # Markov models
        self.boyModel = {}
        self.girlModel = {}
        # Initialize Markov Process
        self.generateMap()

    def generateMap(self):
        self.importNames()
        self.generateModel()

    def importNames(self):
        try:
            f = open("namesBoys.txt", "r")
            for line in f:
                self.boyNames.append((line.rstrip()).lower())
        finally:
            f.close()
        try:
            f = open("namesGirls.txt", "r")
            for line in f:
                self.girlNames.append((line.rstrip()).lower())
        finally:
            f.close()

    def generateModel(self):

        self.boyModel = self.parseNames(self.boyNames)
        self.boyModel = self.calculateDistribution(self.boyModel)

        for item in self.boyModel:
            print("{} {}".format(item, self.boyModel[item]))

        self.girlModel = self.parseNames(self.girlNames)
        self.girlModel = self.calculateDistribution(self.girlModel)

    def parseNames(self, inputList):
        chain = 2
        states = {}

        for item in inputList:
            s = "_" * chain + item
            for i in range(0, len(item)):
                prefix = s[i:i + chain]
                suffix = s[i + chain]
                if prefix in states:
                    if suffix in states[prefix]:
                        states[prefix][suffix] += 1
                    else:
                        states[prefix][suffix] = 1
                else:
                    states[prefix] = {}
                    states[prefix][suffix] = 1
            prefix = s[len(item): len(item) + chain]
            suffix = "\n"
            if prefix in states:
                if suffix in states[prefix]:
                    states[prefix][suffix] += 1
                else:
                    states[prefix][suffix] = 1
            else:
                states[prefix] = {}
                states[prefix][suffix] = 1
        return states

    def calculateDistribution(self, inputModel):
        count = 0
        for element in inputModel:
            arr = inputModel[element]
            count = sum(arr.values())
            for item in arr:
                arr[item] = float(arr[item]) / float(count)
            inputModel[element] = arr
        return inputModel

    def generateNames(self, gender, number, minLen, maxLen):
        names = []
        i = 0
        while i < number:
            result = self.newName(gender)
            if minLen <= len(result) <= maxLen and result is not ' ' and result not in names:
                names.append(result)
                i += 1

        for name in names:
            print(name)

    def newName(self, gender):
        prefix = "__"
        suffix = ""
        name = ""

        model = None
        nameList = None
        if gender is 1:
            model = self.boyModel
            nameList = self.boyNames
        elif gender is 0:
            model = self.girlModel
            nameList = self.girlNames

        while True:
            suffix = choice(model[prefix].keys(), 1, model[prefix].values())
        #    print(model[prefix].keys())
        #    print(model[prefix].values())
        #    print(suffix)
            if suffix[0] == "\n":
                break
            else:
                name = name + suffix[0]
                prefix = prefix[1:] + suffix[0]

        if name in nameList:
            name = ' '
        else:
            name = name.capitalize()

        return name
