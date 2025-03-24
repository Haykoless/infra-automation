import json, os
from src.machine import Machine

def get_vm_input():
    name = input("VM name: ").strip()
    while not name:
        name = input("Name required. VM name: ").strip()

    os_input = input("OS (Ubuntu, CentOS, Windows): ").strip().lower()
    while os_input not in ['ubuntu', 'centos', 'windows']:
        os_input = input("Invalid OS. Choose Ubuntu, CentOS, or Windows: ").strip().lower()
    os_input = os_input.capitalize()

    def get_positive(prompt):
        while True:
            try:
                val = int(input(prompt))
                if val > 0:
                    return val
            except:
                pass
            print("Enter a positive integer.")

    cpu = get_positive("Number of CPUs: ")
    ram = get_positive("RAM in GB: ")
    return name, os_input, cpu, ram

def save_vm(vm, filepath="configs/instances.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append(vm.to_dict())
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print("Configuration saved.")

if __name__ == "__main__":
    details = get_vm_input()
    vm = Machine(*details)
    save_vm(vm)
