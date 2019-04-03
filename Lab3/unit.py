from string import String

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
    if string.get_size() == 5: 
        print("ok, string size stored and retrieved correctly")
    else:
        print("Failed: string size incorrect")
        errors = errors + 1
    if string.get_capacity() == 6:
        print("ok, string capacity stored and retrieved correctly")
    else:
        print("Failed: string capacity incorrect")
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
    c = string1.my_string_compare(string1, string3)
    succ_str = 'Failed: '
    if c == 0:
        succ_str = 'ok, '
    else:
        errors = errors + 1
    print(succ_str + "Expecting 0; got " + str(c))

    print("Comparing 'Hello' with 'World'")
    c = string1.my_string_compare(string1, string2)
    succ_str = 'Failed: '
    if c < 0:
        succ_str = 'ok, '
    else:
        errors = errors + 1
    print(succ_str + "Expecting integer less than 0; got " + str(c))
    print("\n\n")
    return errors > 0


test_list = [string_inst_test, string_compare_test]

def run_tests():
    failed = 0
    for i in test_list:
        failed = failed + i()
    return

run_tests()