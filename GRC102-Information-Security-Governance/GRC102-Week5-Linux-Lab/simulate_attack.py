#!/usr/bin/env python3

import json
import datetime
import requests
import time

def simulate_struts_attack():
    """Simulate an attack scenario against the local Struts lab."""
    target_url = "http://127.0.0.1:8080"

    print("Simulating attack scenario on the Struts application...")

    try:
        # Check the local lab endpoint without executing an exploit payload.
        response = requests.get(target_url, timeout=5)

        print(f"Target responded with HTTP status: {response.status_code}")
        print("Recording a simulated incident for governance analysis...")

        time.sleep(1)

        attack_log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "attack_type": "Struts S2-045 attack scenario simulation",
            "target": "web_server",
            "success": False,
            "simulation_only": True,
            "data_accessed": "None; no data was accessed or exfiltrated",
            "records_affected": 0,
            "http_status": response.status_code,
            "note": "This script records a simulated incident; it does not exploit the vulnerability."
        }

        with open("attack_log.json", "w") as f:
            json.dump(attack_log, f, indent=2)

        print("Simulation completed. Log saved to attack_log.json")

    except requests.RequestException as e:
        print(f"Could not reach the local web application: {e}")
        print("Check that web_server is running and port 8080 is available.")

if __name__ == "__main__":
    simulate_struts_attack()
