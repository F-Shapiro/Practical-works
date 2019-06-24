from os import remove
from os.path import dirname
from multiprocessing import Pool
import time

def createTagnameFile(htmlDoc, firstIndex, secondIndex, tagName):
    containTag = htmlDoc[firstIndex:secondIndex]
    htmlDoc = htmlDoc.replace("<" + tagName, "", 1)
    htmlDoc = htmlDoc.replace("</" + tagName, "", 1)
    with open(dirname(__file__) + "/temporary.txt", "w") as temporaryFile:
        temporaryFile.write(htmlDoc)
    containTag = containTag.replace(">", ">\n")
    containTag = containTag.replace("             </", "\n                </")
    with open(dirname(__file__) + "/" + tagName + ".txt", "a") as tagFile:
        tagFile.write(containTag)

def checkExistH(htmlDoc, tag):
    for num in range(1, 7):
        indexTag = htmlDoc.find("<" + tag + str(num) + ">")
        if indexTag != -1:
            tag = tag + str(num)
            indexTag += (2 + len(tag))
            indexTag2 = htmlDoc.find("</" + tag + ">")
            createTagnameFile(htmlDoc, indexTag, indexTag2, tag)
            return True
    return False

def checkPositionTag(htmlDoc, indexTag, arr, tagName):
    for tag2 in arr:
        indexTag2 = htmlDoc.find("<" + tag2 + ">")
        if indexTag2 != -1:
            if indexTag > indexTag2:
                return False
    return True

def parser(processes):
    tagBox = ["head", "title", "body", "h", "div", "seaction", "ul", "ol", "li", "p", "table"]

    with open(dirname(__file__) + "/temporary.txt", "r") as temporaryFile:
        webPage = temporaryFile.read()

    for tag in tagBox:
        if tag == "h":
            if checkExistH(webPage, tag):
                break
            else:
                continue
        else:
            indexTag = webPage.find("<" + tag + ">")

        if indexTag != -1:
            if checkPositionTag(webPage, indexTag, tagBox, tag):
                print(tag, indexTag)
                indexTag += (2 + len(tag))
                indexTag2 = webPage.find("</" + tag + ">")
                createTagnameFile(webPage, indexTag, indexTag2, tag)
                break
            continue

def main():
    with open(dirname(__file__) + "/file.html", "r") as target:
        with open(dirname(__file__) + "/temporary.txt", "a") as temporaryFile:
            webPage = target.read()
            temporaryFile.write(webPage.replace("\n", ""))

    lenghtCycle = webPage.count("</") - 1
    processes = []
    process = []
    for proc in range(lenghtCycle):
        processes.append(process)

    pool = Pool(processes = 1)
    pool.map(parser, processes)

    remove(dirname(__file__) + "/temporary.txt")

if __name__ == '__main__':
    main()