# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
    # dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems),
#   where the inventory parameter is a dictionary representing the player’s inventory and the addedItems parameter is a list like dragonLoot.
# The addToInventory() function should return a dictionary that represents the updated inventory.
# Note that the addedItems list can contain multiples of the same item.

#! usr/bin/#!/usr/bin/env python

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0 # counter for items
    for k, v in inventory.items(): # for loop to iterate through keys and values
        print(str(v) + ' ' + (k)) # will print value + key with strings
        item_total = item_total + inventory[k] # will add total items
    print("Total number of items: " + str(item_total))
displayInventory(stuff)

print()

#######

def addToInventory(inventory, addedItems): # Defines function addToInventory with parameters inventory (inv) and addedItems.(dragonLoot)
    for loot in addedItems: #will iterate through dragonLoot
        inventory.setdefault(loot,0)
        inventory[loot] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1} # dictionary for inventory
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] # list for additional loot
inventory = addToInventory(inv, dragon_loot) # will define inventory to be equal to inv+dradon loot

displayInventory(inv)
