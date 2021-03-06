from string import *

# Unit testing framework for hangman project
# each function should run tests with intuitive output, and printing ok for passed and 
# Failed for failed tests.  Each function should return 0 if test was passed, and 1 if there 
# were one or more errors.

def string_inst_test():
    errors = 0 
    print ("instantiating string 'Hello'")
    string = String("Hello")
    if isinstance(string, String):
        print("ok, string instantiated")
    else:
        print("Failed - string not instantiated correctly")
        errors = errors + 1
    size = string.get_size()
    if size == 5: 
        print("ok, string size stored and retrieved correctly")
    else:
        print("Failed: string size incorrect: " + str(size))
        errors = errors + 1
    cap = string.get_capacity() 
    if cap == 6:
        print("ok, string capacity stored and retrieved correctly")
    else:
        print("Failed: string capacity incorrect : " + str(cap))
        errors = errors + 1
    print("\n\n")
    return errors > 0

def string_compare_test():
    errors = 0
    print("Instantiating strings 'Hello', 'World', and 'Hello'")
    string1 = String("Hello")
    string2 = String("World")
    string3 = String("Hello")
    print("Comparing 'Hello' with 'Hello'")
    c = my_string_compare(string1, string3)
    succ_str = 'Failed: '
    if c == 0:
        succ_str = 'ok, '
    else:
        errors = errors + 1
    print(succ_str + "Expecting 0; got " + str(c))

    print("Comparing 'Hello' with 'World'")
    c = my_string_compare(string1, string2)
    succ_str = 'Failed: '
    if c < 0:
        succ_str = 'ok, '
    else:
        errors = errors + 1
    print(succ_str + "Expecting integer less than 0; got " + str(c))

    print("Comparing 'World' with 'Hello'")
    c = my_string_compare(string2, string1)
    succ_str = 'Failed: '
    if c > 0:
        succ_str = 'ok, '
    else:
        errors = errors + 1
    print(succ_str + "Expecting integer Greater than 0; got " + str(c))
    print("\n\n")
    return errors > 0

def string_insert_test():
    errors = 0
    s1 = String("The quick brown fox")
    fp = open('dict.txt', 'w')
    print("Writing string to file dict.txt")
    t = my_string_insertion(s1, fp)
    if t:
        print ("Ok, expected true got True")
    else:
        print("Failed, expected True got False")
        errors = errors + 1
    return errors > 0

def string_extract_test():
    errors = 0
    s1 = String()
    print("Attempting to read the first word from 'dict.txt'")
    fp = open('dict.txt', 'r')
    my_string_extraction(s1, fp)
    if my_string_compare(s1, String("The")) != 0:
        print("Failed: Expected string not read in from file: ")
        my_string_insertion(s1)
        errors = errors + 1
    else:
        print("Success, word read correctly.")
    return errors > 0
test_list = [string_inst_test, string_compare_test, string_insert_test, string_extract_test]

def run_tests():
    failed = 0
    for i in test_list:
        failed = failed + i()
    return

run_tests()