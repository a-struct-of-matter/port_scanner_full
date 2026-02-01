# Port Scanner & Vulnerability Assessment Tool with AI

An advanced educational tool for learning cybersecurity concepts through port scanning and AI-powered vulnerability analysis using Google's Gemini API.

## Features

✅ **Multi-threaded Port Scanning** - Fast parallel scanning using ThreadPoolExecutor  
✅ **Service Identification** - Detects services running on open ports  
✅ **Vulnerability Database** - Suggests potential vulnerabilities for identified services  
✅ **🤖 AI-Powered Analysis** - Google Gemini integration for intelligent vulnerability insights  
✅ **Smart Remediation** - AI-generated step-by-step fix recommendations  
✅ **CVE Intelligence** - Fetch current CVE information for services  
✅ **Hardening Guides** - Comprehensive security hardening recommendations  
✅ **Common Ports Mode** - Quick scan of frequently-used ports  
✅ **Detailed Reports** - Generates comprehensive vulnerability assessments  
✅ **JSON Export** - Export scan results for further analysis  
✅ **Interactive Q&A** - Ask security questions to the AI analyzer  

## Installation

### Quick Start

```bash
# 1. Navigate to project folder
cd port_tester

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run setup wizard (recommended)
python setup.py

# 4. Enter your Gemini API key when prompted
```

### Manual Setup

```bash
# Install google-generativeai
pip install google-generativeai

# Get free API key from https://aistudio.google.com/apikey

# Set environment variable (Windows PowerShell)
$env:GEMINI_API_KEY = "your_api_key_here"

# Or set on Linux/Mac
export GEMINI_API_KEY="your_api_key_here"
```

```bash
git clone <repo>
cd port_tester
python port_scanner.py
```

## Usage

### Standard Mode (No AI)

Simply run the scanner:
```bash
python port_scanner.py
```

Follow the interactive prompts to configure your scan.

### With AI Features

1. Set up your Gemini API key (see Installation section)
2. Run the scanner and select "y" for AI features when prompted
3. After scanning, access the AI Features Menu to:
   - Get hardening guides
   - Fetch CVE information
   - Ask security questions
   - Get remediation steps

### Interactive Menu

```
[*] LEGAL NOTICE: Only scan systems you own or have explicit permission to test.

Enter target host (IP or hostname): 192.168.1.1

[*] Scan Options:
    1. Scan common ports (recommended for learning)
    2. Scan custom port range

Select scan type (1 or 2): 1

Enter number of threads (default 50): 50
Export results to JSON? (y/n, default n): y
Enter JSON filename (default: report.json): scan_results.json

[*] AI Features Available (requires Gemini API key)
Use AI-powered analysis? (y/n, default n): y

[+] AI Analyzer initialized successfully!

[*] Scanning host 192.168.1.1...
[+] Port 22: SSH is OPEN
[+] Port 80: HTTP is OPEN
[+] Port 443: HTTPS is OPEN
```

## API Key Setup

### Get Free Gemini API Key

1. Visit: **https://aistudio.google.com/apikey**
2. Sign in with your Google account
3. Click **"Get API Key"** button
4. Copy the generated key
5. Paste it when the tool prompts you

### Setting API Key

**Option 1: Environment Variable (Recommended)**
```bash
# Windows PowerShell
$env:GEMINI_API_KEY = "your_key_here"

# Windows Command Prompt
set GEMINI_API_KEY=your_key_here

# Linux/Mac
export GEMINI_API_KEY="your_key_here"
```

**Option 2: Config File (First Run)**
The tool will ask you to save it to `config.json`

**Option 3: Direct Entry**
Pass it directly when prompted during tool execution

## Features Details

### 🔍 Port Scanning
- Scans single ports or port ranges
- Multi-threaded for speed (up to 500 threads)
- Service identification
- Progress indicators

