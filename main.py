class ConfigCache:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "is_initialized"):
            self.instruction = None
            self.modules = None
            self.themes = None
            self.is_initialized = True

    def make_cache(self, a, b, c):
        self.instruction = a
        self.modules = b
        self.themes = c

    def show_cache(self):
        print(self.instruction, self.modules, self.themes, sep=' Kb, ', end=' Kb\n')


cache1 = ConfigCache()
cache1.make_cache(5, 60, 23)
cache1.show_cache()

cache2 = ConfigCache()
cache2.show_cache()
print(cache1 is cache2)