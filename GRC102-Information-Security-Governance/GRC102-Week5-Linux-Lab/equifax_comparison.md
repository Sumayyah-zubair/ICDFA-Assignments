# Part 2: Simulated Environment and Equifax Data Breach Comparison

## 1. Introduction

This report compares the security governance weaknesses identified in the simulated Linux lab with lessons from the 2017 Equifax data breach.

## 2. Findings from the Simulated Environment

The vulnerability scan identified three findings:

- **Critical — Apache Struts:** The scanner reported a vulnerable indicator associated with CVE-2017-5638.
- **High — MySQL configuration:** The database accepted the configured root password.
- **Medium — Network segmentation:** The web container could reach the database TCP port.

The governance analysis highlighted potential gaps in incident detection, policy implementation, security architecture, and authentication and access control. These findings show why organisations need effective vulnerability management, strong authentication, restricted network access, and clear accountability for remediation.

The attack scenario script recorded an HTTP 200 response and created an incident log. It did not demonstrate successful exploitation or access to customer data.

## 3. Comparison with the Equifax Data Breach

The 2017 Equifax breach involved exploitation of a known vulnerability in Apache Struts. The incident demonstrated the consequences that can arise when a critical software vulnerability is not remediated effectively.

The simulated lab reflects this risk by using a vulnerable Struts application and reporting a potential critical vulnerability. The database and network checks demonstrate additional security concerns: weak or default credentials and excessive connectivity can increase the impact of a compromised application.

The lab is a simplified educational simulation. It does not reproduce the full Equifax attack, and its results do not establish that a real data breach occurred.

## 4. Governance Lessons

1. **Vulnerability management:** Maintain an inventory of systems, monitor security advisories, prioritise critical vulnerabilities, and verify remediation.
2. **Accountability:** Assign owners and deadlines for patching and track unresolved findings through governance processes.
3. **Access control:** Use strong, unique credentials and least-privilege database accounts.
4. **Network segmentation:** Restrict communication between application and database services to necessary connections.
5. **Incident response:** Maintain monitoring, escalation procedures, evidence collection, and tested response plans.
6. **Assurance and metrics:** Use audits and measurable indicators to confirm that controls operate effectively, rather than relying only on written policies.

## 5. Conclusion

The exercise illustrates how technical weaknesses can become governance risks when remediation, access control, network restrictions, monitoring, and accountability are inadequate. The Equifax breach provides a real-world reminder of the importance of timely vulnerability management. Organisations should combine technical controls with clear policies, responsible owners, measurable remediation targets, and regular assurance.
