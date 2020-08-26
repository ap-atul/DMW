import apriori
"""
The min confidence and support should be in decimals
for ex. if you want 22% support i.e. 0.22 
similar for confidence
"""

files = ["groceries.csv", "example.csv", "electronics.csv"]


def runApriori(file):
    minSupport = float(input("Enter the minimum support value :: "))
    minConfidence = float(input("Enter the minimum confidence value :: "))

    data = apriori.dataFromFile(file)
    items, rules = apriori.runApriori(data, minSupport, minConfidence)
    apriori.printResults(items, rules)


def switch(option):
    if option > len(files):
        return

    runApriori(files[option])


while True:
    print("\n\n\n")
    print("*************** Apriori Menu ***************")
    print("1. Groceries data set.")
    print("2. Example data set.")
    print("3. Electronics data set.")
    print("4. Exit")
    print("********************************************")

    opt = int(input("\nEnter your choice :: "))
    if opt == 4:
        print("\nThanks for trying the system !")
        break

    switch(opt - 1)
