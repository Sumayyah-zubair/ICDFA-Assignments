#!/usr/bin/env python3

import os
import sys
import json
import datetime
import random
import matplotlib.pyplot as plt
from governance_tracker import GovernanceTracker

def generate_historical_data():
    """Generate historical data for metrics"""
    months = []
    current_month = datetime.datetime.now()

    for i in range(6):
        month = current_month - datetime.timedelta(days=30 * i)
        months.insert(0, month.strftime("%b %Y"))

    patch_compliance = [random.uniform(70, 85) for _ in range(5)]
    patch_compliance.append(100.0)

    vuln_remediation = [random.uniform(10, 15) for _ in range(5)]
    vuln_remediation.append(1.0)

    security_incidents = [random.randint(1, 3) for _ in range(5)]
    security_incidents.append(0)

    monitoring_coverage = [random.uniform(60, 80) for _ in range(5)]
    monitoring_coverage.append(100.0)

    policy_compliance = [random.uniform(75, 90) for _ in range(5)]
    policy_compliance.append(100.0)

    return {
        "months": months,
        "patch_compliance": patch_compliance,
        "vuln_remediation": vuln_remediation,
        "security_incidents": security_incidents,
        "monitoring_coverage": monitoring_coverage,
        "policy_compliance": policy_compliance
    }

