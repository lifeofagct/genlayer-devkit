# GenLayer DevKit - Installation & Setup

Complete developer toolkit for GenLayer smart contracts.

---

## 🚀 Quick Install

```bash
# Clone or download the devkit
git clone https://github.com/lifeofagct/genlayer-devkit
cd genlayer-devkit

# Install dependencies
pip install -r requirements.txt

# Make CLI executable
chmod +x genlayer_devkit.py

# Optional: Add to PATH
sudo ln -s $(pwd)/genlayer_devkit.py /usr/local/bin/genlayer
```

---

## 📚 Usage Guide

### Initialize New Project

```bash
genlayer init my-awesome-project
cd my-awesome-project
```

Creates project structure:
```
my-awesome-project/
├── contracts/          # Your smart contracts
├── tests/             # Contract tests
├── scripts/           # Deployment scripts
├── docs/              # Documentation
├── genlayer.json      # Project config
├── requirements.txt   # Dependencies
└── README.md          # Project docs
```

### Generate Contracts from Templates

```bash
# List available templates
genlayer templates

# Generate a price oracle
genlayer generate --type oracle --name PriceOracle

# Generate weather insurance
genlayer generate --type insurance --name WeatherInsurance

# Generate basic contract
genlayer generate --type basic --name MyContract
```

### Test Contracts

```bash
# Test a specific contract
genlayer test contracts/MyContract.py

# Run all tests
genlayer test contracts/*.py
```

### Deploy Contracts

```bash
# Deploy to testnet
genlayer deploy contracts/MyContract.py --network testnet

# Deploy to mainnet
genlayer deploy contracts/MyContract.py --network mainnet
```

### Check Contract Status

```bash
# Check deployment status
genlayer status 0x1234abcd...
```

---

## 🎯 Complete Workflow Example

```bash
# 1. Create project
genlayer init price-oracle-project
cd price-oracle-project

# 2. Generate oracle contract
genlayer generate --type oracle --name BitcoinOracle

# 3. Test the contract
genlayer test contracts/BitcoinOracle.py

# 4. Deploy to testnet
genlayer deploy contracts/BitcoinOracle.py --network testnet

# 5. Check status
genlayer status <contract-address>
```

---

## 🛠️ Available Templates

### Basic Contract
Simple storage contract with key-value pairs.

```bash
genlayer generate --type basic --name MyStorage
```

**Generated code:**
- Storage methods (store/retrieve)
- Basic state management
- View and write functions

### Price Oracle
AI-powered price oracle for cryptocurrencies.

```bash
genlayer generate --type oracle --name TokenOracle
```

**Generated code:**
- Price fetching via AI
- Update mechanisms
- Price history tracking

### Weather Insurance
Smart insurance based on weather conditions.

```bash
genlayer generate --type insurance --name WeatherProtect
```

**Generated code:**
- Policy creation
- Weather checking
- Claim processing

### DeFi Lending
Simple lending/borrowing contract.

```bash
genlayer generate --type defi --name LendingPool
```

**Generated code:**
- Deposit/withdraw
- Balance tracking
- Interest calculation (basic)

---

## ⚙️ Configuration

### genlayer.json

```json
{
  "project_name": "my-project",
  "template": "oracle",
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
```

### Custom Templates

Add your own templates to `templates/` directory:

```python
# templates/my_custom_template.py
TEMPLATE_CODE = '''
# { "Depends": "py-genlayer:test" }
from genlayer import *

class {name}(gl.Contract):
    # Your template code here
'''
```

---

## 🧪 Testing Features

### Basic Tests
- Syntax validation
- Contract structure verification
- Function counting
- Required elements check

### Future Features (Coming Soon)
- Unit test generation
- Mock AI responses
- Integration tests
- Gas estimation

---

## 📖 Command Reference

### `genlayer init <project-name>`
Initialize new GenLayer project.

**Options:**
- `--template` - Project template (basic, oracle, defi)

**Example:**
```bash
genlayer init my-oracle --template oracle
```

### `genlayer generate`
Generate contract from template.

**Options:**
- `--type` - Contract type (basic, oracle, insurance, defi)
- `--name` - Contract name

**Example:**
```bash
genlayer generate --type oracle --name PriceOracle
```

### `genlayer test <contract-file>`
Test contract locally.

**Example:**
```bash
genlayer test contracts/MyContract.py
```

### `genlayer deploy <contract-file>`
Deploy contract to GenLayer.

**Options:**
- `--network` - Network (testnet, mainnet)

**Example:**
```bash
genlayer deploy contracts/Oracle.py --network testnet
```

### `genlayer status <address>`
Check contract deployment status.

**Example:**
```bash
genlayer status 0x1234abcd...
```

### `genlayer templates`
List available contract templates.

---

## 🎨 Customization

### Add Custom Commands

Edit `genlayer_devkit.py`:

```python
@cli.command()
@click.argument('contract_file')
def analyze(contract_file):
    """Analyze contract complexity."""
    # Your custom command code
    pass
```

### Extend Templates

Add new templates to the `templates` dict in `generate()` function.

---

## 🐛 Troubleshooting

### "genlayer: command not found"

**Solution:**
```bash
# Use full path
python3 /path/to/genlayer_devkit.py init my-project

# Or add alias
alias genlayer='python3 /path/to/genlayer_devkit.py'
```

### "No contracts/ directory"

**Solution:**
```bash
# Run init first
genlayer init my-project
cd my-project
# Now generate works
genlayer generate --type basic --name Test
```

### Import errors

**Solution:**
```bash
# Install dependencies
pip install click

# Or use requirements.txt
pip install -r requirements.txt
```

---

## 📦 Dependencies

Required Python packages:
- `click` - CLI framework
- `pytest` - Testing (optional)
- `genlayer-sdk` - GenLayer SDK (optional)

Install all:
```bash
pip install click pytest
```

---

## 🚀 Next Steps

1. **Read Examples** - Check `examples/` directory
2. **Deploy First Contract** - Follow workflow above
3. **Join Community** - GenLayer Discord
4. **Contribute** - Submit templates or features

---

## 📄 License

MIT License - Free to use and modify!

---

## 🤝 Contributing

Want to add features?

1. Fork the repo
2. Create new template
3. Add tests
4. Submit PR

---

## 📧 Support

- **GitHub Issues:** Report bugs
- **Discord:** Ask questions
- **Docs:** https://docs.genlayer.com

---

**Built with ❤️ for the GenLayer community**

Start building intelligent contracts faster! 🚀
