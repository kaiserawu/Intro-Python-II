# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.n_to = kwargs.get('n_to')
        self.s_to = kwargs.get('s_to')
        self.e_to = kwargs.get('e_to')
        self.w_to = kwargs.get('w_to')
    def __str__(self):
        return f'\n ---{self.name}--- \n{self.description}\n'