### 🤖 AI-Powered Analysis
- **Vulnerability Analysis**: Get AI insights for each open port
- **Security Scoring**: Instant risk assessment
- **Remediation Steps**: Detailed fix instructions
- **CVE Research**: Current CVE information
- **Hardening Guides**: Complete security hardening procedures
- **Q&A**: Ask follow-up security questions

### 📊 Reporting
- Detailed HTML-ready reports
- JSON export for automation
- Port-by-port vulnerability breakdown
- Prioritized recommendations

### 🛡️ Vulnerability Database
Built-in vulnerabilities for 15+ services:
- FTP, SSH, Telnet, SMTP, DNS
- HTTP/HTTPS, POP3, IMAP, SMB
- MySQL, RDP, PostgreSQL, VNC
- And more...

## Command Examples

### Basic Scan
```bash
python port_scanner.py
# Interactive prompts guide you through setup
```

### Quick Common Ports Scan
```bash
python port_scanner.py
# Select option 1 at the scan type prompt
```

### Detailed Port Range
```bash
python port_scanner.py
# Select option 2 for custom range (e.g., 1-5000)
```

### With AI Analysis
```bash
python port_scanner.py
# Choose "y" for AI features when prompted
# Access AI menu after scan completes
```

## AI Features Menu

After scanning, you can access AI features:

```
======================================================================
AI FEATURES MENU
======================================================================
1. Get hardening guide for a service
2. Get CVE information for a service
3. Ask a security question
4. Get remediation steps for a vulnerability
5. Back to main menu
```

## Sample AI Outputs

### Vulnerability Analysis
```
[AI ANALYSIS] SSH
----------------------------------------------------------------------
Risk Assessment: MEDIUM
Key Security Concerns:
- Brute force attacks are common against SSH
- Weak authentication methods can be exploited
- SSH version disclosure may leak information

Immediate Actions:
- Disable password authentication, use keys only
- Change default port from 22
- Implement rate limiting

Long-term Hardening:
- Use SSH keys with strong passphrases
- Implement multi-factor authentication
- Regular security updates
```

### Remediation Steps
```
REMEDIATION FOR: SSH - Brute Force Attacks

Immediate Fix:
1. Disable password authentication in /etc/ssh/sshd_config
   PasswordAuthentication no
2. Restart SSH service: systemctl restart sshd

Configuration Changes:
1. Set MaxAuthTries to 3
2. Set LoginGraceTime to 30 seconds
3. Enable PubkeyAuthentication

Verification:
- Test SSH key login works
- Confirm password login is disabled
- Check logs for failed attempts
```

## Educational Value

Learn:
- Network programming with Python sockets
- Multi-threading and async programming
- Service enumeration and fingerprinting
- Vulnerability assessment concepts
- AI integration in security tools
- Security best practices
- Prompt engineering for AI
- JSON parsing and data export
- Configuration management
- Error handling and resilience

## Security Notes

⚠️ **Legal and Ethical Use ONLY**

1. **Only scan systems you own or have explicit written permission to test**
2. Unauthorized port scanning may be illegal in your jurisdiction
3. Responsible disclosure of vulnerabilities
4. Educational purposes and authorized penetration testing only
5. Comply with all applicable laws and regulations

### Responsible Use Guidelines

- ✅ Scan your own home network
- ✅ Scan test/lab environments
- ✅ Test with explicit written permission
- ✅ Report vulnerabilities responsibly
- ❌ Don't scan systems you don't own
- ❌ Don't use for malicious purposes
- ❌ Don't exceed authorized scope

## Requirements

### System Requirements
- Python 3.6 or higher
- Internet connection (for Gemini API)
- Gemini API key (free from Google)

### Python Packages
- `google-generativeai` - AI analysis engine

### Standard Library (built-in)
- `socket` - Network programming
- `threading/concurrent.futures` - Multi-threading
- `json` - Data export
- `datetime` - Timestamps
- `sys` - System operations

## Troubleshooting

### API Key Issues
```
Error: "Gemini API key not found"
Solution: 
1. Get free key from https://aistudio.google.com/apikey
2. Run setup.py to configure
3. Set GEMINI_API_KEY environment variable
```

