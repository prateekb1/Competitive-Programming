def matchingStrings(stringList, queries):
    # Write your code here
    result = []
    for i in queries:
        a = stringList.count(i)
        result.append(a)
    return result

print(matchingStrings(['ab','ab','abc'],['ab','abc','bc']))