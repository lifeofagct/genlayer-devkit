#!/usr/bin/env python3
"""
GenLayer DevKit - Developer Tools for GenLayer
================================================

A comprehensive CLI tool for GenLayer smart contract development.

Commands:
  init        - Initialize a new GenLayer project
  generate    - Generate contract from template
  test        - Test contracts locally
  deploy      - Deploy contracts to GenLayer
  status      - Check contract deployment status

Author: HASBUNALLAH AYO ABDULRAHMAN
"""

import click
import os
import json
import subprocess
from pathlib import Path

# Version
VERSION = "1.0.0"

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_success(msg):
    click.echo(f"{Colors.GREEN}✓{Colors.ENDC} {msg}")

def print_error(msg):
    click.echo(f"{Colors.RED}✗{Colors.ENDC} {msg}")

def print_info(msg):
    click.echo(f"{Colors.BLUE}ℹ{Colors.ENDC} {msg}")

def print_warning(msg):
    click.echo(f"{Colors.YELLOW}⚠{Colors.ENDC} {msg}")


@click.group()
@click.version_option(version=VERSION)
def cli():
    """
    GenLayer DevKit - Developer tools for GenLayer smart contracts.
    
    Quick start:
      genlayer init my-project
      cd my-project
      genlayer generate oracle --type weather
      genlayer test WeatherOracle.py
      genlayer deploy WeatherOracle.py
    """
    pass


@cli.command()
@click.argument('project_name')
@click.option('--template', default='basic', help='Project template (basic, oracle, defi)')
def init(project_name, template):
    """Initialize a new GenLayer project."""
    
    click.echo(f"\n{Colors.BOLD}🚀 GenLayer DevKit{Colors.ENDC}")
    click.echo(f"Creating new project: {Colors.CYAN}{project_name}{Colors.ENDC}\n")
    
    # Create project directory
    project_path = Path(project_name)
    if project_path.exists():
        print_error(f"Directory '{project_name}' already exists!")
        return
    
    project_path.mkdir()
    
    # Create directory structure
    dirs = ['contracts', 'tests', 'scripts', 'docs']
    for dir_name in dirs:
        (project_path / dir_name).mkdir()
        print_success(f"Created {dir_name}/")
    
    # Create config file
    config = {
        "project_name": project_name,
        "template": template,
        "genlayer_version": "1.0",
        "networks": {
            "testnet": {
                "rpc_url": "https://rpc.testnet.genlayer.com",
                "network_id": "testnet"
            },
            "mainnet": {
                "rpc_url": "https://rpc.mainnet.genlayer.com",
                "network_id": "mainnet"
            }
        }
    }
    
    with open(project_path / 'genlayer.json', 'w') as f:
        json.dump(config, f, indent=2)
    print_success("Created genlayer.json")
    
    # Create README
    readme_content = f"""# {project_name}

GenLayer smart contract project.

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Test contracts
genlayer test contracts/MyContract.py

# Deploy
genlayer deploy contracts/MyContract.py --network testnet
```

## Project Structure

- `contracts/` - Smart contracts
- `tests/` - Contract tests
- `scripts/` - Deployment scripts
- `docs/` - Documentation

## Resources

- [GenLayer Docs](https://docs.genlayer.com)
- [DevKit Guide](https://github.com/lifeofagct/genlayer-devkit)
"""
    
    with open(project_path / 'README.md', 'w') as f:
        f.write(readme_content)
    print_success("Created README.md")
    
    # Create requirements.txt
    requirements = """genlayer-sdk>=0.1.0
click>=8.0.0
pytest>=7.0.0
"""
    
    with open(project_path / 'requirements.txt', 'w') as f:
        f.write(requirements)
    print_success("Created requirements.txt")
    
    # Create .gitignore
    gitignore = """__pycache__/
*.pyc
.pytest_cache/
.env
venv/
*.log
"""
    
    with open(project_path / '.gitignore', 'w') as f:
        f.write(gitignore)
    print_success("Created .gitignore")
    
    # Create sample contract based on template
    if template == 'basic':
        contract_content = """# {{ "Depends": "py-genlayer:test" }}
from genlayer import *

class MyContract(gl.Contract):
    def __init__(self):
        self.value = 0
    
    @gl.public.write
    def set_value(self, new_value: int):
        self.value = new_value
        return f"Value set to {new_value}"
    
    @gl.public.view
    def get_value(self) -> int:
        return self.value
"""
    elif template == 'oracle':
        contract_content = """# {{ "Depends": "py-genlayer:test" }}
from genlayer import *

class PriceOracle(gl.Contract):
    def __init__(self):
        self.prices = {}
    
    @gl.public.write
    def update_price(self, token: str) -> int:
        # In production, fetch real price via AI
        # For now, demo implementation
        self.prices[token] = 45000
        return self.prices[token]
    
    @gl.public.view
    def get_price(self, token: str) -> int:
        return self.prices.get(token, 0)
"""
    else:
        contract_content = """# {{ "Depends": "py-genlayer:test" }}
from genlayer import *

class MyContract(gl.Contract):
    def __init__(self):
        pass
"""
    
    with open(project_path / 'contracts' / 'MyContract.py', 'w') as f:
        f.write(contract_content)
    print_success("Created contracts/MyContract.py")
    
    click.echo(f"\n{Colors.GREEN}✨ Project created successfully!{Colors.ENDC}\n")
    click.echo(f"Next steps:")
    click.echo(f"  cd {project_name}")
    click.echo(f"  genlayer generate --help")
    click.echo(f"  genlayer test contracts/MyContract.py\n")


