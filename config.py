"""
Configuration management for Port Scanner with AI
"""

import os
import json
from pathlib import Path


class Config:
    """Manage configuration settings."""
    
    DEFAULT_CONFIG = {
        "gemini_api_key": "",
        "use_ai_analysis": True,
        "cache_insights": True,
        "default_threads": 50,
        "default_timeout": 2,
        "export_format": "json",
    }
    
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> dict:
        """Load configuration from file or environment."""
        # First, check environment variable
        api_key = os.getenv('GEMINI_API_KEY')
        
        # Then check config file
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    if api_key:
                        config['gemini_api_key'] = api_key
                    return config
            except Exception as e:
                print(f"[!] Error loading config file: {e}")
        
        # Return default with environment API key if found
        config = self.DEFAULT_CONFIG.copy()
        if api_key:
            config['gemini_api_key'] = api_key
        
        return config
    
    def save_config(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            print(f"[+] Configuration saved to {self.config_file}")
        except Exception as e:
            print(f"[!] Error saving config: {e}")
    
    def set_api_key(self, api_key: str):
        """Set Gemini API key."""
        self.config['gemini_api_key'] = api_key
        # Also save to environment for current session
        os.environ['GEMINI_API_KEY'] = api_key
    
    def get_api_key(self) -> str:
        """Get configured API key."""
        return self.config.get('gemini_api_key', '') or os.getenv('GEMINI_API_KEY', '')
    
    def setup_api_key(self):
        """Interactive API key setup."""
        print("\n" + "="*70)
        print("GEMINI API KEY SETUP")
        print("="*70)
        print("\nYou need a Google Gemini API key to use AI features.")
        print("Get your FREE API key from: https://aistudio.google.com/apikey\n")
        
        current_key = self.get_api_key()
        if current_key:
            print(f"Current API Key: {current_key[:10]}...{current_key[-5:]}")
            update = input("Update API key? (y/n): ").strip().lower()
            if update != 'y':
                return True
        
        api_key = input("\nEnter your Gemini API key: ").strip()
        if api_key:
            self.set_api_key(api_key)
            self.save_config()
            print("[+] API key configured successfully!")
            return True
        else:
            print("[!] No API key provided. AI features will be disabled.")
            return False
    
    def __getitem__(self, key: str):
        """Get config value like dict."""
        return self.config.get(key)
    
    def __setitem__(self, key: str, value):
        """Set config value like dict."""
        self.config[key] = value


# Global config instance
_config = None


def get_config() -> Config:
    """Get global config instance."""
    global _config
    if _config is None:
        _config = Config()
    return _config


if __name__ == "__main__":
    config = Config()
    config.setup_api_key()
