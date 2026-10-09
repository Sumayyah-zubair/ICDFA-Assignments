# Part 3 — Implementing Governance Controls

## Objective
Implement and record security governance controls based on lessons from the Equifax data breach scenario.

## Controls Implemented

### 1. Patch Management
Recorded simulated patch status for Apache Struts (PATCH-001). The control represents a process for tracking, prioritising, testing, and verifying security patches.

### 2. Network Segmentation
Recorded simulated status for network segmentation (PATCH-003). The intended control is to restrict communication between services to required traffic.

### 3. Database Security
Recorded simulated status for database security (PATCH-002). The intended control is to enforce strong authentication and least-privilege database access.

### 4. Security Monitoring
Created `monitoring/security_monitor.sh`, a basic script that records the time a monitoring check runs. It is a demonstration and is not yet configured to analyse system logs or generate security alerts.

### 5. Governance Oversight
Created `governance_oversight.md` to document security roles, responsibilities, review of critical vulnerabilities, remediation ownership, escalation of overdue findings, and periodic review of metrics.

## Verification Results
- Governance policies: 5
- Governance controls: 13
- Governance metrics: 3
- Monitoring script exists: Yes
- Oversight document exists: Yes

## Limitations
The patch-status flags are simulated records. They do not confirm that Apache Struts was patched, MySQL was hardened, or network segmentation was technically enforced. The monitoring script records a timestamp but does not yet monitor real system logs.

## Relevance to the Equifax Breach
These controls address governance lessons associated with the Equifax breach by emphasising timely vulnerability remediation, restricted network access, secure database configuration, monitoring, and clear accountability. Effective implementation requires technical verification, documented ownership, deadlines, and regular review rather than relying solely on recorded status.
