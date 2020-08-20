import apriori

file = "dataset.csv"
minSupport = float(input("Enter the minimum support value :: "))
minConfidence = float(input("Enter the minimum confidence value :: "))

data = apriori.dataFromFile(file)
items, rules = apriori.runApriori(data, minSupport, minConfidence)
apriori.printResults(items, rules)
