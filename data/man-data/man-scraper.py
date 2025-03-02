import subprocess
from tqdm import tqdm

# List of UNIX commands to scrape
commands = [
    "ls", "cd", "pwd", "rm", "cp", "mv", "mkdir", "cat", "wc",
    "grep", "find", "chmod", "chown", "tar", "ps", "kill", "echo",
    "cut", "awk", "sed", "top", "ssh", "nmap", "netcat", "telnet",
    "man", "sftp",
            ]

output_file = "unix_commands.txt"

def fetch_man_page(command):
    """Fetch the full man page for a command."""
    try:
        output = subprocess.run(["man", command], capture_output=True, text=True)
        return output.stdout.strip()
    except Exception as e:
        print(f"Failed to fetch man page for {command}: {e}")
        return None

# Scrape man pages and save to file
with open(output_file, "w") as f:
    for cmd in tqdm(commands, desc="Scraping man pages"):
        man_text = fetch_man_page(cmd)
        if man_text:
            f.write(f"COMMAND: {cmd}\n")
            f.write(f"{man_text}\n\n{'='*80}\n\n")  # Separator for readability

print(f"Dataset saved to {output_file}")