__author__ = 'batefirok'

def read_file():
    # file destination
    destination_file = r'random.txt'

    try:
        # open the file in mode read
        file_reader = open(destination_file, 'r')

        # get all random objects from the file
        all_random_objects = file_reader.read()

        # map all random objects to a list of string by using split
        list_random_objects = all_random_objects.split(',')

        # traverse list random objects
        for random_object in list_random_objects:

            if random_object.__contains__(' '):
                # case alphanumeric
                print(random_object.strip() + ' - alphanumeric')
            elif random_object.__contains__('.'):
                # case real
                print(random_object + ' - real numbers')
            elif random_object.isdigit():
                # case integer
                print(random_object + ' - integer')
            elif random_object.isalpha():
                # case alphabetical strings
                print(random_object + ' - alphabetical strings')

    except:
        print("Some errors occurred! Make sure the file exists")

# execute program
read_file()