# Quick Start Guide

## Installation (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Gemini API Key (Free)
Visit: https://aistudio.google.com/apikey
- Sign in with Google account
- Click "Get API Key"
- Copy the key

### Step 3: Set API Key (Windows)
```powershell
# Option A: Set environment variable (temporary - current session only)
$env:GEMINI_API_KEY = "your_key_here"

# Option B: Run setup wizard (recommended - saves to config file)
python setup.py
```

### Step 4: Run the Scanner
```bash
python port_scanner.py
```

Follow the interactive prompts!

---

## First Scan Example

```
Enter target host (IP or hostname): 127.0.0.1

[*] Scan Options:
    1. Scan common ports (recommended for learning)
    2. Scan custom port range

Select scan type (1 or 2): 1

Enter number of threads (default 50): 50

Export results to JSON? (y/n, default n): n

[*] AI Features Available (requires Gemini API key)
Use AI-powered analysis? (y/n, default n): y

[+] AI Analyzer initialized successfully!

[*] Scanning host 127.0.0.1...
[+] Scan completed successfully!

======================================================================
AI FEATURES MENU
======================================================================
1. Get hardening guide for a service
2. Get CVE information for a service
3. Ask a security question
4. Get remediation steps for a vulnerability
5. Back to main menu
```

---

## Troubleshooting

### No API Key error?
```bash
# Option 1: Run setup
python setup.py

# Option 2: Set environment variable
$env:GEMINI_API_KEY = "your_key"

# Option 3: Create config.json manually with:
{
  "gemini_api_key": "your_key_here"
}
```

### Installation fails?
```bash
# Update pip first
python -m pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

### Scan is slow?
- Use common ports mode (option 1) for quick scan
- Reduce port range (1-1000 instead of 1-10000)
- Increase threads (up to 500)

---

## Features at a Glance

✅ Scan open ports
✅ Identify services
✅ AI-powered vulnerability analysis
✅ Get remediation steps
✅ Research CVEs
✅ Get hardening guides
✅ Ask security questions
✅ Export results to JSON

---

## Next Steps

1. **Read full documentation**: `README.md`
2. **Understand the code**: `port_scanner.py`, `ai_analyzer.py`
3. **Practice on localhost**: `127.0.0.1`
4. **Learn from results**: Review AI insights
5. **Extend the tool**: Add more features!

---

## Important Notes

⚠️ **Legal & Ethical Use**
- Only scan systems you own or have permission to test
- Unauthorized scanning may be illegal
- Use for learning and authorized testing only

✅ **Best Practices**
- Start with common ports
- Test on localhost first
- Use AI insights to learn
- Keep your API key private
- Never share your API key

---

## File Descriptions

| File | Purpose |
|------|---------|
| `port_scanner.py` | Main scanning application |
| `ai_analyzer.py` | Gemini AI integration |
| `config.py` | Configuration management |
| `setup.py` | Installation wizard |
| `utilities.py` | Helper functions |
| `requirements.txt` | Python dependencies |
| `config.json` | Your saved API key (auto-created) |

---

## Help & Support

1. Check `README.md` for full documentation
2. Review error messages carefully
3. Test with `127.0.0.1` first
4. Verify API key is correct
5. Check internet connection
6. Read code comments for details

---

**Happy Learning! 🚀**
