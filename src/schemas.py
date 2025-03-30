import json, os
from pydantic import BaseModel, validator

class VMModel(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int

    @validator("name")
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("VM name cannot be empty")
        return v

    @validator("os")
    def validate_os(cls, v):
        valid = ["ubuntu", "centos", "windows"]
        if v.lower() not in valid:
            raise ValueError(f"Invalid OS. Choose: {', '.join(valid)}")
        return v.lower()

    @validator("cpu", "ram")
    def validate_positive(cls, v):
        if v <= 0:
            raise ValueError("Value must be a positive integer")
        return v

def get_positive(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0: return val
        except: pass
        print("Enter a positive integer.")

def get_vm_input():
    name = input("VM name: ").strip()
    os_input = input("OS (Ubuntu, CentOS, Windows): ").strip().lower()
    cpu = get_positive("CPUs: ")
    ram = get_positive("RAM (GB): ")
    return name, os_input, cpu, ram

def save_vm(vm, path="configs/instances.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try: data = json.load(open(path))
    except: data = []
    data.append(vm.dict())
    json.dump(data, open(path, "w"), indent=4)
    print("VM configuration saved.")

if __name__ == "__main__":
    try:
        vm = VMModel(*get_vm_input())
        save_vm(vm)
    except Exception as e:
        print("Validation failed:", e)
