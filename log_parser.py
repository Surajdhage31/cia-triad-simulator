# Open and read the sample log file
log_file = "sample_auth.log"

print("[*] Parsing log file for suspicious activity...\n")

try:
    with open(log_file, "r") as file:
        for line in file:
            # Check if 'WARNING' or 'ALERT' is present in the log line
            if "WARNING" in line or "ALERT" in line:
                print(f"[!] SUSPICIOUS PATTERN FOUND: {line.strip()}")

except FileNotFoundError:
    print(f"[!] Error: The file {log_file} was not found.")
