import os
from os import walk

def findValidFoldersForMatrix(dirPath):
    result = []
    
    for (dirPath, dirNames, filesNames) in walk(dirPath):
        if ("azuredeploy.json" in filesNames and "README.md" in filesNames):
            result.append(dirPath)
        for dirName in dirNames:
            result += findValidFoldersForMatrix(dirName)

    return result

def run():
    results = findValidFoldersForMatrix("D:\\Tests\\action-deploy-azure-button-tests\\test")

    matrixOutput = "::set-output name=matrix::{\"include\":["

    for item in results:
        matrixOutput += "{\"template\":\""+os.path.join(item, "azuredeploy.json")+"\", \"markdown\":\""+os.path.join(item, "README.md")+"\"},"

    matrixOutput = matrixOutput[:-1]
    matrixOutput += "]}"
    print(matrixOutput)


if __name__ == "__main__":
    run()
