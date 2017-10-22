from collections import namedtuple
from cliar import Cliar


Person = namedtuple('Person', ('firstname', 'lastname'))


def string_to_person(string):
    """Create a ``Person`` from a string.

    :param string: Space-separated string of first and last names, e.g. ``John Smith``

    :returns: ``Person`` instance.
    """

    try:
        return Person(*string.split())
    except Exception as e:
        print('Conversion failed')
        return None


class CustomParser(Cliar):
    """This CLI demonstrates the usage
    of a custom arg parser.
    """

    def personify(self, person:string_to_person):
        """This method uses a custom ``string_to_person``
        parser to convert input string into a ``Person`` instance
        *before* handling it.
        """

        if person is not None:
            print('First name:', person.firstname)
            print('Last name:', person.lastname)


if __name__ == '__main__':
    CustomParser().parse()