from numpy.random import choice

class NameGenerator:
    def __init__(self):
        # List of imported names
        self.boyNames = []
        self.girlNames = []
        # Markov models
        self.boyModel = {}
        self.girlModel = {}
        # Import name reference files
        self.importNames()
        # Initialize Markov models
        self.generateModel()

    '''
    This method imports the reference texts containing each individual name.
    Names are stored in an array which acts as a reference for letter parsing 
    and for the uniqueness of subsequently created names.
    '''
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

    '''
    The generateModel method serves as a utility function that oversees the creation
    of the markov models regarding boy and girl names. The names are parsed and tallied 
    for letter association before the probability distribution of each individual 
    sequence is calculated. The commented code can be used to display the models for
    the purpose of debugging.
    '''
    def generateModel(self):
        self.boyModel = self.parseNames(self.boyNames)
        self.boyModel = self.calculateDistribution(self.boyModel)
        self.girlModel = self.parseNames(self.girlNames)
        self.girlModel = self.calculateDistribution(self.girlModel)

        # for item in self.boyModel:
        #     print("{} {}".format(item, self.boyModel[item]))
        #
        # for item in self.girlModel:
        #     print("{} {}".format(item, self.girlModel[item]))

    '''
    This function tracks the occurrence of letter sequences on each name
    in the specified inputList. The letter associations are considered 
    in lengths of 1 and 2 in formats such as: 'rs' -> 't', 'r' -> 'st', etc.
    The __ is used to identify starting sequences, whereas the '\n' character
    identifies ending sequences
    '''
    def parseNames(self, inputList):
        states = {}
        j = 2
        for item in inputList:
            s = "__" + item
            # Single to single letter association: 'rs' followed by 't'
            for i in range(0, len(item)):
                prefix = s[i:i + j]
                suffix = s[i + j]
                states = self.addState(states, prefix, suffix)

            # Single to double letter association: 'r' followed by 'st'
            for i in range(0, len(item) - 1):
                prefix = s[i]
                suffix = s[i + 1: i + 1 + j]
                states = self.addState(states, prefix, suffix)

            # Single to single letter association: 'r' followed by 's'
            for i in range(0, len(item)):
                prefix = s[i]
                suffix = s[i + 1]
                states = self.addState(states, prefix, suffix)

            # Append new line character for finishing sequence
            for i in range(1, 3):
                prefix = s[len(item): len(item) + i]
                suffix = "\n"
                states = self.addState(states, prefix, suffix)
        return states

    '''
    This is a utility function that adds a specific state to the the model
    that is passed in. Prefix represents the current state, whereas suffix 
    represents subsequent states. The count of each suffix maintained and 
    utilized in the probability calculations.
    '''
    def addState(self, states, prefix, suffix):
        if prefix in states:
            if suffix in states[prefix]:
                states[prefix][suffix] += 1
            else:
                states[prefix][suffix] = 1
        else:
            states[prefix] = {}
            states[prefix][suffix] = 1
        return states
    '''
    Here we complete the creation of our markov model by converting the counts
    previously recorded for sequence into probabilities. With this implementation,
    our model is currently a 1st order model.
    '''
    def calculateDistribution(self, inputModel):
        for element in inputModel:
            arr = inputModel[element]
            count = sum(arr.values())
            for item in arr:
                arr[item] = float(arr[item]) / float(count)
            inputModel[element] = arr
        return inputModel

    '''
    This is the method called on our NameGenerator object to create out list of names.
    The gender argument is passed into the newName() method, which creates the individual
    word using our models. The returned word is checked against the min and max length
    requirements, as well as for uniqueness. 
    '''
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

    '''
    This is the method that performs the actual name generation. The selected prefix is 
    fed into the numpy.random.choice() method, which selects the appropriate suffix based
    on its probability distribution. The returned suffix is appended to the name under 
    construction. The '__' and '\n' provide the boundary conditions for name building.
    '''
    def newName(self, gender):
        # Select the gender model
        model = None
        nameList = None
        if gender is 1:
            model = self.boyModel
            nameList = self.boyNames
        elif gender is 0:
            model = self.girlModel
            nameList = self.girlNames

        # Construct the word
        prefix = "__"
        name = ""
        while True:
            suffix = choice(model[prefix].keys(), 1, p=model[prefix].values())
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
