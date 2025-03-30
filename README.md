# infra-automation

##Project Overview

# infra-automation is a hybrid Python and Bash automation toolkit for provisioning, configuring, and testing cloud or local infrastructure setups. It modularizes infrastructure tasks into shell scripts for setup and Python for validations or logic-heavy operations.

##Objectives

- Automate infrastructure setup across environments.
- Use Bash for quick system operations and Python for processing logic.
- Separate configs, scripts, and source logic for clarity and reusability.

##Project Structure


##Setup Instructions

###Prerequisites

- Linux/macOS or WSL
- Bash
- Python 3.8+
- Installed CLI tools depending on use case (e.g., kubectl ,aws , etc.)

###Installation

bash
git clone https://github.com/Haykoless/infra-automation.git
cd infra-automation
chmod +x scripts/*.sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

VM configuration saved.
Bash script started...
Nginx installed successfully (simulated).
Provisioning finished.
