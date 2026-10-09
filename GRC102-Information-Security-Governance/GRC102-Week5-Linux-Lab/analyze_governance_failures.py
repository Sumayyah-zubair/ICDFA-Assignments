#!/usr/bin/env python3

import os
import json
import datetime

def load_json(filename):
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found")
        return None
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Could not read {filename}: {e}")
        return None

def analyze_governance_failures():
    failures = []

    reports = sorted(
        f for f in os.listdir(".")
        if f.startswith("vulnerability_report_") and f.endswith(".json")
    )
    vulnerability_report = load_json(reports[-1]) if reports else None
    attack_log = load_json("attack_log.json")
    governance_data = load_json("governance_data.json")
    patch_status = load_json("patch_status.json") or {
        "struts_patched": False,
        "mysql_secured": False,
        "network_segmented": False
    }

    if vulnerability_report:
        for vuln in vulnerability_report.get("vulnerabilities", []):
            if vuln.get("vulnerable", False) and vuln.get("severity") in ["Critical", "High"]:
                failures.append({
                    "category": "Patch Management",
                    "description": f"Unpatched {vuln.get('vulnerability', 'vulnerability')}",
                    "impact": "System may be exposed to exploitation",
                    "recommendation": vuln.get("remediation", "Apply the vendor-recommended fix")
                })

    if attack_log:
        failures.append({
            "category": "Incident Detection",
            "description": "An attack scenario was recorded; successful exploitation was not demonstrated",
            "impact": "Monitoring and alerting effectiveness still needs verification",
            "recommendation": "Implement monitoring, alerting, and incident-response procedures"
        })

    if governance_data:
        policies = governance_data.get("policies", [])
        if any("patch" in p.get("name", "").lower() for p in policies) and not patch_status.get("struts_patched", False):
            failures.append({
                "category": "Policy Implementation",
                "description": "Patch management policy may not be effectively implemented",
                "impact": "Critical vulnerabilities may remain unremediated",
                "recommendation": "Assign ownership, deadlines, and verification for patching"
            })

    if not patch_status.get("network_segmented", False):
        failures.append({
            "category": "Security Architecture",
            "description": "Network segmentation control is not recorded as implemented",
            "impact": "A compromised service could potentially reach other services",
            "recommendation": "Restrict inter-service access using least-privilege network rules"
        })

    if not patch_status.get("mysql_secured", False):
        failures.append({
            "category": "Authentication and Access Control",
            "description": "Database security control is not recorded as implemented",
            "impact": "Weak credentials or excessive privileges could increase risk",
            "recommendation": "Use strong credentials and least-privilege database accounts"
        })

    return failures

def main():
    failures = analyze_governance_failures()
    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "failures": failures,
        "summary": {
            "total_failures": len(failures),
            "categories": {}
        }
    }

    for failure in failures:
        category = failure["category"]
        report["summary"]["categories"][category] = (
            report["summary"]["categories"].get(category, 0) + 1
        )

    filename = f"governance_failure_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Governance failure analysis completed. Report saved to {filename}")
    print(f"Summary: {len(failures)} governance findings identified")
    for category, count in report["summary"]["categories"].items():
        print(f"  {category}: {count}")

if __name__ == "__main__":
    main()
