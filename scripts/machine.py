import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        logging.info(f"Machine created: {name}, OS: {os}, CPU: {cpu}, RAM: {ram}GB")

    def to_dict(self):
        return {"name": self.name, "os": self.os, "cpu": self.cpu, "ram": self.ram}
print("machine.py executed")