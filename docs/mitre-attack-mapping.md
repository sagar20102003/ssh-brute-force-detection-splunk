```markdown
# MITRE ATT&CK Framework Mapping

This project demonstrates real-world adversary techniques mapped to the MITRE ATT&CK framework.

## Techniques Used

### Credential Access (TA0006)

| Technique | ID | Description | Implementation |
|-----------|-----|-------------|----------------|
| Password Guessing | T1110.001 | Brute force password guessing | Hydra attacks against SSH |
| Password Spraying | T1110.003 | Single password against multiple accounts | Hydra with -L option |

### Lateral Movement (TA0008)

| Technique | ID | Description | Implementation |
|-----------|-----|-------------|----------------|
| SSH | T1021.004 | Using SSH for lateral movement | Successful SSH login after brute force |

## Detection Coverage

| Detection Method | MITRE Technique Detected | Alert Type |
|------------------|--------------------------|------------|
| 5+ failures in 5 minutes | T1110.001 | Brute Force Alert |
| Failures then success | T1021.004 | Successful Breach Alert |

## Data Sources Used
- **Linux Audit Logs**: `/var/log/auth.log`
- **Authentication Logs**: SSH authentication events

## Mitigation Recommendations
1. Account Lockout Policy
2. Rate Limiting with fail2ban
3. Strong Password Policy
4. Multi-Factor Authentication