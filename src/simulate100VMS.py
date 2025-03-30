import json, os, subprocess, sys
# Simulate provisioning 100 VMs with a bash script
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from schemas import VMModel


CONFIG_PATH = "configs/instances.json"
SCRIPT_PATH = "scripts/Bash Scripts/install_nginx.sh"

os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)


try:
    with open(CONFIG_PATH, "r") as f:
        all_vms = json.load(f)
except:
    all_vms = []


for i in range(1, 101):
    name = f"vm-{i}"
    vm = VMModel(name=name, os="ubuntu", cpu=2, ram=4)
    all_vms.append(vm.dict())

    print(f"[{i}/100] Provisioning {name}...")

    
    try:
        result = subprocess.run(["bash", SCRIPT_PATH], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error provisioning {name}: {e.stderr}")


with open(CONFIG_PATH, "w") as f:
    json.dump(all_vms, f, indent=4)

print("Finished provisioning 100 VMs (simulated).")