### Network Timeouts
```
Error: "Could not connect to host"
Solution:
- Check if host is reachable
- Verify network connectivity
- Try reducing thread count (-t 10)
```

### Slow Scans
```
Solution:
- Increase thread count (default 50, max 500)
- Reduce port range or use common ports mode (-c)
- Check your network bandwidth
```

### AI Features Not Working
```
Error: "AI analyzer not available"
Solution:
- Install google-generativeai: pip install google-generativeai
- Check API key is set correctly
- Verify internet connectivity
- Check API quota at https://aistudio.google.com/app/apiDashboard
```

## Project Structure

```
port_tester/
├── port_scanner.py      # Main scanning tool
├── ai_analyzer.py       # Gemini AI integration
├── config.py            # Configuration management
├── utilities.py         # Utility functions
├── setup.py            # Setup wizard
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Files Documentation

### port_scanner.py
Main application with:
- `PortScanner` class - Core scanning logic
- Port and service detection
- Vulnerability database
- Report generation
- Interactive UI

### ai_analyzer.py
AI integration with:
- `GeminiAnalyzer` class - Gemini API wrapper
- `AIInsightCache` - Result caching
- Vulnerability analysis
- Remediation generation
- CVE research

### config.py
Configuration system:
- API key management
- Config file handling
- Environment variable support
- Interactive setup

### utilities.py
Helper functions:
- Banner grabbing
- Certificate extraction
- Port descriptions
- Security recommendations

### setup.py
Installation wizard:
- Dependency installation
- API key setup
- System verification

## Future Enhancements

- [ ] Web-based GUI interface
- [ ] Real-time threat intelligence feeds
- [ ] Custom exploit database
- [ ] Automated remediation
- [ ] Multi-threaded AI requests
- [ ] Report scheduling
- [ ] Shodan integration
- [ ] Nessus/OpenVAS integration
- [ ] Docker containerization
- [ ] Database logging
- [ ] Advanced filtering
- [ ] Export to multiple formats (PDF, HTML, etc.)

## Learning Path

1. **Week 1**: Basic port scanning
2. **Week 2**: Service identification
3. **Week 3**: Vulnerability assessment
4. **Week 4**: AI-powered analysis
5. **Week 5**: Remediation planning
6. **Week 6**: Report writing and communication

## Resources

- **Google Gemini API**: https://aistudio.google.com
- **Python Sockets**: https://docs.python.org/3/library/socket.html
- **Threading**: https://docs.python.org/3/library/threading.html
- **OWASP**: https://owasp.org/
- **CVSS Scoring**: https://www.first.org/cvss/
- **Port Numbers**: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
- **CIS Controls**: https://www.cisecurity.org/
- **NIST Framework**: https://www.nist.gov/cyberframework

## License

Educational Use Only - Use responsibly and legally.

## Disclaimer

This tool is provided for educational and authorized security testing purposes only. The authors are not responsible for misuse or damage caused by this tool. Always obtain proper authorization before testing any system. Comply with all applicable laws and regulations.

## Support

For issues or questions:
1. Check README.md (this file)
2. Review comments in the code
3. Check the setup.py for installation help
4. Verify API key configuration
5. Test with localhost first

## Contributing

To extend this tool:
1. Add more services to `VULNERABILITIES` dictionary
2. Implement new AI analysis methods
3. Add banner grabbing capabilities
4. Create custom reports
5. Add logging functionality

## Version History

### v1.0
- Initial release
- Basic port scanning
- Service identification
- Vulnerability database
- Interactive UI

### v1.1
- Added Google Gemini AI integration
- AI-powered vulnerability analysis
- Remediation recommendations
- CVE research
- Hardening guides
- Interactive AI menu
- Configuration management
- Setup wizard

---

**Last Updated**: February 2026
**Status**: Educational Release
**Compatibility**: Python 3.6+
