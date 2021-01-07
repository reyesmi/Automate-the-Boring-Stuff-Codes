"""
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
colWidths[0] = 7
colWidths[1] = 5
colWidths[2] = 5
Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

Hint: your code will first have to find the longest string in each of the inner lists so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers.
The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the number of inner lists in tableData.
That way, colWidths[0] can store the width of the longest string in tableData[0], colWidths[1] can store the width of the longest string in tableData[1], and so on.
You can then find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method.
"""


def printTable(tableData):
    colWidth = [0] * len(tableData) # Creates a list which can be expanded to indicate the width of the column. i.e [0] * 3 = [0,0,0]
    count = 0 # We'll use the variable count as the index.
    while count < len(tableData): # Finds longest string in each sublist
        for item in tableData[count]: # We'll iterate through each item in the sublists
            if len(item) > colWidth[count]: # We'll measure the length of each item. The longest item will be set to the column width.
                colWidth[count] = len(item)
        count += 1

    for word in range(len(tableData)):
        for item in range(len(tableData)):
            print(tableData[item][word].rjust(colWidth[item]),end = ' ')
        print()
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
