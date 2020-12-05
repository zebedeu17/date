class Profesor:
    """Clasa profesor"""

    def __init__(self, first, last, materie):
        self.first = first
        self.last = last
        self.materie = materie

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.last, self.first)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Profesor('{}', '{}')".format(self.first, self.last, self.materie)
