"""
First of all, what is private in other languages?

Private is a kind of status given to attribute or method, which secures from using it from outside a class.
It can be used internally, but if we want to call it or change it from outside the class,
we need to use special interface-like methods.
For attributes we usually have two separate methods named in convention like getX and setX or x_getter and x_setter.
This way attribute 'x' is protected from direct access.

This assures that other developers will use objects in way they were supposed to,
so the code is simpler, easier to maintain and acts predictable.

Our seniority levels describes "private" attributes in double quotes for a reason.
Python don't have any real private properties. Basically there is only a naming convention.
"""


class Tree:
    def __init__(self, is_fruit_tree: bool):
        self.is_fruit_tree = is_fruit_tree          # for some reason, this value needs to be accessible

    def take_a_fruit(self):
        if self.is_fruit_tree:
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

    # All problems starts here. Our class is vulnerable
    # t.is_fruit_tree = 'false'       # reassign with invalid values
    # del t.is_fruit_tree               # breaking object

    t.take_a_fruit()

    print()
    print(dir(t))
    print(vars(t))
