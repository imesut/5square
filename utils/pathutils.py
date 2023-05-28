pathSplitChar = ">>"

# Path Utils
def combinePaths(pathArray : list) -> str:
    return pathSplitChar.join(pathArray)

def splitPathStr(pathString : str) -> list:
    return pathString.split(pathSplitChar)

def addToPath(str1 : str, str2 : str) -> str:
    return str1 + pathSplitChar + str2

def prvPath(crntPath : str) -> str:
    return combinePaths(splitPathStr(crntPath)[:-1])

def lastPathParam(crntPath : str) -> str:
    return splitPathStr(crntPath)[-1]