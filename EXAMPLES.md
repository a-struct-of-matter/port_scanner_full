# Usage Examples

## Example 1: Basic Localhost Scan

**Scenario**: Learning about your own machine

```bash
python port_scanner.py
```

**Input**:
```
Enter target host: 127.0.0.1
Select scan type: 1 (common ports)
Threads: 50
Export JSON: n
Use AI: y
```

**Output**:
```
[*] Scanning host 127.0.0.1
[+] Port 22: SSH is OPEN
[+] Port 80: HTTP is OPEN

[AI ANALYSIS] SSH
Risk Assessment: MEDIUM
Key Security Concerns:
- Brute force attacks
- Key management issues
...
```

---

## Example 2: Full Network Scan with AI

**Scenario**: Comprehensive security assessment of your network

```bash
python port_scanner.py
```

**Input**:
```
Enter target host: 192.168.1.1
Select scan type: 2 (custom range)
Start port: 1
End port: 10000
Threads: 100
Export JSON: y
Filename: network_scan_2026.json
Use AI: y
```

**Features Used**:
- Full port range scan
- AI analysis for each service
- JSON export for documentation
- AI insights included in report

---

## Example 3: Quick Common Ports Only

**Scenario**: Fast security check without full scan

```bash
python port_scanner.py
```

**Input**:
```
Enter target host: example.com
Select scan type: 1 (common ports)
Threads: 50
Export JSON: n
Use AI: n
```

**Time**: ~5-10 seconds

---

## Example 4: Using AI Features Menu

After scanning, you can interact with AI:

```
AI FEATURES MENU
1. Get hardening guide for a service
2. Get CVE information for a service
3. Ask a security question
4. Get remediation steps for a vulnerability
5. Back to main menu

Select: 1
Enter service: SSH
```

**AI Response**:
```
COMPREHENSIVE HARDENING GUIDE FOR SSH

PRE-REQUISITES:
- SSH installed and running
- Root or sudo access
- Understanding of SSH concepts

SECURITY CONFIGURATION:
1. Disable root login
   PermitRootLogin no
   
2. Disable password auth
   PasswordAuthentication no
   
3. Set SSH port
   Port 2222

4. Limit connection attempts
   MaxAuthTries 3
   MaxStartups 10:30:60
   ...
```

---

## Example 5: CVE Research

```
AI FEATURES MENU
Select: 2
Enter service: MySQL

AI Response:
TOP CVEs FOR MYSQL:

1. CVE-2022-0391
   CVSS Score: 9.8
   Impact: Remote code execution
   Mitigation: Update MySQL to 8.0.28 or later
   
2. CVE-2021-2154
   CVSS Score: 8.4
   Impact: DML privileges required
   Mitigation: Restrict DML privileges
   ...
```

---

## Example 6: Ask Security Questions

```
AI FEATURES MENU
Select: 3
Question: What is the difference between SSH and Telnet?

AI Response:
SSH (Secure Shell) vs Telnet:

SSH:
✓ Encrypted communication
✓ Secure authentication
✓ Public key infrastructure support
✓ Modern standard (RFC 4252)

Telnet:
✗ Unencrypted plaintext
✗ Weak authentication
✗ Deprecated
✗ Security risk

RECOMMENDATION:
Always use SSH over Telnet.
Telnet should be disabled on all systems.
```

---

## Example 7: Remediation Steps

```
AI FEATURES MENU
Select: 4
Service: MySQL
Vulnerability: Default credentials often used

AI Response:
REMEDIATION FOR MYSQL - DEFAULT CREDENTIALS

IMMEDIATE FIX:
1. Change root password immediately
   mysql -u root -p
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'strong_password';
   
2. Remove anonymous users
   DELETE FROM mysql.user WHERE user='';
   
3. Remove remote root login
   DELETE FROM mysql.user WHERE user='root' AND host!='localhost';

CONFIGURATION CHANGES:
1. Edit /etc/mysql/mysql.conf.d/mysqld.cnf
   skip-external-locking
   bind-address = 127.0.0.1

VERIFICATION:
1. Test: mysql -u root -p
2. Check: SELECT user, host FROM mysql.user;
3. Flush privileges: FLUSH PRIVILEGES;

TESTING:
1. Attempt password login
2. Verify remote access is blocked
3. Check error logs
```

---

## Example 8: Web Server Assessment

**Target**: Typical web server (Apache/Nginx)

```bash
python port_scanner.py
```

