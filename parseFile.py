from functions import fileReading
from functions import auxiliar
import sys

def parse(dictPath: str) -> dict:
    # Read file
    fileData = fileReading.readFile(filePath)
    print(f'fileData: {fileData}')
    # Arrange data 
    dataDict: dict = auxiliar.writingDict(fileData)
    return dataDict


if __name__ == '__main__':
    # User Input
    filePath: str = sys.argv[1]
    
    # Function execution
    print(parse(filePath))

