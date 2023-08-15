import os

RUNTIME_FOLDER = 'runtime'

class Runtime:
    def __init__(self) -> None:
        self.__is_initialized = False
        
        self.FOLDER = RUNTIME_FOLDER
        self.create_folder(self.FOLDER)

    def create_folder(self, name : str) -> str:
        if not self.__is_initialized:
            path = name
            self.__is_initialized = True

        else:
            path = os.path.join(self.FOLDER, name)

        if not os.path.exists(path = path):
            os.makedirs(path)

        return path
