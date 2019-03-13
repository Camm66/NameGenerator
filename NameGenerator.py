

class NameGenerator:
    def __init__(self):
        # List of imported names
        self.boyNames = []
        self.girlNames = []
        # Dictionary key == letter combination, value == letter count
        self.boyCount = {}
        self.girlCount = {}
        # Initialize Markov Process
        self.generateMap()

    def generateMap(self):
        self.importNames()
        self.generateCount()

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

    def generateCount(self):
        states = dict()
        for item in self.boyNames:
            for i in range(len(item) + 1):
                for j in range(i):
                    if item[j:i] in states:
                        states[item[j:i]] += 1
                    else:
                        states[item[j:i]] = 1
        self.boyCount = states

        states = dict()
        for item in self.girlNames:
            for i in range(len(item) + 1):
                for j in range(i):
                    if item[j:i] in states:
                        states[item[j:i]] += 1
                    else:
                        states[item[j:i]] = 1
        self.girlCount = states

        print(self.boyCount)
        print(self.girlCount)

    def markovProcess(self, minLen, maxLen, gender):
        pass


'''
1) import individual names
2) Get the count of each individual letter & letter combo


'''