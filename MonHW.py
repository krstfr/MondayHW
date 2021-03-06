import re

##In-Class Exercise #3
##Print each persons name and twitter handle, using groups, should look like:
##==============
##Full Name / Twitter
##==============

##Derek Hawkins / @derekhawkins
##Erik Sven-Osterberg / @sverik
##Ryan Butz / @ryanbutz
##Example Exampleson / @example
##Ripal Pael / @ripalp
##Darth Vader / @darthvader

people = {
    'Derek Hawkins': '@derekhawkins',
    'Erik Sven-Osterberg': '@sverik',
    'Ryan Butz': '@ryanbutz',
    'Example Exampleson': '@example',
    'Ripal Pael': '@ripalp',
    'Darth Vader': '@darthvader',
}

for name,twitter in people.items():
    print(name.title() +" " + twitter.title())

##Regex project
##Use python to read the file regex_test.txt and print the 
##last name on each line using regular expressions and groups 
# (return None for names with no first and last name, or names that 
# aren't properly capitalized)
#Hint: use with open() and readlines()¶

#Step 1 get regex correct
pattern = re.compile("(([A-Z][a-z]+)( [A-Z][a-z]*)? ([A-Z][a-z]+))")
with open('regex-test.txt') as file:
    for lines in file.readlines():

        if pattern.match(lines): 
            print (lines)
        else:
            print("None")

#Step 2 run regex on each line inside "for" loop


    

