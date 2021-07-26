class Tree:
    def __init__(self, is_fruit_tree: bool):
        self._is_fruit_tree = is_fruit_tree  # for some reason, this value needs to be accessible

    @property
    def is_fruit_tree(self):  # this is basically getter
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
    # t._is_fruit_tree = False        # still breakable
    # del t.is_fruit_tree             # breaking object
    # del t._is_fruit_tree             # breaking object

    t.take_a_fruit()

    print()
    print(dir(t))
    print(vars(t))
