from string import *

# Unit testing framework for hangman project
# each function should run tests with intuitive output, and printing ok for passed and 
# Failed for failed tests.  Each function should return 0 if test was passed, and 1 if there 
# were one or more errors.

def string_inst_test():
    errors = 0 
    print("Testing string instantiation, size and capacity")
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
    print("Testing string compare function")
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
    print("Testing string insertion function")
    s1 = String("The quick brown fox")
    fp = open('dict.txt', 'w')
    print("Writing string to file dict.txt")
    t = my_string_insertion(s1, fp)
    if t:
        print ("Ok, expected true got True")
    else:
        print("Failed, expected True got False")
        errors = errors + 1
    print("\n\n")
    return errors > 0

def string_extract_test():
    errors = 0
    s1 = String()
    print("Testing string extraction function")
    print("Attempting to read the first word from 'dict.txt'")
    fp = open('dict.txt', 'r')
    my_string_extraction(s1, fp)
    if my_string_compare(s1, String("The")) != 0:
        print("Failed: Expected string not read in from file: ")
        my_string_insertion(s1)
        errors = errors + 1
    else:
        print("Success, word read correctly.")
    print("\n\n")
    return errors > 0

def string_at_test():
    errors = 0
    s1 = String("Hello!")
    c = my_string_at(s1, 0)
    print("Testing my string at function")
    print("checking the second index of the string \"Hello!\"")
    if c == 'H':
        print ("ok, expecting H got " + c)
    else:
        print ("Failed: expecting H got " + c)
        errors = errors + 1
    print("Checking an out of bounds index")
    c = my_string_at(s1, 600)
    if c == False:
        print ("ok, out of bounds case handled correctly")
    else:
        print("Failed: Out of bounds case did not return None")
        errors = errors + 1
    print("Checking edge cases")
    c = my_string_at(s1, 6)
    if c == None:
        print("ok, edge case handled correctly.")
    else:
        print("Failed: edge case did not return None")
        errors = errors + 1
    c = my_string_at(s1, 5)
    if c == '!':
        print("ok, edge case handled correctly")
    else:
        print("Failed, in bounds edge case did not return correct char")
        errors = errors + 1
    print("\n\n")
    return errors > 0

def string_push_back_test():
    errors = 0
    print("Testing string push back function")
    print("Testing null string case")
    string = None
    c = my_string_push_back(string, '1')
    if c == False:
        print("ok, expected False got False")
    else:
        print("Failed: expected False")
        errors = errors + 1
    print("Testing empty string case")
    string = String()
    c = my_string_push_back(string, '1')
    if c == True and my_string_at(string, 0) == '1':
        print("ok, expected true and '1', got true and '1'")
    else:
        print("Failed: Expected true and '1'")
        errors = errors + 1
    print("Testing regular string case")
    string = String("Hello")
    c = my_string_push_back(string, '!')
    if c == True and my_string_at(string, 5) == '!':
        print("ok, expected True and '!' and got True and '!'")
    else:
        print("Failed: expected True and '!'")
        errors = errors + 1
    print("\n\n")
    return errors > 0

def string_pop_back_test():
    errors = 0
    print("Testing string pop back function")
    print("Testing empty string")
    string = String()
    c = my_string_pop_back(string)
    if c == False:
        print("ok, expected False got False")
    else:
        print("Failed: expected False, got " + str(c))
        errors = errors + 1
    print("Testing null case")
    string = None
    c = my_string_pop_back(string)
    if c == False:
        print("ok, expected False got False")
    else:
        print("Failed: expected False, got " + str(c))
        errors = errors + 1
    print("Testing valid string case")
    string = String("Hello")
    c = my_string_pop_back(string)
    if c == True and string.get_size() == 4:
        print("ok, expected True got True")
    else:
        print("Failed: expected True and 4 got " + str(c), " and " + str(string.get_size()) )
        errors = errors + 1
    print("\n\n")
    return errors > 0

def string_c_string_test():
    print("Testing my string c string function")
    errors = 0
    print("Testing none case")
    string = None
    c = my_string_c_string(string)
    if c == None:
        print("ok, expected None got None")
    else:
        print("Failed: expected None got " + str(c))
        errors = errors + 1
    print("Testing valid string case")
    string = String("Hello!")
    c = my_string_c_string(string)
    if c == "Hello!":
        print("ok, expected 'Hello!' got " + str(c))
    else:
        print("Failed: expected 'Hello!', got " + str(c))
        errors = errors + 1
    print("Testing empty string case")
    string = String()
    c = my_string_c_string(string)
    if c == '':
        print("ok, expected '' got ''")
    else:
        print("Failed: expected '' got " + str(c))
        errors = errors + 1
    print("\n\n")
    return errors > 0

def string_empty_test():
    errors = 0
    print("Testing my string empty function")
    print("Testing none case")
    string = None
    c = my_string_empty(string)
    if c == False:
        print("ok, expected false got false")
    else:
        print("Failed: expected false got " + str(c))
        errors = errors + 1
    print("Testing empty case")
    string = String()
    c = my_string_empty(string)
    if c == True:
        print("ok, expected True got True")
    else:
        print("Failed: expected True got " + str(c))
        errors = errors + 1  
    print("Testing non-empty case")
    string = String("Hello!")
    c = my_string_empty(string)
    if c == False:
        print("ok, expected False got False")
    else:
        print("Failed: expected False got " + str(c))
        errors = errors + 1
    print("\n\n")
    return errors > 0

def string_assignment_test():
    errors = 0
    print("Testing string assignment function")
    print("Testing none case")
    string1 = None
    string2 = String("Hello!")
    c = my_string_assignment(string1, string2)
    if c == False:
        print("ok, expected False got False")
    else:
        print("Failed: expected False got " + str(c))
        errors = errors + 1
    print("Testing valid strings")
    string1 = String("World")
    c = my_string_assignment(string1, string2)
    if c == True:
        print("ok, expected True got True")
    else:
        print("Failed: expected True got " + str(c))
        errors = errors + 1
    print("\n\n")
    return errors > 0

test_list = [string_inst_test, string_compare_test, string_insert_test, string_extract_test,
string_at_test, string_push_back_test, string_pop_back_test, string_c_string_test, string_empty_test, string_assignment_test]

def run_tests():
    failed = 0
    for i in test_list:
        failed = failed + i()
    return

run_tests()
