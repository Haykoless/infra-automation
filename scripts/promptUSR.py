import json, os

def get_vm_input():
    name = input("VM name: ").strip()
    while not name:
        name = input("Name can't be empty. VM name: ").strip()

    os_input = input("OS (Ubuntu, CentOS, Windows): ").strip().lower()
    while os_input not in ['ubuntu', 'centos', 'windows']:
        os_input = input("Invalid OS. Choose Ubuntu, CentOS, or Windows: ").strip().lower()

    def get_int(prompt):
        while True:
            try:
                val = int(input(prompt))
                if val > 0:
                    return val
            except:
                pass
            print("Enter a positive integer.")

    cpu = get_int("Number of CPUs: ")
    ram = get_int("RAM in GB: ")
    return {"name": name, "os": os_input.capitalize(), "cpu": cpu, "ram": ram}

def save_vm(vm, filepath="configs/instances.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        with open(filepath) as f:
            data = json.load(f)
    except:
        data = []
    data.append(vm)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print("Configuration saved.")

if __name__ == "__main__":
    vm = get_vm_input()
    save_vm(vm)
