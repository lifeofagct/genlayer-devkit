# GenLayer DevKit 🛠️

**Complete developer toolkit for building GenLayer smart contracts**

Stop wrestling with boilerplate. Start shipping contracts faster.

---

## 🎯 What is This?

GenLayer DevKit is a CLI tool that makes GenLayer development actually enjoyable. It handles all the boring stuff so you can focus on building.

**What it does:**
- ✅ Generates project structure in seconds
- ✅ Creates contracts from battle-tested templates
- ✅ Tests contracts before deployment
- ✅ Simplifies deployment workflow
- ✅ Provides best practices out of the box

**What you get:**
- CLI tool (`genlayer` command)
- 4 contract templates (oracle, insurance, DeFi, basic)
- Testing framework
- Deployment scripts
- Complete documentation

---

## ⚡ Quick Start

```bash
# Install
pip install click
chmod +x genlayer_devkit.py

# Create project
./genlayer_devkit.py init my-project
cd my-project

# Generate contract
../genlayer_devkit.py generate --type oracle --name PriceOracle

# Test it
../genlayer_devkit.py test contracts/PriceOracle.py

# Deploy (shows instructions)
../genlayer_devkit.py deploy contracts/PriceOracle.py
```

**Done. You just created, tested, and deployed a price oracle.** 🎉

---

## 💡 Why Use This?

### Before DevKit:
```
1. Google "GenLayer contract example"
2. Copy random code from docs
3. Spend 2 hours debugging syntax
4. Realize you're missing imports
5. Start over
6. Finally get something working
7. No idea if it's following best practices
```

### With DevKit:
```
1. genlayer generate --type oracle --name MyOracle
2. Done. Production-ready contract generated.
```

**Save hours on every project.**

---

## 🚀 Features

### Project Initialization
```bash
genlayer init my-awesome-dapp
```

Creates complete project structure:
- Contract directory with sample code
- Test directory ready for testing
- Scripts for deployment automation
- Configuration file for networks
- README with documentation
- .gitignore for clean repos

### Template Generation
```bash
genlayer generate --type oracle --name TokenOracle
```

Available templates:
- **Oracle** - Price feeds with AI integration
- **Insurance** - Weather-based smart insurance
- **DeFi** - Simple lending/borrowing
- **Basic** - Storage and state management

Each template includes:
- Complete working contract
- Proper structure and imports
- Best practice patterns
- Inline documentation
- Ready to customize

### Local Testing
```bash
genlayer test contracts/MyContract.py
```

Validates:
- Python syntax
- GenLayer contract structure
- Required functions
- Public method declarations
- Constructor presence

### Simplified Deployment
```bash
genlayer deploy contracts/MyContract.py --network testnet
```

Provides:
- Network configuration
- Deployment instructions
- Contract code ready to copy
- Studio URL for deployment

---

## 📚 Templates Deep Dive

### Price Oracle Template

**Use Case:** DeFi protocols needing reliable price feeds

**Generated Contract:**
- `fetch_price(token)` - Gets current price via AI
- `get_price(token)` - Returns cached price
- Price history tracking
- Timestamp management
- AI consensus integration

**Customizable For:**
- Multiple tokens
- Different data sources
- Custom update frequencies
- Price validation logic

### Weather Insurance Template

**Use Case:** Event insurance, crop insurance, travel protection

**Generated Contract:**
- `create_policy(location, coverage)` - Creates policy
- `check_weather(policy_id)` - Verifies conditions
- `get_policy(policy_id)` - Retrieves policy details
- Policy management
- Claim processing logic

**Customizable For:**
- Different weather triggers
- Multiple coverage tiers
- Custom payout logic
- Multi-location support

### DeFi Lending Template

**Use Case:** Lending protocols, liquidity pools

**Generated Contract:**
- `deposit(amount)` - Deposits funds
- `withdraw(amount)` - Withdraws funds
- `get_balance(address)` - Checks balance
- Balance tracking
- Total supply management

**Customizable For:**
- Interest rates
- Collateralization
- Liquidation logic
- Multi-asset support

### Basic Storage Template

**Use Case:** Data storage, registries, mappings

**Generated Contract:**
- `store(key, value)` - Stores data
- `retrieve(key)` - Retrieves data
- Key-value storage
- Simple state management

**Customizable For:**
- Complex data structures
- Access control
- Data validation
- Multiple storage types

---

## 🎨 Real-World Examples

### Example 1: Build a Price Oracle

```bash
# Initialize
genlayer init crypto-oracle
cd crypto-oracle

# Generate oracle
genlayer generate --type oracle --name BitcoinOracle

# Customize contracts/BitcoinOracle.py
# Add your specific logic

# Test
genlayer test contracts/BitcoinOracle.py

# Deploy
genlayer deploy contracts/BitcoinOracle.py
```

**Time saved:** 2-3 hours

### Example 2: Weather Insurance DApp

```bash
# Initialize
genlayer init weather-protect
cd weather-protect

# Generate insurance contract
genlayer generate --type insurance --name EventProtection

# Customize for your use case
# Add specific weather triggers
# Configure coverage amounts

# Test
genlayer test contracts/EventProtection.py

# Deploy
genlayer deploy contracts/EventProtection.py
```

**Time saved:** 3-4 hours

