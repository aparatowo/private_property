class Tree:
    def __init__(self, is_fruit_tree: bool):
        self._is_fruit_tree = is_fruit_tree  # for some reason, this value needs to be accessible

    @property
    def is_fruit_tree(self):  # introduce property
        pass

    @is_fruit_tree.getter
    def is_fruit_tree(self):  # now this is a getter
        # return str(self._is_fruit_tree).upper()     # and we can put some logic here
        return self._is_fruit_tree

    def take_a_fruit(self):
        if self._is_fruit_tree:

            print("""
              ,--./,-.
             / #      \\
            |          |
             \        /
              `._,._,'

        Here is your fruit.
        Art by Hayley Jane Wakenshaw""")
        else:
            print("No fruits here")


if __name__ == "__main__":
    t = Tree(True)

    # t.is_fruit_tree = 'false'       # reassign with invalid values
    # del t.is_fruit_tree             # breaking object
    # t._is_fruit_tree = False        # still breakable
    # del t._is_fruit_tree             # breaking object

    t.take_a_fruit()

    print()
    print(dir(t))
    print(vars(t))
