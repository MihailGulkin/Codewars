class FileMaster():
    def __init__(self, filepath):
        self._dir_path, self._filename, self._extension = \
            self.__splits(filepath)

    def extension(self):
        return self._extension

    def filename(self):
        return self._filename

    def dir_path(self):
        return f'{self._dir_path}/'

    @staticmethod
    def __splits(path: str):
        path = path.rsplit('/', 1)
        return path[0], *path[1].split('.')
