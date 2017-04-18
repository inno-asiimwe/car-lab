class Car(object):
    def __init__(self, name = 'General', model = 'GM', typ = None ):
        self.type = typ
        self.model = model
        self.name = name
        self.speed = 0

        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.type != 'trailer':
            self.num_of_wheels = 4
        else:
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.type != 'Trailer':
            return True
        else:
            return False

    def drive(self, factor):
        if factor == 7:
            self.speed = 77
        elif factor ==3:
            self.speed = 1000
        return self
