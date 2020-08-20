from itertools import chain, combinations
from collections import defaultdict


def subsets(arr):
    """
    create subsets from the array
    :param arr: input array
    :return:non empty subset
    """
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
    """
    calculate the support for item set and return a set of elements that satisfies
    the minimum support
    :param itemSet: input set of elements
    :param transactionList: tuple of rules confidence
    :param minSupport: minimum support to check
    :param freqSet: frequency set containing no of freq of each element
    :return: subset of satisfied elements
    """
    returnSet = set()
    countSet = defaultdict(int)

    for item in itemSet:
        for transaction in transactionList:
            if item.issubset(transaction):
                freqSet[item] += 1
                countSet[item] += 1

    for item, count in countSet.items():
        support = float(count) / len(transactionList)

        if support >= minSupport:
            returnSet.add(item)

    return returnSet


def joinSet(itemSet, length):
    """
    join a set with all elements
    :param itemSet: input set
    :param length: length of the set
    :return: joined set of all ele
    """
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data):
    """
    read the data and convert to tuple of tuple
    return a set
    :param data: input data from file
    :return: set of all ele (item set and count)
    """
    transactionList = list()
    itemSet = set()

    for record in data:
        transaction = frozenset(record)
        transactionList.append(transaction)

        for item in transaction:
            itemSet.add(frozenset([item]))

    return itemSet, transactionList


def runApriori(data, minSupport, minConfidence):
    """
    run the apriori on the data from the file
    :param data: input data
    :param minSupport: minimum support
    :param minConfidence: minimum confidence
    :return: rules ((pre_tuple, post_tuple), confidence),
            items (tuple, support)
    """
    # initial sets
    itemSet, transactionList = getItemSetTransactionList(data)

    # stores (key = n_itemSets, value = support) satisfying (minSupport)
    freqSet = defaultdict(int)
    largeSet = dict()

    # dictionary to store association rules
    assocRules = dict()

    oneCSet = returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet)

    currentLSet = oneCSet
    k = 2

    while currentLSet != set([]):
        largeSet[k - 1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet, transactionList, minSupport, freqSet)
        currentLSet = currentCSet
        k += 1

    def getSupport(item):
        """
        return support of an item
        :param item: input
        :return: support of the item
        """
        return float(freqSet[item] / len(transactionList))

    toRetItems = []
    toRetRules = []

    for key, values in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item)) for item in values])

    for key, val in list(largeSet.items())[1:]:
        for item in val:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item) / getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)), confidence))

    return toRetItems, toRetRules


def printResults(items, rules):
    """
    print the associations selected and the items
    :param items: all the items
    :param rules: all the rules
    :return: None
    """

    print("\n************  Items  *************\n")
    for item, support in sorted(items, key=lambda x: x[1], reverse=True):
        print("item : { %s } , %.3f" % (str(item), support))

    print("\n************  Rules  *************\n")
    for rule, confidence in sorted(rules, key=lambda c: c[1], reverse=True):
        pre, post = rule
        print("Rule { %s } ---> { %s } , %.3f" % (str(pre), str(post), confidence))


def dataFromFile(fileName):
    """
    returns a generated set for the records
    :param fileName: input file name
    :return: set
    """

    with open(fileName, 'rU') as file:
        for line in file:
            line = line.strip().rstrip(',')
            record = frozenset(line.split(','))
            yield record
