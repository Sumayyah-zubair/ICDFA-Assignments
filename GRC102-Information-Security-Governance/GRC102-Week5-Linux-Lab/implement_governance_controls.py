#!/usr/bin/env python3

import os
import json
import datetime
import argparse
from governance_tracker import GovernanceTracker

TODAY = datetime.datetime.now().strftime("%Y-%m-%d")

def record_patch_status(patch_id):
    """Record the lab's simulated patch status."""
    status = {
        "struts_patched": False,
        "mysql_secured": False,
        "network_segmented": False
    }

    if os.path.exists("patch_status.json"):
        with open("patch_status.json", "r") as f:
            status.update(json.load(f))

    if patch_id == "PATCH-001":
        status["struts_patched"] = True
    elif patch_id == "PATCH-002":
        status["mysql_secured"] = True
    elif patch_id == "PATCH-003":
        status["network_segmented"] = True

    with open("patch_status.json", "w") as f:
        json.dump(status, f, indent=2)

    print(f"{patch_id}: simulated status recorded. This does not apply a real fix.")

def add_control(name, description, owner):
    tracker = GovernanceTracker()
    tracker.add_control(name, description)
    print(f"Recorded governance control: {name}")

def implement_monitoring():
    os.makedirs("monitoring", exist_ok=True)

    script = """#!/bin/bash
# Educational monitoring example. Does not access production logs or credentials.
LOG_FILE="./monitoring/security_monitor.log"
date '+%Y-%m-%d %H:%M:%S - Monitoring check executed' >> "$LOG_FILE"
echo "Monitoring check recorded in $LOG_FILE"
"""
    with open("monitoring/security_monitor.sh", "w") as f:
        f.write(script)
    os.chmod("monitoring/security_monitor.sh", 0o755)

    print("Created a basic lab monitoring script. Configure and test real log sources before relying on alerts.")

def implement_oversight():
    content = """# Security Governance Oversight

## Roles and Responsibilities
- Executive leadership: approve security priorities and resources.
- Security lead: coordinate the security programme and report risks.
- System owners: remediate vulnerabilities and provide evidence.
- Database administrator: manage database access and credentials.

## Oversight
- Review critical vulnerabilities regularly.
- Assign owners and due dates for corrective actions.
- Escalate overdue critical findings.
- Review security metrics and audit evidence periodically.
"""
    with open("governance_oversight.md", "w") as f:
        f.write(content)

    tracker = GovernanceTracker()
    tracker.add_policy(
        "Security Governance Oversight",
        "Defines security roles, responsibilities, escalation, and review"
    )
    tracker.add_control(
        "Executive Security Oversight",
        "Periodic review of risks, metrics, and remediation status"
    )
    print("Created oversight policy and recorded the control")

def verify_controls():
    print("\nControl verification")
    if os.path.exists("patch_status.json"):
        with open("patch_status.json", "r") as f:
            status = json.load(f)
        print("Recorded simulated status:", json.dumps(status, indent=2))
        print("Note: status flags are not proof of technical remediation.")
    else:
        print("No patch_status.json exists; no simulated patch status recorded.")

    print("Monitoring script exists:", os.path.exists("monitoring/security_monitor.sh"))
    print("Oversight document exists:", os.path.exists("governance_oversight.md"))

    tracker = GovernanceTracker()
    print("Governance tracker record counts:")
    print("Policies:", len(tracker.data.get("policies", [])))
    print("Controls:", len(tracker.data.get("controls", [])))
    print("Metrics:", len(tracker.data.get("metrics", [])))

def main():
    parser = argparse.ArgumentParser(description="Implement lab governance controls")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--patch", action="store_true")
    parser.add_argument("--network", action="store_true")
    parser.add_argument("--database", action="store_true")
    parser.add_argument("--monitoring", action="store_true")
    parser.add_argument("--oversight", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.all or args.patch:
        print("Recording simulated patch-management status...")
        record_patch_status("PATCH-001")
        add_control(
            "Automated Patch Management",
            "Track, prioritise, test, and verify security patches",
            "Security Engineer"
        )

    if args.all or args.network:
        record_patch_status("PATCH-003")
        add_control(
            "Network Segmentation",
            "Restrict inter-service connectivity to required traffic",
            "Network Engineer"
        )

    if args.all or args.database:
        record_patch_status("PATCH-002")
        add_control(
            "Database Security",
            "Use strong authentication and least-privilege database access",
            "Database Administrator"
        )

    if args.all or args.monitoring:
        implement_monitoring()
        add_control(
            "Security Monitoring",
            "Record monitoring checks and establish alert review procedures",
            "Security Engineer"
        )

    if args.all or args.oversight:
        implement_oversight()

    if args.all or args.verify:
        verify_controls()

if __name__ == "__main__":
    main()
