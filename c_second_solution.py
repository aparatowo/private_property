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

    # t.__is_fruit_tree = False        # what happened with dir/vars?
    # del t.__is_fruit_tree

    # t._Tree__is_fruit_tree = False        # still breakable
    # del t._Tree__is_fruit_tree

    t.take_a_fruit()

    print()
    print(dir(t))
    print(vars(t))

    # We are consenting adults

    # install see via "pip install see" command
    # from see import see
    # print(see(t))  # best to use in terminal