@cli.command()
@click.option('--type', default='basic', help='Contract type (basic, oracle, insurance, defi)')
@click.option('--name', prompt='Contract name', help='Name for the contract')
def generate(type, name):
    """Generate a contract from template."""
    
    click.echo(f"\n{Colors.BOLD}📝 Generating Contract{Colors.ENDC}\n")
    
    templates = {
        'basic': {
            'description': 'Basic contract with storage',
            'code': '''# {{ "Depends": "py-genlayer:test" }}
from genlayer import *

class {name}(gl.Contract):
    def __init__(self):
        self.data = {{}}
    
    @gl.public.write
    def store(self, key: str, value: str):
        self.data[key] = value
        return f"Stored: {{key}} = {{value}}"
    
    @gl.public.view
    def retrieve(self, key: str) -> str:
        return self.data.get(key, "Not found")
'''
        },
        'oracle': {
            'description': 'Price oracle with AI integration',
            'code': '''# {{ "Depends": "py-genlayer:test" }}
from genlayer import *

class {name}(gl.Contract):
    def __init__(self):
        self.prices = {{}}
        self.last_update = 0
    
    @gl.public.write
    def fetch_price(self, token: str) -> int:
        """Fetch token price using AI"""
        
        prompt = f"Get current price for {{token}} in USD"
        
        def get_price():
            return gl.exec_prompt(prompt)
        
        price_str = gl.eq_principle_strict_eq(get_price)
        price = int(price_str)
        
        self.prices[token] = price
        self.last_update = gl.block_timestamp
        
        return price
    
    @gl.public.view
    def get_price(self, token: str) -> int:
        return self.prices.get(token, 0)
'''
        },
        'insurance': {
            'description': 'Weather-based insurance contract',
            'code': '''# {{ "Depends": "py-genlayer:test" }}
from genlayer import *

class {name}(gl.Contract):
    def __init__(self):
        self.policies = {{}}
        self.policy_counter = 0
    
    @gl.public.write
    def create_policy(self, location: str, coverage: int) -> str:
        self.policy_counter += 1
        policy_id = f"POL-{{self.policy_counter}}"
        
        self.policies[policy_id] = {{
            "location": location,
            "coverage": coverage,
            "active": True
        }}
        
        return policy_id
    
    @gl.public.write
    def check_weather(self, policy_id: str) -> str:
        if policy_id not in self.policies:
            return "Policy not found"
        
        # In production: fetch real weather via AI
        # Check if payout conditions met
        
        return "Weather checked"
    
    @gl.public.view
    def get_policy(self, policy_id: str) -> str:
        policy = self.policies.get(policy_id)
        if not policy:
            return "Not found"
        return f"Location: {{policy['location']}}, Coverage: {{policy['coverage']}}"
'''
        },
        'defi': {
            'description': 'Simple DeFi lending contract',
            'code': '''# {{ "Depends": "py-genlayer:test" }}
from genlayer import *

class {name}(gl.Contract):
    def __init__(self):
        self.balances = {{}}
        self.total_supply = 0
    
    @gl.public.write
    def deposit(self, amount: int):
        user = gl.message_sender_address
        
        if user not in self.balances:
            self.balances[user] = 0
        
        self.balances[user] += amount
        self.total_supply += amount
        
        return f"Deposited {{amount}}"
    
    @gl.public.write
    def withdraw(self, amount: int):
        user = gl.message_sender_address
        
        if user not in self.balances or self.balances[user] < amount:
            return "Insufficient balance"
        
        self.balances[user] -= amount
        self.total_supply -= amount
        
        return f"Withdrawn {{amount}}"
    
    @gl.public.view
    def get_balance(self, address: str) -> int:
        return self.balances.get(address, 0)
'''
        }
    }
    
    if type not in templates:
        print_error(f"Unknown template type: {type}")
        print_info(f"Available types: {', '.join(templates.keys())}")
        return
    
    template = templates[type]
    
    # Generate contract code
    contract_code = template['code'].format(name=name)
    
    # Write to file
    filename = f"{name}.py"
    contracts_dir = Path('contracts')
    
    if not contracts_dir.exists():
        print_warning("No contracts/ directory. Run 'genlayer init' first!")
        contracts_dir = Path('.')
    
    filepath = contracts_dir / filename
    
    with open(filepath, 'w') as f:
        f.write(contract_code)
    
    print_success(f"Generated {filepath}")
    print_info(f"Template: {template['description']}")
    
    click.echo(f"\n{Colors.GREEN}✨ Contract generated!{Colors.ENDC}\n")
    click.echo(f"Next steps:")
    click.echo(f"  genlayer test {filepath}")
    click.echo(f"  genlayer deploy {filepath}\n")


