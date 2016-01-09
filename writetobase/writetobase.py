infile = raw_input('which file?')
nitrogen_database = open(infile, "a")

def main_event_loop():
    global nitrogen_database
    again = True 
    print "start writing to database \n"
    count = 0
    while again == True:
        print count
        repeat = raw_input("continue? (y/n/endli/enddi/newli/newdi): ")
        if repeat == "y":
            nitrogen_database.write(" "*28+"("+"'"+raw_input("Scientific \
Name: ")+"'"+", ")
            nitrogen_database.write(" "+"'"+raw_input("Common Name: ")+"'"+"),"+"\n")
            count += 1
        elif repeat == "n":
            nitrogen_database.close()
            again = False
        elif repeat == "endli":
            nitrogen_database.write(" "*20+"],\n"'\n')
        elif repeat == "enddi":
            nitrogen_database.write(" "*12+"}\n"'\n')
        elif repeat == "newli":
            nitrogen_database.write(" "*13+"'"+raw_input('list name:')+"'"+": [\n") 
        elif repeat == "newdi":
            nitrogen_database.write(raw_input('dictionary name:')+"= {\n")
        else:
            print "not a command dummie!"
            print
            print "try these:"
            print "Keep appending list = 'y'"
            print "start a new list = 'newli'"
            print "start a new dictionary = 'newdi'"
            print
            print "DO NOT FORGET TO END YOUR LISTS AND DICTIONARIES: 'endli' \
or 'enddi'... BEFORE STARTING A NEW ONE!"
    print "you wrote "+str(count)+" lines of data!"

main_event_loop()
