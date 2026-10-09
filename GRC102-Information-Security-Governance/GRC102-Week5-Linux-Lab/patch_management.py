#!/usr/bin/env python3

import json
import os
import argparse


PATCHES = [
    {
        "id": "PATCH-001",
        "name": "Apache Struts2 S2-045 Patch",
        "cve": "CVE-2017-5638",
        "severity": "Critical",
        "target": "web_server",
        "status": "Available"
    },
    {
        "id": "PATCH-002",
        "name": "MySQL Security Configuration",
        "cve": "N/A",
        "severity": "High",
        "target": "database_server",
        "status": "Available"
    },
    {
        "id": "PATCH-003",
        "name": "Network Segmentation Rules",
        "cve": "N/A",
        "severity": "Medium",
        "target": "all",
        "status": "Available"
    }
]


def apply_patch(patch_id):
    """Simulate applying a governance patch."""
    patch = next(
        (item for item in PATCHES if item["id"] == patch_id),
        None
    )

    if patch is None:
        print(f"Patch {patch_id} not found.")
        return

    print(f"Applying {patch['id']}: {patch['name']}")
    print(f"Target: {patch['target']}")
    print(f"Severity: {patch['severity']}")

    status = {
        "struts_patched": False,
        "mysql_secured": False,
        "network_segmented": False
    }

    if os.path.exists("patch_status.json"):
        try:
            with open("patch_status.json", "r", encoding="utf-8") as file:
                status.update(json.load(file))
        except (json.JSONDecodeError, OSError):
            pass

    if patch_id == "PATCH-001":
        status["struts_patched"] = True
    elif patch_id == "PATCH-002":
        status["mysql_secured"] = True
    elif patch_id == "PATCH-003":
        status["network_segmented"] = True

    with open("patch_status.json", "w", encoding="utf-8") as file:
        json.dump(status, file, indent=2)

    print("Patch simulation completed.")
    print("Status saved to patch_status.json")


def list_patches():
    """List available patches."""
    for patch in PATCHES:
        print(
            f"{patch['id']} | {patch['name']} | "
            f"{patch['severity']} | {patch['target']} | "
            f"{patch['status']}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Security governance patch management simulator"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available patches"
    )
    parser.add_argument(
        "--apply",
        metavar="PATCH_ID",
        help="Simulate applying a patch by ID"
    )

    args = parser.parse_args()

    if args.list:
        list_patches()
    elif args.apply:
        apply_patch(args.apply)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
