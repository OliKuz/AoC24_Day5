

# read all the rulkes from the file
## everything before the empty line is the rules
## everything after the empty line are the updates

# 47|53, means that if an update includes both page number 47 and page number 53:
##    number 47 must be printed at some point before page number 53. (not necessarily immediately before)

# after all of the correct updates are stored, check for their middle value
# add all of the middle values togather and return the sum

# TASK 2: Fix the incorrect updates and return the sum of the middle values

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
    invalid_updates = []

    for update in updates:
        pages = update.split(",")
        valid = True
        for page in pages:
            key = page
            values = pages[pages.index(page)+1:]

            # check that all of the values after the key are not supposed to come before the key
            for value in values:
                if value in rules_dict:
                    if key in rules_dict[value]:
                        valid = False
                        break
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    print()
    print("Valid Updates: ", valid_updates)

    # find the middle value of all of the valid updates
    middle_values = []
    for update in valid_updates:
        pages = update.split(",")
        middle_values.append(pages[len(pages)//2])

    # add all of the middle values together
    sum = 0         
    for value in middle_values:
        sum += int(value)
    print("Sum: ", sum)    

    print()

    print("Invalid Updates: ", invalid_updates)   

    # T2 fix the updates
    fixed_updates = []
    go = True
    new_invalid_updates = invalid_updates

    while (go):
        # continue checking until the updates are no longer being fixed
        fixed_updates = fix(new_invalid_updates, rules_dict)
        if fixed_updates == new_invalid_updates:
            go = False
        new_invalid_updates = fixed_updates


    print()
    print("Fixed Updates: ", fixed_updates)

    middle_values = []
    for update in fixed_updates:
        pages = update.split(",")
        middle_values.append(pages[len(pages)//2])

    sum = 0
    for value in middle_values:
        sum += int(value)
    
    print("Fixed Sum: ", sum)

                        



def fix(invalid_updates, rules_dict):

    fixed_updates = []

    for update in invalid_updates:
        pages = update.split(",")
        for page in pages:
            key = page
            values = pages[pages.index(page)+1:]

            for value in values:
                if value in rules_dict:
                    if key in rules_dict[value]:
                        print("Fixing: ", key, value)
                        # try reordering the by swapping the key and value
                        key_index = pages.index(key)
                        value_index = pages.index(value)
                        pages[key_index], pages[value_index] = pages[value_index], pages[key_index]
                        update = ",".join(pages)
                        print("Fixed: ", update)

        fixed_updates.append(update)

    return fixed_updates
        



if __name__ == "__main__":
    main()

