class Singleton:
    def __new__(cls):
        """
        The python's __new__ method runs before __init__
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Creating {cls.instance} object')
        return cls.instance


def main() -> None:
    """
    Shows that only a single instance is created
    :return: None
    """
    s1 = Singleton()
    print(f'Id of instance 1: {id(s1)}')

    dict_singleton = {}
    for index in range(2, 11):
        dict_singleton[index] = Singleton()
        print(f'Id of instance {index}: {id(dict_singleton[index])}')


if __name__ == '__main__':
    main()