def generate_metrics_visualizations(data):
    """Generate visualizations for security governance metrics"""
    months = data["months"]
    os.makedirs("metrics_visualizations", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(months, data["patch_compliance"], marker='o', linestyle='-', color='#3498db')
    plt.axhline(y=95, color='#2ecc71', linestyle='--', label='Target')
    plt.title('Patch Compliance Trend')
    plt.xlabel('Month')
    plt.ylabel('Compliance (%)')
    plt.ylim(0, 105)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("metrics_visualizations/patch_compliance.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(months, data["vuln_remediation"], marker='o', linestyle='-', color='#e74c3c')
    plt.axhline(y=7, color='#2ecc71', linestyle='--', label='Target')
    plt.title('Vulnerability Remediation Time Trend')
    plt.xlabel('Month')
    plt.ylabel('Days to Remediate')
    plt.ylim(0, 20)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("metrics_visualizations/vuln_remediation.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(months, data["security_incidents"], color='#9b59b6')
    plt.axhline(y=0, color='#2ecc71', linestyle='--', label='Target')
    plt.title('Security Incidents Trend')
    plt.xlabel('Month')
    plt.ylabel('Number of Incidents')
    plt.ylim(0, 5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("metrics_visualizations/security_incidents.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(months, data["monitoring_coverage"], marker='o', linestyle='-', color='#f39c12')
    plt.axhline(y=95, color='#2ecc71', linestyle='--', label='Target')
    plt.title('Security Monitoring Coverage Trend')
    plt.xlabel('Month')
    plt.ylabel('Coverage (%)')
    plt.ylim(0, 105)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("metrics_visualizations/monitoring_coverage.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(months, data["policy_compliance"], marker='o', linestyle='-', color='#16a085')
    plt.axhline(y=95, color='#2ecc71', linestyle='--', label='Target')
    plt.title('Policy Compliance Trend')
    plt.xlabel('Month')
    plt.ylabel('Compliance (%)')
    plt.ylim(0, 105)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("metrics_visualizations/policy_compliance.png")
    plt.close()

    return [
        "metrics_visualizations/patch_compliance.png",
        "metrics_visualizations/vuln_remediation.png",
        "metrics_visualizations/security_incidents.png",
        "metrics_visualizations/monitoring_coverage.png",
        "metrics_visualizations/policy_compliance.png"
    ]

def generate_executive_dashboard(data, visualization_files):
    """Generate an executive dashboard for security governance"""
    dashboard_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Security Governance Executive Dashboard</title>
<style>
body {{font-family:Arial,sans-serif;margin:0;padding:20px;background:#f5f5f5;}}
.dashboard {{max-width:1200px;margin:0 auto;}}
.header {{background:#2c3e50;color:white;padding:20px;border-radius:5px 5px 0 0;}}
.content {{display:flex;flex-wrap:wrap;gap:20px;padding:20px;background:white;}}
.card {{background:white;border-radius:5px;box-shadow:0 2px 5px rgba(0,0,0,.1);padding:20px;flex:1 1 300px;}}
.card h2 {{margin-top:0;color:#2c3e50;border-bottom:1px solid #eee;padding-bottom:10px;}}
.metric {{display:flex;justify-content:space-between;margin-bottom:10px;gap:10px;}}
.metric-label,.metric-value {{font-weight:bold;}}
.good {{color:#2ecc71;}} .warning {{color:#f39c12;}} .critical {{color:#e74c3c;}}
.chart {{margin-top:20px;text-align:center;}}
.chart img {{max-width:100%;height:auto;border:1px solid #eee;border-radius:5px;}}
.footer {{text-align:center;margin-top:20px;color:#777;}}
</style>
</head>
<body>
<div class="dashboard">
<div class="header">
<h1>Security Governance Executive Dashboard</h1>
<p>Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
</div>
<div class="content">
<div class="card"><h2>Security Posture Summary</h2>
<div class="metric"><span class="metric-label">Overall Security Posture:</span><span class="metric-value good">Good</span></div>
<div class="metric"><span class="metric-label">Patch Compliance:</span><span class="metric-value good">{data["patch_compliance"][-1]:.1f}%</span></div>
<div class="metric"><span class="metric-label">Vulnerability Remediation Time:</span><span class="metric-value good">{data["vuln_remediation"][-1]:.1f} days</span></div>
<div class="metric"><span class="metric-label">Security Incidents (Current Month):</span><span class="metric-value good">{data["security_incidents"][-1]}</span></div>
<div class="metric"><span class="metric-label">Security Monitoring Coverage:</span><span class="metric-value good">{data["monitoring_coverage"][-1]:.1f}%</span></div>
<div class="metric"><span class="metric-label">Policy Compliance:</span><span class="metric-value good">{data["policy_compliance"][-1]:.1f}%</span></div>
</div>
<div class="card"><h2>Risk Summary</h2>
<div class="metric"><span class="metric-label">Critical Risks:</span><span class="metric-value good">0</span></div>
<div class="metric"><span class="metric-label">High Risks:</span><span class="metric-value good">0</span></div>
<div class="metric"><span class="metric-label">Medium Risks:</span><span class="metric-value warning">2</span></div>
<div class="metric"><span class="metric-label">Low Risks:</span><span class="metric-value good">3</span></div>
<div class="metric"><span class="metric-label">Risk Acceptance Rate:</span><span class="metric-value good">0%</span></div>
<div class="metric"><span class="metric-label">Average Risk Remediation Time:</span><span class="metric-value good">5.2 days</span></div>
</div>
<div class="card"><h2>Compliance Summary</h2>
<div class="metric"><span class="metric-label">Policy Compliance:</span><span class="metric-value good">{data["policy_compliance"][-1]:.1f}%</span></div>
<div class="metric"><span class="metric-label">Control Effectiveness:</span><span class="metric-value good">95%</span></div>
<div class="metric"><span class="metric-label">Audit Findings (Open):</span><span class="metric-value good">0</span></div>
<div class="metric"><span class="metric-label">Regulatory Compliance:</span><span class="metric-value good">100%</span></div>
<div class="metric"><span class="metric-label">Security Training Completion:</span><span class="metric-value good">98%</span></div>
<div class="metric"><span class="metric-label">Third-Party Risk Assessment:</span><span class="metric-value good">100%</span></div>
</div>
</div>
<div class="content">
<div class="card"><h2>Patch Compliance Trend</h2><div class="chart"><img src="{visualization_files[0]}" alt="Patch Compliance Trend"></div></div>
<div class="card"><h2>Vulnerability Remediation Time Trend</h2><div class="chart"><img src="{visualization_files[1]}" alt="Vulnerability Remediation Time Trend"></div></div>
</div>
<div class="content">
<div class="card"><h2>Security Incidents Trend</h2><div class="chart"><img src="{visualization_files[2]}" alt="Security Incidents Trend"></div></div>
<div class="card"><h2>Security Monitoring Coverage Trend</h2><div class="chart"><img src="{visualization_files[3]}" alt="Security Monitoring Coverage Trend"></div></div>
</div>
<div class="content">
<div class="card"><h2>Policy Compliance Trend</h2><div class="chart"><img src="{visualization_files[4]}" alt="Policy Compliance Trend"></div></div>
<div class="card"><h2>Key Recommendations</h2><ol>
<li>Maintain current patch management process to ensure continued compliance</li>
<li>Continue monitoring for new vulnerabilities and address them promptly</li>
<li>Conduct regular security awareness training for all employees</li>
<li>Perform quarterly security assessments to identify new risks</li>
<li>Update security policies and procedures annually</li>
</ol></div>
</div>
<div class="footer"><p>ICDFA GRC102 - Security Governance Dashboard</p></div>
</div>
</body>
</html>
"""
    with open("executive_dashboard.html", "w") as f:
        f.write(dashboard_html)
    return "executive_dashboard.html"

def generate_board_report(data, visualization_files):
    """Generate a board-level security governance report"""
    report_md = f"""# Security Governance Board Report

**Date: {datetime.datetime.now().strftime("%Y-%m-%d")}**

## Executive Summary

This report provides an overview of the organization's security governance posture. The security program has shown significant improvement over the past month, with all key metrics now meeting or exceeding targets.

## Key Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Patch Compliance | {data["patch_compliance"][-1]:.1f}% | 95% | OK |
| Vulnerability Remediation Time | {data["vuln_remediation"][-1]:.1f} days | 7 days | OK |
| Security Incidents | {data["security_incidents"][-1]} | 0 | OK |
| Security Monitoring Coverage | {data["monitoring_coverage"][-1]:.1f}% | 95% | OK |
| Policy Compliance | {data["policy_compliance"][-1]:.1f}% | 95% | OK |

## Risk Summary

The guide's illustrative risk summary lists:
- 0 Critical Risks
- 0 High Risks
- 2 Medium Risks
- 3 Low Risks

These values are examples and must be validated against actual risk records.

## Security Incidents

The sample data sets the current-month incident count to zero. This is illustrative and does not prove that no incidents occurred.

## Compliance Status

The sample report assumes full compliance. Actual compliance must be verified against policies, controls, audit evidence, and applicable requirements.

## Security Program Improvements

1. **Enhanced Patch Management:** Track, test, and verify security patches.
2. **Improved Network Segmentation:** Restrict inter-service communication to required traffic.
3. **Strengthened Database Security:** Apply strong authentication and least-privilege access.
4. **Enhanced Security Monitoring:** Configure and test log monitoring and alerts.
5. **Improved Governance Oversight:** Assign responsibilities and review risks and metrics.

## Recommendations

1. Review security governance performance regularly.
2. Conduct an independent security assessment to validate controls.
3. Improve security awareness and training.
4. Develop third-party risk management.
5. Track security metrics over time and report them to leadership.

## Conclusion

Metrics help management monitor security performance and identify areas requiring corrective action. The illustrative data in this report must not be treated as verified evidence of control effectiveness.
"""
    with open("board_report.md", "w") as f:
        f.write(report_md)
    return "board_report.md"

def main():
    data = generate_historical_data()
    visualization_files = generate_metrics_visualizations(data)
    dashboard_file = generate_executive_dashboard(data, visualization_files)
    board_report_file = generate_board_report(data, visualization_files)

    print("Security governance metrics and reporting generated:")
    print(f"- Executive Dashboard: {dashboard_file}")
    print(f"- Board Report: {board_report_file}")
    print(f"- Visualizations: {', '.join(visualization_files)}")
    print("Note: generated historical metrics are illustrative, not measured production results.")

if __name__ == "__main__":
    main()
