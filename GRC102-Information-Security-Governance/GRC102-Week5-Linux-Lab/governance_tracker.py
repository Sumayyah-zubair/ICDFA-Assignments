#!/usr/bin/env python3

import json
import os
import argparse


class GovernanceTracker:
    def __init__(self, data_file="governance_data.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                pass

        return {
            "policies": [],
            "controls": [],
            "risks": [],
            "incidents": [],
            "metrics": [],
            "audits": []
        }

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

    def add_policy(self, name, description):
        self.data["policies"].append({
            "name": name,
            "description": description
        })
        self.save_data()
        print(f"Policy added: {name}")

    def add_control(self, name, description):
        self.data["controls"].append({
            "name": name,
            "description": description
        })
        self.save_data()
        print(f"Control added: {name}")

    def add_risk(self, name, likelihood, impact, description):
        likelihood_values = {"Low": 1, "Medium": 2, "High": 3}
        impact_values = {"Low": 1, "Medium": 2, "High": 3}

        if likelihood not in likelihood_values or impact not in impact_values:
            print("Likelihood and impact must be Low, Medium, or High.")
            return

        score = likelihood_values[likelihood] * impact_values[impact]

        if score >= 6:
            risk_level = "High"
        elif score >= 3:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        self.data["risks"].append({
            "name": name,
            "likelihood": likelihood,
            "impact": impact,
            "score": score,
            "risk_level": risk_level,
            "description": description
        })
        self.save_data()
        print(f"Risk added: {name} ({risk_level})")

    def add_incident(self, name, description, severity):
        self.data["incidents"].append({
            "name": name,
            "description": description,
            "severity": severity
        })
        self.save_data()
        print(f"Incident added: {name}")

    def add_metric(self, name, target, actual):
        self.data["metrics"].append({
            "name": name,
            "target": target,
            "actual": actual
        })
        self.save_data()
        print(f"Metric added: {name}")

    def add_audit(self, name, description, status):
        self.data["audits"].append({
            "name": name,
            "description": description,
            "status": status
        })
        self.save_data()
        print(f"Audit added: {name}")

    def list_items(self, category):
        items = self.data.get(category, [])
        print(f"\n{category.title()}:")
        if not items:
            print("No records found.")
            return

        print(json.dumps(items, indent=2))

    def list_policies(self):
        self.list_items("policies")

    def list_controls(self):
        self.list_items("controls")

    def list_risks(self):
        self.list_items("risks")

    def list_incidents(self):
        self.list_items("incidents")

    def list_metrics(self):
        self.list_items("metrics")

    def list_audits(self):
        self.list_items("audits")

    def generate_dashboard(self):
        print("\n=== Governance Dashboard ===")
        print(f"Policies: {len(self.data['policies'])}")
        print(f"Controls: {len(self.data['controls'])}")
        print(f"Risks: {len(self.data['risks'])}")
        print(f"Incidents: {len(self.data['incidents'])}")
        print(f"Metrics: {len(self.data['metrics'])}")
        print(f"Audits: {len(self.data['audits'])}")

        print("\n=== Metrics ===")
        for metric in self.data["metrics"]:
            print(
                f"{metric['name']}: "
                f"Target={metric['target']}, "
                f"Actual={metric['actual']}"
            )


def main():
    parser = argparse.ArgumentParser(
        description="Security governance tracker"
    )

    parser.add_argument("--add-policy", nargs=2, metavar=("NAME", "DESCRIPTION"))
    parser.add_argument("--add-control", nargs=2, metavar=("NAME", "DESCRIPTION"))
    parser.add_argument(
        "--add-risk",
        nargs=4,
        metavar=("NAME", "LIKELIHOOD", "IMPACT", "DESCRIPTION")
    )
    parser.add_argument(
        "--add-incident",
        nargs=3,
        metavar=("NAME", "DESCRIPTION", "SEVERITY")
    )
    parser.add_argument(
        "--add-metric",
        nargs=3,
        metavar=("NAME", "TARGET", "ACTUAL")
    )
    parser.add_argument(
        "--add-audit",
        nargs=3,
        metavar=("NAME", "DESCRIPTION", "STATUS")
    )

    parser.add_argument("--list-policies", action="store_true")
    parser.add_argument("--list-controls", action="store_true")
    parser.add_argument("--list-risks", action="store_true")
    parser.add_argument("--list-incidents", action="store_true")
    parser.add_argument("--list-metrics", action="store_true")
    parser.add_argument("--list-audits", action="store_true")
    parser.add_argument("--dashboard", action="store_true")

    args = parser.parse_args()
    tracker = GovernanceTracker()

    if args.add_policy:
        tracker.add_policy(*args.add_policy)
    elif args.add_control:
        tracker.add_control(*args.add_control)
    elif args.add_risk:
        tracker.add_risk(*args.add_risk)
    elif args.add_incident:
        tracker.add_incident(*args.add_incident)
    elif args.add_metric:
        tracker.add_metric(*args.add_metric)
    elif args.add_audit:
        tracker.add_audit(*args.add_audit)
    elif args.list_policies:
        tracker.list_policies()
    elif args.list_controls:
        tracker.list_controls()
    elif args.list_risks:
        tracker.list_risks()
    elif args.list_incidents:
        tracker.list_incidents()
    elif args.list_metrics:
        tracker.list_metrics()
    elif args.list_audits:
        tracker.list_audits()
    elif args.dashboard:
        tracker.generate_dashboard()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
