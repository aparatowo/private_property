from see import see

class Tree:
    def __init__(self, is_fruit_tree: bool):
        self.__is_fruit_tree = is_fruit_tree  # for some reason, this value needs to be accessible

    @property
    def is_fruit_tree(self):  # introduce property
        pass

    @is_fruit_tree.getter
    def is_fruit_tree(self):  # now this is a getter
        # return str(self._is_fruit_tree).upper()     # and we can put some logic here
        return self.__is_fruit_tree

    @is_fruit_tree.setter
    def is_fruit_tree(self, user_input): # this is a setter
        if user_input in ['f', 'false']:
            self.__is_fruit_tree = False
        else:
            self.__is_fruit_tree = bool(user_input)   # we should deal with input here so we have normalized attr values

    @is_fruit_tree.deleter
    def is_fruit_tree(self):  # this is a deleter
        self.__is_fruit_tree = False

    def take_a_fruit(self):
        if self.__is_fruit_tree:

            print("""
                  ,--./,-.
                 / #      \\
                |          |
                 \\        /
                  `._,._,'
    
            Here is your fruit.
            Art by Hayley Jane Wakenshaw""")
        else:
            print("No fruits here")


if __name__ == "__main__":
    t = Tree(True)

    # TODO: we should cover this
    # t.is_fruit_tree = 'false'       # reassign with invalid values
    # del t.is_fruit_tree             # breaking object

    t.take_a_fruit()

    print()
    print(see(t))
    print()
    print(dir(t))
    print(vars(t))
