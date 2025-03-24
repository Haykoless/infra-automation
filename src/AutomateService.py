import json, os, subprocess
from src.machine import Machine

def get_vm():
    name = input("VM name: ").strip()
    while not name:
        name = input("Name required. VM name: ").strip()
    os_choice = input("OS (Ubuntu, CentOS, Windows): ").strip().lower()
    while os_choice not in ['ubuntu', 'centos', 'windows']:
        os_choice = input("Choose Ubuntu, CentOS, or Windows: ").strip().lower()
    cpu = int(input("Number of CPUs: "))
    ram = int(input("RAM in GB: "))
    return name, os_choice.capitalize(), cpu, ram

def save_vm(vm, path="configs/instances.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path) as f:
            data = json.load(f)
    except:
        data = []
    data.append(vm.to_dict())
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print("Configuration saved.")

def run_script(script="scripts/install_nginx.sh"):
    try:
        result = subprocess.run(["bash", script], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Script error:", e.stderr)

if __name__ == "__main__":
    vm = Machine(*get_vm())
    save_vm(vm)
    run_script()
