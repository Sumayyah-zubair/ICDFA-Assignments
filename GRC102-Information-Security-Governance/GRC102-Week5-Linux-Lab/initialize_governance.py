#!/usr/bin/env python3

from governance_tracker import GovernanceTracker


def main():
    tracker = GovernanceTracker()

    # Add policies
    tracker.add_policy(
        "Patch Management Policy",
        "Ensure security patches are identified, tested, and applied promptly."
    )
    tracker.add_policy(
        "Vulnerability Management Policy",
        "Identify, assess, prioritize, and remediate security vulnerabilities."
    )
    tracker.add_policy(
        "Incident Response Policy",
        "Define procedures for detecting, reporting, and responding to incidents."
    )

    # Add controls
    tracker.add_control(
        "Automated Patch Management",
        "Track and apply approved security patches."
    )
    tracker.add_control(
        "Vulnerability Scanning",
        "Regularly scan systems for known security vulnerabilities."
    )
    tracker.add_control(
        "Network Segmentation",
        "Restrict unnecessary communication between network components."
    )

    # Add risks
    tracker.add_risk(
        "Unpatched Vulnerabilities",
        "High",
        "High",
        "Unpatched software may be exploited by attackers."
    )
    tracker.add_risk(
        "Insufficient Network Segmentation",
        "Medium",
        "High",
        "Unrestricted communication may expose sensitive services."
    )
    tracker.add_risk(
        "Weak Authentication",
        "Medium",
        "Medium",
        "Weak or default credentials may allow unauthorized access."
    )

    # Add incident
    tracker.add_incident(
        "Web Server Compromise",
        "A simulated web server vulnerability was identified during scanning.",
        "Critical"
    )

    # Add metrics
    tracker.add_metric("Patch Compliance", 95, 85)
    tracker.add_metric("Vulnerability Remediation Time", 7, 12)
    tracker.add_metric("Security Incidents", 0, 1)

    # Add audit
    tracker.add_audit(
        "Annual Security Audit",
        "Review security controls, policies, and risk management practices.",
        "Scheduled"
    )

    print("Governance tracker initialized with sample data")


if __name__ == "__main__":
    main()
