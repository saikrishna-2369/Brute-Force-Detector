import re
import time
from collections import defaultdict
import requests   # Only if using Slack notifications

LOG_FILE = "login_attempts.log"
THRESHOLD = 3       # Failed attempts before block
TIME_WINDOW = 60    # Seconds
BLOCK_DURATION = 120  # Seconds to "block" an IP

# Optional: Slack webhook URL
SLACK_WEBHOOK = ""  # Add your webhook URL here if using notifications

failed_attempts = defaultdict(list)
blocked_ips = {}  # IP -> unblock timestamp

def follow(file):
    file.seek(0, 2)  # go to end of file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def send_slack(ip):
    if not SLACK_WEBHOOK:
        return
    message = {"text": f"🚨 Brute force detected from {ip}"}
    try:
        requests.post(SLACK_WEBHOOK, json=message)
    except Exception as e:
        print(f"⚠️ Failed to send Slack notification: {e}")

with open(LOG_FILE) as log:
    loglines = follow(log)
    for line in loglines:
        now = time.time()
        # Unblock IPs whose block duration expired
        for ip in list(blocked_ips):
            if now >= blocked_ips[ip]:
                print(f"✅ Unblocked IP {ip}")
                del blocked_ips[ip]

        if "Failed login" in line:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if ip_match:
                ip = ip_match.group(1)

                # Skip blocked IPs
                if ip in blocked_ips:
                    continue

                failed_attempts[ip].append(now)
                failed_attempts[ip] = [t for t in failed_attempts[ip] if now - t < TIME_WINDOW]

                if len(failed_attempts[ip]) >= THRESHOLD:
                    print(f"🚨 Brute force detected from {ip} - Blocking for {BLOCK_DURATION}s")
                    blocked_ips[ip] = now + BLOCK_DURATION
                    failed_attempts[ip] = []

                    # Optional: send notification
                    send_slack(ip)
