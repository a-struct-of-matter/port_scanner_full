"""
Setup and installation guide for Port Scanner with AI
"""

import subprocess
import sys
import os


def install_dependencies():
    """Install required packages."""
    print("\n" + "="*70)
    print("INSTALLING DEPENDENCIES")
    print("="*70)
    
    try:
        print("[*] Installing google-generativeai...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("[+] Dependencies installed successfully!")
        return True
    except Exception as e:
        print(f"[!] Error installing dependencies: {e}")
        return False


def setup_api_key():
    """Setup Gemini API key."""
    print("\n" + "="*70)
    print("GEMINI API KEY SETUP")
    print("="*70)
    print("\nYou need a free Google Gemini API key for AI features.")
    print("Steps:")
    print("1. Visit: https://aistudio.google.com/apikey")
    print("2. Click 'Get API Key'")
    print("3. Copy your API key")
    print("\nYou can set it in three ways:")
    print("  a) Environment variable: set GEMINI_API_KEY=your_key")
    print("  b) Save to config.json (will be done on first run)")
    print("  c) Pass directly when running the tool")
    
    choice = input("\nDo you want to save your API key now? (y/n): ").strip().lower()
    if choice == 'y':
        try:
            from config import Config
            config = Config()
            config.setup_api_key()
        except Exception as e:
            print(f"[!] Error: {e}")
            return False
    
    return True


def verify_installation():
    """Verify all components are working."""
    print("\n" + "="*70)
    print("VERIFYING INSTALLATION")
    print("="*70)
    
    checks = []
    
    # Check Python version
    print("[*] Checking Python version...", end=" ")
    if sys.version_info >= (3, 6):
        print("✓")
        checks.append(True)
    else:
        print("✗ (Need Python 3.6+)")
        checks.append(False)
    
    # Check socket module
    print("[*] Checking socket module...", end=" ")
    try:
        import socket
        print("✓")
        checks.append(True)
    except:
        print("✗")
        checks.append(False)
    
    # Check google-generativeai
    print("[*] Checking google-generativeai...", end=" ")
    try:
        import google.generativeai as genai
        print("✓")
        checks.append(True)
    except:
        print("✗")
        checks.append(False)
    
    # Check config module
    print("[*] Checking config module...", end=" ")
    try:
        from config import Config
        print("✓")
        checks.append(True)
    except:
        print("✗")
        checks.append(False)
    
    # Check port_scanner module
    print("[*] Checking port_scanner module...", end=" ")
    try:
        from port_scanner import PortScanner
        print("✓")
        checks.append(True)
    except:
        print("✗")
        checks.append(False)
    
    if all(checks):
        print("\n[+] All checks passed! Ready to use.")
        return True
    else:
        print("\n[!] Some checks failed. Please review the errors above.")
        return False


def main():
    """Run setup wizard."""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Port Scanner Setup Wizard                              ║
    ║   With AI-Powered Vulnerability Analysis                 ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Install dependencies
    if not install_dependencies():
        print("\n[!] Setup failed at dependency installation.")
        return False
    
    # Step 2: Setup API key
    if not setup_api_key():
        print("\n[*] API key setup skipped. AI features will be disabled.")
    
    # Step 3: Verify installation
    if not verify_installation():
        print("\n[!] Setup incomplete. Please fix the errors above.")
        return False
    
    print("\n" + "="*70)
    print("SETUP COMPLETE!")
    print("="*70)
    print("\nTo start scanning, run:")
    print("  python port_scanner.py")
    print("\nFor more info, see README.md")
    print("="*70 + "\n")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
