tableData = [['apples','oranges','cherries','bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs','cats','moose','goose']]

def colWidthFinder(list_of_values):
    colWidth = 0
    for i in range(len(list_of_values)):
        if len(list_of_values[i]) > colWidth:
            colWidth = len(list_of_values[i])
    return colWidth
        

def printTable(table):
    columnWidths = {}
    for i in range(len(table)):
        columnWidths.setdefault(i,colWidthFinder(table[i]))
        
    #tableprinter
    tableLine = []
    for i in range(len(table[0])):#vertical count
        for n in range(len(table)):#horizontal count
            tableLine.append(table[n][i].rjust(columnWidths[n]))
            if len(tableLine) == len(table):
                print(' '.join(tableLine))
                tableLine = []
    #print(columnWidths)
       
printTable(tableData) 
