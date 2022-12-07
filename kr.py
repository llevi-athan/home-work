from re import sub

class NameConverterSnake():
    def __init__(self, name):
        self.name = name

    def to_snake_case(self):
        res = [self.name[0].lower()]
        for c in self.name[1:]:
            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ-':
                res.append('_')
                res.append(c.lower())
            else:
                res.append(c)
            if c in ('-'):
                res.remove('-')
        return ''.join(res)

class NameConverterCamel():
    def __init__(self, name):
        self.name = name

    def to_camel_case(self):
        capitalize_first = True
        if capitalize_first == True:
            self.name = sub(r"(_|-)+", " ", self.name).title().replace(" ", "")
            return self.name[0].title() + self.name[1:]
        else:
            self.name = sub(r"(_|-)+", " ", self.name).title().replace(" ", "")
            return self.name[0].lower() + self.name[1:]


if __name__ == '__main__':
    capitalize_first= True
    name = input("Ведите слово на английском")
    reg1 = NameConverterSnake(name)
    reg2 = NameConverterCamel(name)
    print("snake case - ", reg1.to_snake_case())
    print("camel case - ", reg2.to_camel_case())
