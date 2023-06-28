class Ignore:
    IGNORE_MODE = False

    def __init__(self):
        self.__ignore_files = []

        with open('.ignore', 'r') as f:
            try:
                self.__ignore_files.append(f.readline())
            except FileNotFoundError:
                self.IGNORE_MODE = True

    def __know_value(self, value):
        pass

    def find_ignore(self):
        a = map(str, self.__ignore_files)



