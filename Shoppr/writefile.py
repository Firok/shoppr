__author__ = 'batefirok'
import typeobject
from sys import getsizeof
from string import ascii_lowercase, digits
from random import randrange, randint, choice


class GenerateObject:
    """
        class for generating random of objects
    """

    def __init__(self, type):
        """
        :param type: type of object
        :return:
        """
        self.type = type

    def get_type(self):
        return  self.type

    def create_object(self):
        """
        create a random object
        :return:  return random object
        """

        # random object to return as result
        random_object = ''

        # set a random size of character of the random object from 1 and close to 19
        random_size = randrange(1,20)

        if self.type == typeobject.TypeObject.INTEGER.value:
            # case type of object is integer
            return random_object.join(choice(digits) for i in range(random_size))
        elif self.type == typeobject.TypeObject.ALPHABETICAL.value:
            # case type of object is alphabetical
            return random_object.join(choice(ascii_lowercase) for i in range(random_size))
        elif self.type == typeobject.TypeObject.ALPHANUMERIC.value:
            # case type of object is alphanumeric

            # random number of spaces before the random object alphanumeric between 1 and 10
            spaces = randint(1,10)
            for i in range(spaces):
                random_object += ' '

            # random object alphanumeric
            for i in range(random_size):
                random_object += choice(ascii_lowercase + digits)

            # random number of spaces after the random object alphanumeric
            spaces = randint(1,10)
            for i in range(spaces):
                random_object += ' '
        elif self.type == typeobject.TypeObject.REAL.value:
            # case type of object is real

            # reset random size from 2 to 19 as there will be one or more decimal place(s)
            random_size = randint(2,19)

            # random decimal separator position of the real from 0 to 18
            separator_position = randrange(random_size)

            # random object real
            for i in range(random_size):
                if i == separator_position:
                    random_object += '.'
                    continue
                random_object += choice(digits)
            # convert to float and back to string as we can have values as '.5' , '879.'
            random_object = str(float(random_object))

        return random_object

def create_file_objects():
    # file destination
    destination_file = r'random.txt'

    # init current output size to 0
    current_size = 0;

    # 10MB in bytes
    max_size = 10485760

    # open or create the file in mode write
    file_writer = open(destination_file, 'w')
    while current_size <= max_size:
        # create type object random value between 1 and 4
        random_type = randrange(1,5)

        # generate random object
        random_object = GenerateObject(random_type).create_object()

        # get size of random object in bytes and increment the current size
        current_size += getsizeof(random_object)

        # check if size is less or equal to max size 10MB
        if current_size <= max_size:
            # add random object separated with ',' to the file
            file_writer.write(random_object + ',')

    # close file
    file_writer.close()


# execute program
create_file_objects()