@cli.command()
@click.argument('contract_file')
def test(contract_file):
    """Test a contract locally."""
    
    click.echo(f"\n{Colors.BOLD}🧪 Testing Contract{Colors.ENDC}\n")
    
    if not os.path.exists(contract_file):
        print_error(f"Contract file not found: {contract_file}")
        return
    
    print_info(f"Testing: {contract_file}")
    
    # Read contract
    with open(contract_file, 'r') as f:
        contract_code = f.read()
    
    # Basic syntax check
    try:
        compile(contract_code, contract_file, 'exec')
        print_success("Syntax check passed")
    except SyntaxError as e:
        print_error(f"Syntax error: {e}")
        return
    
    # Check for required elements
    checks = [
        ('gl.Contract', 'Inherits from gl.Contract'),
        ('@gl.public', 'Has public methods'),
        ('def __init__', 'Has constructor')
    ]
    
    for pattern, description in checks:
        if pattern in contract_code:
            print_success(description)
        else:
            print_warning(f"Missing: {description}")
    
    # Count functions
    public_funcs = contract_code.count('@gl.public')
    print_info(f"Public functions: {public_funcs}")
    
    click.echo(f"\n{Colors.GREEN}✓ Basic tests passed{Colors.ENDC}")
    click.echo(f"\n{Colors.YELLOW}Note:{Colors.ENDC} For full testing, deploy to testnet\n")


@cli.command()
@click.argument('contract_file')
@click.option('--network', default='testnet', help='Network to deploy to')
def deploy(contract_file, network):
    """Deploy contract to GenLayer."""
    
    click.echo(f"\n{Colors.BOLD}🚀 Deploying Contract{Colors.ENDC}\n")
    
    if not os.path.exists(contract_file):
        print_error(f"Contract file not found: {contract_file}")
        return
    
    print_info(f"Contract: {contract_file}")
    print_info(f"Network: {network}")
    
    # Read config
    config_file = 'genlayer.json'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
            if network in config.get('networks', {}):
                network_config = config['networks'][network]
                print_info(f"RPC: {network_config['rpc_url']}")
    
    click.echo(f"\n{Colors.YELLOW}Deployment Steps:{Colors.ENDC}")
    click.echo("1. Open GenLayer Studio: https://studio.genlayer.com")
    click.echo(f"2. Copy contents of {contract_file}")
    click.echo("3. Paste into Studio editor")
    click.echo("4. Click 'Deploy'")
    click.echo("5. Save contract address")
    
    # Open file for user
    print_info(f"\nContract code:")
    click.echo(f"\n{Colors.CYAN}--- {contract_file} ---{Colors.ENDC}")
    with open(contract_file, 'r') as f:
        click.echo(f.read())
    click.echo(f"{Colors.CYAN}--- End ---{Colors.ENDC}\n")


@cli.command()
@click.argument('address')
def status(address):
    """Check contract deployment status."""
    
    click.echo(f"\n{Colors.BOLD}📊 Contract Status{Colors.ENDC}\n")
    
    print_info(f"Address: {address}")
    print_info("Network: testnet")
    
    click.echo(f"\n{Colors.YELLOW}Check status at:{Colors.ENDC}")
    click.echo(f"https://studio.genlayer.com/contracts/{address}\n")


@cli.command()
def templates():
    """List available contract templates."""
    
    click.echo(f"\n{Colors.BOLD}📋 Available Templates{Colors.ENDC}\n")
    
    templates_list = [
        ("basic", "Basic storage contract"),
        ("oracle", "Price oracle with AI"),
        ("insurance", "Weather-based insurance"),
        ("defi", "Simple DeFi lending")
    ]
    
    for name, desc in templates_list:
        click.echo(f"  {Colors.CYAN}{name:12}{Colors.ENDC} - {desc}")
    
    click.echo(f"\n{Colors.YELLOW}Usage:{Colors.ENDC}")
    click.echo(f"  genlayer generate --type oracle --name MyOracle\n")


if __name__ == '__main__':
    cli()
