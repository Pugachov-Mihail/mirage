import os


class FindPath:
    def __init__(self):
        self.__path = os.getcwd()
        self.__files = os.listdir(self.__path)

        for i in self.__create_path_to_files():
            self.__set__(self, i)

    def __set__(self, instance, value):
        for i in self.__files:
            instance.__dict__[i] = FolderFollow(value, i)

    def __create_path_to_files(self):
        path_to_files = []
        for i in self.__files:
            path = self.__path + "\\" + i
            path_to_files.append(path)
        return path_to_files


class FolderFollow:
    def __init__(self, path_to_files, name):
        if os.path.isdir(path_to_files):
            self.name = name
            self.folder = True
        else:
            self.folder = False
            return

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __repr__(self):
        return f'{self.name}, {self.folder}'

    @classmethod
    def isFiles(cls, value):
        file = None
        if os.path.isfile(value):
            file = False
        elif os.path.isdir(value):
            file = True
        return file
