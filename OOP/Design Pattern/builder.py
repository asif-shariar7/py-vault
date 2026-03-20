class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f"Cpu: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"    



class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def get_cpu(self, cpu):
        self.cpu = cpu
        return self 

    def get_ram(self, ram):
        self.ram = ram
        return self  

    def get_storage(self, storage):
        self.storage = storage
        return self
    def build(self):
        return Computer(self.cpu, self.ram, self.storage)   


builder = ComputerBuilder()

obj = builder.get_cpu("Intel i9").get_ram("32GB").get_storage("1TB").build()
print(obj)


