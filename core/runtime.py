import os

RUNTIME_FOLDER = 'runtime'

class Runtime:
    def __init__(self) -> None:
        self.__is_initialized = False

        self.create_folder(RUNTIME_FOLDER)

    def create_folder(self, name : str) -> None:
        if not self.__is_initialized:
            path = name
            self.__is_initialized = True

        else:
            path = os.path.join(RUNTIME_FOLDER, name)

        if not os.path.exists(path = path):
            os.makedirs(path)

    @classmethod
    def path(self) -> str:
        return RUNTIME_FOLDER