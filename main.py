

# read all the rulkes from the file
## everything before the empty line is the rules
## everything after the empty line are the updates

# 47|53, means that if an update includes both page number 47 and page number 53:
##    number 47 must be printed at some point before page number 53. (not necessarily immediately before)

# after all of the correct updates are stored, check for their middle value
# add all of the middle values togather and return the sum

def main():

    input_file = open("input_xs.txt", "r")
    lines = input_file.readlines()
    input_file.close()
    
    rules = []
    updates = []
    for line in lines:
        if line == "\n":
            break
        rules.append(line)

    for line in lines[len(rules)+1:]:
        updates.append(line)

    # clean the \n from the strings
    rules = [rule.strip() for rule in rules]
    updates = [update.strip() for update in updates]

    print("Rules: ", rules)
    print("Updates: ", updates)

    # create a dictionary to store the rules 
    # key: page number, value: the page numbers that it must come before

    rules_dict = {}
    for rule in rules:
        pages = rule.split("|")
        key = pages[0]
        if key not in rules_dict:
            rules_dict[key] = []
        for page in pages[1:]:
            rules_dict[key].append(page)

    # make a list with all of the valid updates
    # key must be printed at some point before values. (not necessarily immediately before)

    valid_updates = []
    for update in updates:
        pages = update.split(",")
        valid = True
        for page in pages:
            key = page
            values = pages[pages.index(page)+1:]
            print("Key: ", key)
            print("Values: ", values)

            # check that all of the values after the key are not supposed to come before the key
            for value in values:
                if value in rules_dict:
                    if key in rules_dict[value]:
                        valid = False
                        break
        if valid:
            valid_updates.append(update)

    print("Valid Updates: ", valid_updates)

    # find the middle value of all of the valid updates
    middle_values = []
    for update in valid_updates:
        pages = update.split(",")
        middle_values.append(pages[len(pages)//2])

    print("Middle Values: ", middle_values)

    # add all of the middle values together
    sum = 0         
    for value in middle_values:
        sum += int(value)
    print("Sum: ", sum)       
        



if __name__ == "__main__":
    main()

