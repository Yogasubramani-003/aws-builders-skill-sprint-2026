#!/usr/bin/env python3
"""
Verification Script for Builders Skill Sprint Challenges
This script checks if all prerequisites are properly installed and configured.
"""

import sys
import subprocess
from pathlib import Path

def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version is compatible")
        return True
    else:
        print("❌ Python 3.8 or higher is required")
        return False

def check_package(package_name, import_name=None):
    """Check if a Python package is installed."""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"✅ {package_name} is installed")
        return True
    except ImportError:
        print(f"❌ {package_name} is NOT installed")
        print(f"   Install with: pip install {package_name}")
        return False

def check_aws_credentials():
    """Check if AWS credentials are configured."""
    print_header("Checking AWS Configuration")
    try:
        import boto3
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print(f"✅ AWS credentials configured")
        print(f"   Account: {identity['Account']}")
        print(f"   User/Role: {identity['Arn']}")
        return True
    except Exception as e:
        print(f"❌ AWS credentials not configured or invalid")
        print(f"   Error: {str(e)}")
        print(f"   Run: aws configure")
        return False

def check_ollama():
    """Check if Ollama is installed and running."""
    print_header("Checking Ollama (for Challenge 1)")
    
    # Check if ollama command exists
    try:
        result = subprocess.run(['ollama', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            print(f"✅ Ollama is installed: {result.stdout.strip()}")
        else:
            print("❌ Ollama command failed")
            return False
    except FileNotFoundError:
        print("❌ Ollama is NOT installed")
        print("   Download from: https://ollama.ai")
        return False
    except Exception as e:
        print(f"⚠️  Could not verify Ollama: {str(e)}")
        return False
    
    # Check if Ollama server is running
    try:
        import requests
        response = requests.get('http://localhost:11434', timeout=2)
        print("✅ Ollama server is running")
        return True
    except:
        print("⚠️  Ollama server is NOT running")
        print("   Start with: ollama serve")
        return False

def check_ollama_model():
    """Check if required Ollama model is available."""
    try:
        result = subprocess.run(['ollama', 'list'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if 'llama3.2:3b' in result.stdout:
            print("✅ llama3.2:3b model is available")
            return True
        else:
            print("⚠️  llama3.2:3b model not found")
            print("   Pull with: ollama pull llama3.2:3b")
            return False
    except:
        return False

def check_file_structure():
    """Check if all challenge files exist."""
    print_header("Checking File Structure")
    
    base_path = Path(__file__).parent / "April-2026"
    challenges = [
        "challenge-1-first-agent",
        "challenge-2-tools",
        "challenge-3-memory",
        "challenge-4-full-agent",
        "challenge-5-innovate-mcp-chatbot"
    ]
    
    all_exist = True
    for challenge in challenges:
        challenge_path = base_path / challenge / "starter.py"
        if challenge_path.exists():
            print(f"✅ {challenge}/starter.py exists")
        else:
            print(f"❌ {challenge}/starter.py NOT found")
            all_exist = False
    
    return all_exist

def main():
    """Run all verification checks."""
    print("\n" + "🚀" * 30)
    print("  Builders Skill Sprint Challenges - Setup Verification")
    print("🚀" * 30)
    
    results = []
    
    # Check Python version
    results.append(("Python Version", check_python_version()))
    
    # Check required packages
    print_header("Checking Python Packages")
    results.append(("strands", check_package("strands-agents", "strands")))
    results.append(("strands-tools", check_package("strands-tools", "strands_tools")))
    results.append(("boto3", check_package("boto3")))
    results.append(("faiss-cpu", check_package("faiss-cpu", "faiss")))
    results.append(("requests", check_package("requests")))
    
    # Check AWS configuration
    results.append(("AWS Credentials", check_aws_credentials()))
    
    # Check Ollama
    results.append(("Ollama", check_ollama()))
    results.append(("Ollama Model", check_ollama_model()))
    
    # Check file structure
    results.append(("File Structure", check_file_structure()))
    
    # Summary
    print_header("Verification Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nPassed: {passed}/{total} checks")
    
    if passed == total:
        print("\n🎉 All checks passed! You're ready to run the challenges!")
        print("\nNext steps:")
        print("  1. cd April-2026/challenge-1-first-agent")
        print("  2. python starter.py")
    else:
        print("\n⚠️  Some checks failed. Please install missing dependencies.")
        print("\nQuick fix:")
        print("  pip install -r requirements.txt")
        print("  aws configure")
        print("  ollama serve  # In a separate terminal")
    
    print("\n" + "=" * 60)
    print("For detailed setup instructions, see SETUP_AND_RUN.md")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
