class helloWorld:
    """A really simple implementation of the `Hello World` program, using the
    classic `Single-Letter Decorator` paradigm.
    """
    string_length = 11

    def __init__(self):
        middle = "}{".join(["{}".format(i) for i in range(self.string_length)])
        self.empty = "%s%s%s" % ("{", middle, "}")

    @staticmethod
    def add_h(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+"h"
            return result
        return wrapper

    @staticmethod
    def add_e(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+"e"
            return result
        return wrapper

    @staticmethod
    def add_l(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+"l"
            return result
        return wrapper

    @staticmethod
    def add_o(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+"o"
            return result
        return wrapper

    @staticmethod
    def add_w(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+"w"
            return result
        return wrapper

    @staticmethod
    def add_r(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+"r"
            return result
        return wrapper

    @staticmethod
    def add_d(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+"d"
            return result
        return wrapper

    @staticmethod
    def add_space(func):
        def wrapper(*a, **k):
            result = func(*a, **k)
            result = result+" "
            return result
        return wrapper

    @property
    def functions(self):
        return [self.add_h,
                self.add_e,
                self.add_l,
                self.add_l,
                self.add_o,
                self.add_space,
                self.add_w,
                self.add_o,
                self.add_r,
                self.add_l,
                self.add_d]

    def empty_letter(self):
        return ""

    def main(self):
        dictionary = dict()
        for i, func in enumerate(self.functions):
            dictionary[i] = func(self.empty_letter)()
        empty_string = self.empty
        return f"{empty_string}".format(*list(dictionary.values()))

if __name__=="__main__":
    t = helloWorld()
    print(t.main())
