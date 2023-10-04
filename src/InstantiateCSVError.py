class InstantiateCSVError(Exception):
    def __init__(self, *args):
        """
        File item.csv is corrupted
        """
        if args:
            self.massage = args[0]
        else:
            self.massage = 'InstantiateCSVError: Файл item.csv поврежден'