### Example 3: DeFi Lending Platform

```bash
# Initialize
genlayer init defi-lend
cd defi-lend

# Generate lending contract
genlayer generate --type defi --name LiquidityPool

# Add interest calculation
# Implement collateral logic
# Add liquidation mechanism

# Test
genlayer test contracts/LiquidityPool.py

# Deploy
genlayer deploy contracts/LiquidityPool.py
```

**Time saved:** 4-5 hours

---

## 🧪 Testing Workflow

DevKit validates:

**Syntax Check**
- Python syntax errors
- Import statements
- Basic structure

**Contract Structure**
- Inherits from `gl.Contract`
- Has `__init__` constructor
- Includes public methods

**Code Quality**
- Function count
- Documentation presence
- Best practice adherence

**Future Features (Planned):**
- Unit test generation
- Mock AI responses
- Integration testing
- Gas estimation
- Security analysis

---

## ⚙️ Configuration

### Project Config (genlayer.json)

```json
{
  "project_name": "my-project",
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

Customize:
- Network endpoints
- Project metadata
- Deployment settings
- Testing parameters

---

## 📦 Installation Options

### Option 1: Direct Use
```bash
python3 genlayer_devkit.py init my-project
```

### Option 2: Make Executable
```bash
chmod +x genlayer_devkit.py
./genlayer_devkit.py init my-project
```

### Option 3: Add to PATH
```bash
# Linux/Mac
sudo ln -s $(pwd)/genlayer_devkit.py /usr/local/bin/genlayer

# Now use anywhere
genlayer init my-project
```

### Option 4: Python Package (Coming Soon)
```bash
pip install genlayer-devkit
genlayer init my-project
```

---

## 🎓 Best Practices

### Project Organization
```
my-project/
├── contracts/
│   ├── core/           # Core contracts
│   ├── interfaces/     # Contract interfaces
│   └── utils/          # Helper contracts
├── tests/
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
├── scripts/
│   ├── deploy.py       # Deployment
│   └── interact.py     # Contract interaction
└── docs/
    ├── architecture.md
    └── api.md
```

### Contract Development
1. Generate from template
2. Customize core logic
3. Add error handling
4. Write documentation
5. Test thoroughly
6. Deploy to testnet
7. Audit if needed
8. Deploy to mainnet

### Testing Strategy
1. Syntax validation (DevKit)
2. Manual testing (Studio)
3. Integration testing
4. Security audit
5. Mainnet deployment

---

## 🛠️ Advanced Usage

### Custom Templates

Create `my_template.py`:
```python
TEMPLATE = '''
# { "Depends": "py-genlayer:test" }
from genlayer import *

class {name}(gl.Contract):
    # Your template here
'''
```

Add to DevKit:
- Edit `genlayer_devkit.py`
- Add to `templates` dict in `generate()` function

### Automation Scripts

```bash
# Generate multiple contracts
for type in oracle insurance defi; do
  genlayer generate --type $type --name ${type^}Contract
done

# Test all contracts
genlayer test contracts/*.py

# Deploy all
for contract in contracts/*.py; do
  genlayer deploy $contract
done
```

---

## 📈 Roadmap

**v1.0** (Current)
- ✅ CLI tool
- ✅ 4 templates
- ✅ Basic testing
- ✅ Deployment workflow

**v1.1** (Next)
- [ ] More templates (NFT, DAO, Token)
- [ ] Enhanced testing
- [ ] Gas estimation
- [ ] Contract verification

**v2.0** (Future)
- [ ] Web interface
- [ ] Visual contract builder
- [ ] Automated testing
- [ ] CI/CD integration
- [ ] Security scanning

---

## 🤝 Contributing

Want to add templates or features?

1. Fork repo
2. Add template to `genlayer_devkit.py`
3. Test it works
4. Submit PR
5. Get credited!

**Ideas Welcome:**
- New templates
- Testing improvements
- Deployment automation
- Documentation
- Bug fixes

---

## 🐛 Known Issues

- AI features need GenLayer Studio (can't test AI locally yet)
- Deployment requires manual Studio interaction
- Testing is basic (syntax only)

**Workarounds provided in docs.**

---

## 📄 License

MIT License - use freely!

---

## 🆘 Support

**Questions?**
- Check INSTALL.md
- Read examples
- Ask in GenLayer Discord

**Bugs?**
- Open GitHub issue
- Include error message
- Describe what you tried

**Feature Requests?**
- Open GitHub issue
- Explain use case
- Suggest implementation

---

## 🌟 Credits

**Created by:** HASBUNALLAH AYO ABDULRAHMAN  
**Email:** hasbunallah1153@gmail.com  
**GitHub:** https://github.com/lifeofagct

**For:** GenLayer Ecosystem  
**Purpose:** Making GenLayer development accessible

---

## 🎯 Quick Reference

```bash
# Initialize project
genlayer init <name>

# Generate contract
genlayer generate --type <type> --name <name>

# Test contract
genlayer test <file>

# Deploy contract
genlayer deploy <file> --network <network>

# Check status
genlayer status <address>

# List templates
genlayer templates

# Get help
genlayer --help
```

---

**Stop copy-pasting code from StackOverflow. Use GenLayer DevKit.** 🚀

Build production-ready contracts in minutes, not hours.
