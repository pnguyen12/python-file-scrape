def readFile():
    # create lists needed for output
    sources = []
    destinations = []
    # open file in read
    file = open('scrape.txt', 'r')

    # loop over file
    for line in file:
        # split the line using tab as a delimiter
        currentLine = line.split('\t')
        # join the array back to a string
        newLine = "".join(currentLine)

        # check the current line
        if checkLine(newLine):
            # split the newline so we can append the 2nd and 3rd elements
            currentLineIp = newLine.split()
            # append values
            sources.append(currentLineIp[2])
            destinations.append(currentLineIp[3])
    
    writeFile(sources, destinations)

def checkLine(line):
    # the IP addresses that are needed all have these strings in common
    # if either are in the current line return true
    if "ACK" in line or "SSDP" in line:
        return True

def writeFile(sources, destinations):
    # create file name
    filename = 'output.txt'
    # open the file in write
    file = open(filename, 'w')
    # create our columns with three tabs
    file.write('Source \t\t\tDestination')
    # traverse through the sources this will be the same length as the destinations list
    for index in range(len(sources)):
        # write a new line
        file.write('\n')
        # write the sources and destination with the current index
        file.write(sources[index] + '\t' + destinations[index])
    # close the file
    file.close()

def main():
    readFile()

main()

