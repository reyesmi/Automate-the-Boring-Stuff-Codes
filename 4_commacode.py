# This program will ask the user to input a list of items that would be returned with a string containing all the items
# separated by a comma and space, with 'and' inserted before the last item.

# This defines a function named commacode with parameter itemlist. itemlist contains the list of items that the user entered.
import sys
def commacode(itemlist):
    i = 0 # i represents the index of the list.
    while True: # Start of the loop. The index(i) will iterate from a range of 0 until length of the itemlist list minus 1.
        if i < len(itemlist) - 1:
            print (itemlist[i], end = ', ') # This will be printed as long as the index is less than the length of the itemlist-1.
            i += 1
        elif i == 0: # In case the user enters only 1 item on the list.
            print (itemlist[i]) # Only the single item will be displayed. No 'and' is appended.
            return
        else:
            print ('and '+ itemlist[i]) # When the index(i) is has reached the last item of the list, the word 'and' will be inserted
            return

itemlist = [] # Initializing the list
while True: # This is the user input loop.
    item = input('Please enter an item for your list or press Enter to stop. \nIf you do not wish to use this program, type in quit.\n')
    if item == 'quit': # Program will exit if user types in quit.
        sys.exit()
    elif item is not '': # List will be built for every item entered by the user.
        itemlist.append(item)
    else: # If user presses Enter, it is assumed that he has completed his list.
        break

commacode(itemlist) # This calls the function
