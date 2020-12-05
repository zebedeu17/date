class Elev:
    """Clasa elev"""

    def __init__(self, first, last, clasa, nota_mate, nota_info, nota_romana, nota_fizica, absenta_mate, absenta_info, absenta_romana, absenta_fizica):
        self.first = first
        self.last = last
        self.clasa = clasa
        self.nota_mate = nota_mate
        self.nota_info = nota_info
        self.nota_romana = nota_romana
        self.nota_fizica = nota_fizica
        self.absenta_mate = absenta_mate
        self.absenta_info = absenta_info
        self.absenta_romana = absenta_romana
        self.absenta_fizica = absenta_fizica

    @property
    def email(self):
        return '{}.{}@email.hu'.format(self.last, self.first)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Elev('{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.first, self.last, self.clasa, self.nota_mate, self.nota_info, self.nota_romana, self.nota_fizica, self.absenta_mate, self.absenta_info,self.absenta_romana, self.absenta_fizica)
