#!/usr/bin/env python3
"""
GenLayer DevKit - Easy Setup Script
====================================

Run this to set up DevKit in one command.
"""

import os
import sys
import subprocess
import platform

def print_banner():
    banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║            🛠️  GenLayer DevKit Setup 🛠️                  ║
║                                                           ║
║          Developer Tools for GenLayer Contracts          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
    print(banner)

def check_python():
    """Check Python version"""
    print("✓ Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher required!")
        print(f"   Current version: {version.major}.{version.minor}")
        return False
    
    print(f"  Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def install_dependencies():
    """Install required packages"""
    print("\n✓ Installing dependencies...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "click", "colorama", "--break-system-packages", "-q"
        ])
        print("  Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        # Try without --break-system-packages
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                "click", "colorama", "-q"
            ])
            print("  Dependencies installed successfully")
            return True
        except:
            print("❌ Failed to install dependencies")
            print("  Try manually: pip install click colorama")
            return False

def make_executable():
    """Make devkit executable"""
    print("\n✓ Setting up executable...")
    
    devkit_file = "genlayer_devkit.py"
    
    if not os.path.exists(devkit_file):
        print(f"❌ {devkit_file} not found!")
        return False
    
    # Make executable on Unix
    if platform.system() != "Windows":
        try:
            os.chmod(devkit_file, 0o755)
            print(f"  {devkit_file} is now executable")
        except Exception as e:
            print(f"⚠️  Could not make executable: {e}")
    
    return True

def create_alias():
    """Create command alias"""
    print("\n✓ Setting up alias...")
    
    system = platform.system()
    devkit_path = os.path.abspath("genlayer_devkit.py")
    
    if system == "Windows":
        # PowerShell alias
        print("""
  Windows PowerShell alias:
  
  Add this to your PowerShell profile:
  
  function genlayer { python "{}" $args }
  
  Or run directly:
  python genlayer_devkit.py <command>
        """.format(devkit_path))
    else:
        # Unix alias
        shell = os.environ.get('SHELL', '')
        
        if 'bash' in shell:
            rc_file = os.path.expanduser('~/.bashrc')
        elif 'zsh' in shell:
            rc_file = os.path.expanduser('~/.zshrc')
        else:
            rc_file = None
        
        if rc_file:
            alias_line = f'\nalias genlayer="python3 {devkit_path}"\n'
            
            print(f"""
  Add this to your {rc_file}:
  
  alias genlayer="python3 {devkit_path}"
  
  Or run: echo '{alias_line}' >> {rc_file}
            """)
        else:
            print(f"""
  Create an alias in your shell:
  
  alias genlayer="python3 {devkit_path}"
            """)
    
    return True

def test_installation():
    """Test if installation works"""
    print("\n✓ Testing installation...")
    
    try:
        result = subprocess.run(
            [sys.executable, "genlayer_devkit.py", "--version"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("  DevKit is working!")
            return True
        else:
            print("⚠️  DevKit test failed")
            return False
    except Exception as e:
        print(f"⚠️  Test error: {e}")
        return False

def print_next_steps():
    """Show next steps"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                    ✨ Setup Complete! ✨                  ║
╚═══════════════════════════════════════════════════════════╝

📚 Quick Start:

  # Test the CLI
  python genlayer_devkit.py --help
  
  # Create your first project
  python genlayer_devkit.py init my-awesome-project
  cd my-awesome-project
  
  # Generate a contract
  python ../genlayer_devkit.py generate --type oracle --name PriceOracle
  
  # Test it
  python ../genlayer_devkit.py test contracts/PriceOracle.py

📖 Documentation:
  - Read DEVKIT_README.md for full guide
  - Check DEVKIT_INSTALL.md for detailed setup
  - See examples/ for contract templates

🚀 Happy Building!
    """)

def main():
    """Main setup function"""
    print_banner()
    
    # Run setup steps
    steps = [
        ("Checking Python", check_python),
        ("Installing dependencies", install_dependencies),
        ("Making executable", make_executable),
        ("Creating alias", create_alias),
        ("Testing installation", test_installation)
    ]
    
    success = True
    for step_name, step_func in steps:
        if not step_func():
            success = False
            print(f"\n⚠️  Setup incomplete: {step_name} failed")
            break
    
    if success:
        print_next_steps()
    else:
        print("""
╔═══════════════════════════════════════════════════════════╗
║              ⚠️  Setup encountered issues  ⚠️             ║
╚═══════════════════════════════════════════════════════════╝

You can still use DevKit by running:
  python genlayer_devkit.py <command>

Check DEVKIT_INSTALL.md for troubleshooting.
        """)

if __name__ == "__main__":
    main()