**Input**:
```
Host: webserver.local
Scan type: 1 (common ports)
Threads: 50
AI: y
```

**Results**:
```
[+] Port 80: HTTP is OPEN
[+] Port 443: HTTPS is OPEN
[+] Port 22: SSH is OPEN

[AI ANALYSIS] HTTP
- Unencrypted traffic risk
- Vulnerable to MITM attacks
- Should redirect to HTTPS
- Run hardening guide for Apache

[AI ANALYSIS] HTTPS
- Check certificate validity
- Verify TLS 1.2+ only
- Test cipher suite strength
```

---

## Example 9: Database Server Scan

**Target**: PostgreSQL server

```bash
python port_scanner.py
```

**Input**:
```
Host: db.internal
Scan type: 2
Start: 5400
End: 5500
Threads: 20
AI: y
```

**Results**:
```
[+] Port 5432: PostgreSQL is OPEN

[AI ANALYSIS] PostgreSQL
Risk: CRITICAL
Concerns:
- Database exposed to network
- Default credentials risk
- SQL injection potential

Immediate Actions:
- Restrict network access
- Implement strong auth
- Regular backup verification
```

---

## Example 10: Environment Variable Setup

**Windows PowerShell**:
```powershell
# Set for current session only
$env:GEMINI_API_KEY = "your_api_key_here"
python port_scanner.py

# Or set permanently via System Properties
[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "your_key", "User")
```

**Windows Command Prompt**:
```cmd
set GEMINI_API_KEY=your_api_key_here
python port_scanner.py
```

**Linux/Mac**:
```bash
export GEMINI_API_KEY="your_api_key_here"
python port_scanner.py

# Or add to ~/.bashrc for persistence
echo 'export GEMINI_API_KEY="your_key"' >> ~/.bashrc
```

---

## Example 11: JSON Export for Automation

```bash
python port_scanner.py
```

**Input**:
```
Host: 192.168.1.0/24
Scan type: 1
Export JSON: y
Filename: network_inventory.json
AI: n (for speed)
```

**Resulting JSON**:
```json
{
  "host": "192.168.1.0/24",
  "scan_time": "2026-02-01T15:30:45.123456",
  "open_ports": {
    "22": "SSH",
    "80": "HTTP",
    "443": "HTTPS"
  },
  "vulnerabilities": {
    "22": {
      "service": "SSH",
      "risks": [
        "Brute force attacks if weak credentials used",
        "SSH key exhaustion attacks possible"
      ]
    }
  }
}
```

**Use Cases**:
- Import into spreadsheet
- Parse with scripts
- Generate reports
- Track changes over time
- Compliance documentation

---

## Example 12: Learning Path

**Day 1**: Understanding Ports
```bash
python port_scanner.py
# Scan: 127.0.0.1, common ports
# Learn about standard ports
```

**Day 2**: Service Identification
```bash
python port_scanner.py
# Scan: 192.168.1.1, common ports
# Identify services using AI
```

**Day 3**: Vulnerability Assessment
```bash
python port_scanner.py
# Scan: 192.168.1.1, full range
# Review AI vulnerability analysis
```

**Day 4**: Remediation
```bash
# Use AI menu to get hardening guides
# Implement recommendations
# Practice on test systems
```

**Day 5**: Advanced Scanning
```bash
python port_scanner.py
# Custom port ranges
# Multiple hosts
# Export and analyze results
```

---

## Tips & Tricks

### Speed Up Scanning
- Use common ports mode (10x faster)
- Increase threads to 200-500
- Reduce port range

### Better AI Insights
- Ask follow-up questions
- Request specific formats
- Ask for step-by-step guides
- Request comparison analysis

### Troubleshooting Scans
- Test with 127.0.0.1 first
- Check network connectivity
- Verify firewall rules
- Increase timeout if needed

### Learning Effectively
- Scan your own systems first
- Review AI explanations carefully
- Practice remediation steps
- Document your findings
- Compare before/after results

---

## Common Scenarios

| Scenario | Scan Type | Threads | AI? | Export? |
|----------|-----------|---------|-----|---------|
| Learning | Common | 50 | Yes | No |
| Quick Check | Common | 100 | No | No |
| Full Audit | Custom | 200 | Yes | Yes |
| Documentation | Custom | 100 | Yes | Yes |
| Lab Testing | Common | 50 | Yes | No |
| Compliance | Custom | 100 | Yes | Yes |

---

**Remember**: Always have permission before scanning any system!
