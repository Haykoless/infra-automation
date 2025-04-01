import logging, subprocess, os

# Setup logging to a file
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/provisioning.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_bash(script="scripts/install_nginx.sh"):
    try:
        result = subprocess.run(["bash", script], check=True,
                                capture_output=True, text=True)
        logging.info("Bash output: %s", result.stdout)
    except Exception as e:
        logging.error("Bash script error: %s", e)

if __name__ == "__main__":
    logging.info("Provisioning started.")
    run_bash()
    logging.info("Provisioning finished.")