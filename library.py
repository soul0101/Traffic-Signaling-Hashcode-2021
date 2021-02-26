

class Street(object):
    def __init__(self, index, B, E, name, time):
        self.index = index
        self.B = B
        self.E = E
        self.name = name
        self.time = time

    def __repr__(self):
        return '[id:{}-B:{}-E:{}-name:{}]'.format(self.index, self.B, self.E, self.name)

class Car(object):
    def __init__(self, index, num, street):
        self.index = index
        self.num = num
        self.street = street

    def __repr__(self):
        return '[id:{}-len:{}-{}]'.format(self.index, self.num, self.street)





class Light(object):
    def __init__(self, intersection, street, time):
        self.intersection = intersection
        self.street = street
        self.time = time
            
    def __repr__(self):
        return '[id:{}-street:{}-time:{}]'.format(self.intersection, self.street, self.time)
