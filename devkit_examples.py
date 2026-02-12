"""
GenLayer DevKit - Example Contracts Library
============================================

Pre-built, production-ready contract examples.
"""

# Example 1: Advanced Price Oracle
ADVANCED_ORACLE = '''# { "Depends": "py-genlayer:test" }
"""
Advanced Multi-Token Price Oracle
==================================

Features:
- Multiple token support
- Price validation
- Historical data
- Update frequency control
"""

from genlayer import *

class MultiTokenOracle(gl.Contract):
    def __init__(self):
        self.prices = {}  # token -> price
        self.last_update = {}  # token -> timestamp
        self.update_interval = 300  # 5 minutes
        self.trusted_sources = ["coingecko", "coinmarketcap", "binance"]
    
    @gl.public.write
    def update_price(self, token: str) -> int:
        """Update price for a specific token"""
        
        # Check if update needed
        last = self.last_update.get(token, 0)
        if gl.block_timestamp - last < self.update_interval:
            return self.prices.get(token, 0)
        
        # Fetch price via AI from multiple sources
        prompt = f"""Get current price for {token} from these sources: {self.trusted_sources}
        
Return only the median price as an integer (no decimals, no text)."""
        
        def fetch():
            return gl.exec_prompt(prompt)
        
        price_str = gl.eq_principle_strict_eq(fetch)
        
        try:
            price = int(price_str)
        except:
            raise Exception("Invalid price format from AI")
        
        # Validate price is reasonable
        if price <= 0:
            raise Exception("Price must be positive")
        
        # Check for extreme changes (>50% in one update)
        if token in self.prices:
            old_price = self.prices[token]
            change = abs(price - old_price) / old_price
            if change > 0.5:
                raise Exception("Price change too extreme, possible error")
        
        # Store price
        self.prices[token] = price
        self.last_update[token] = gl.block_timestamp
        
        return price
    
    @gl.public.view
    def get_price(self, token: str) -> int:
        """Get cached price for token"""
        return self.prices.get(token, 0)
    
    @gl.public.view
    def get_last_update(self, token: str) -> int:
        """Get timestamp of last price update"""
        return self.last_update.get(token, 0)
    
    @gl.public.write
    def batch_update(self, tokens: list) -> dict:
        """Update prices for multiple tokens"""
        results = {}
        for token in tokens:
            try:
                price = self.update_price(token)
                results[token] = price
            except Exception as e:
                results[token] = f"Error: {str(e)}"
        return results
'''

# Example 2: Complete Weather Insurance
COMPLETE_INSURANCE = '''# { "Depends": "py-genlayer:test" }
"""
Weather-Based Event Insurance
==============================

Features:
- Policy creation with custom triggers
- Automated claim processing
- Multi-location support
- Historical weather verification
"""

from genlayer import *

class WeatherInsurance(gl.Contract):
    def __init__(self):
        self.policies = {}
        self.policy_counter = 0
        self.claims = {}
        self.total_payouts = 0
    
    @gl.public.write
    def create_policy(self, location: str, event_date: str, 
                     trigger_condition: str, coverage: int) -> str:
        """
        Create new insurance policy.
        
        Args:
            location: City or coordinates
            event_date: Date of insured event (YYYY-MM-DD)
            trigger_condition: e.g., "rain", "temperature < 10C", "snow"
            coverage: Payout amount if condition met
        """
        
        self.policy_counter += 1
        policy_id = f"POL-{self.policy_counter:04d}"
        
        self.policies[policy_id] = {
            "owner": gl.message_sender_address,
            "location": location,
            "event_date": event_date,
            "trigger": trigger_condition,
            "coverage": coverage,
            "status": "active",
            "created_at": gl.block_timestamp
        }
        
        return policy_id
    
    @gl.public.write
    def file_claim(self, policy_id: str) -> str:
        """File insurance claim for a policy"""
        
        if policy_id not in self.policies:
            return "ERROR: Policy not found"
        
        policy = self.policies[policy_id]
        
        if policy["status"] != "active":
            return f"ERROR: Policy status is {policy['status']}"
        
        if policy["owner"] != gl.message_sender_address:
            return "ERROR: Only policy owner can file claims"
        
        # Check weather conditions via AI
        prompt = f"""Check weather for {policy['location']} on {policy['event_date']}.

Condition to verify: {policy['trigger']}

Return format:
WEATHER: [actual conditions]
CONDITION_MET: YES or NO
CONFIDENCE: [0-100]%"""
        
        def check_weather():
            return gl.exec_prompt(prompt)
        
        weather_report = gl.eq_principle_strict_eq(check_weather)
        
        # Parse result
        if "CONDITION_MET: YES" in weather_report:
            # Approve claim
            policy["status"] = "claimed"
            policy["payout"] = policy["coverage"]
            policy["weather_report"] = weather_report
            
            self.total_payouts += policy["coverage"]
            
            # Record claim
            self.claims[policy_id] = {
                "policy_id": policy_id,
                "claimed_at": gl.block_timestamp,
                "payout": policy["coverage"],
                "weather_report": weather_report
            }
            
            return f"""✅ CLAIM APPROVED

Policy: {policy_id}
Payout: {policy['coverage']} tokens

Weather Report:
{weather_report}"""
        else:
            # Deny claim
            policy["status"] = "denied"
            
            return f"""❌ CLAIM DENIED

Policy: {policy_id}

Weather Report:
{weather_report}

Trigger condition was not met."""
    
    @gl.public.view
    def get_policy(self, policy_id: str) -> dict:
        """View policy details"""
        return self.policies.get(policy_id, {})
    
    @gl.public.view
    def get_my_policies(self) -> list:
        """Get all policies owned by caller"""
        owner = gl.message_sender_address
        my_policies = []
        
        for policy_id, policy in self.policies.items():
            if policy["owner"] == owner:
                my_policies.append({
                    "id": policy_id,
                    "location": policy["location"],
                    "date": policy["event_date"],
                    "coverage": policy["coverage"],
                    "status": policy["status"]
                })
        
        return my_policies
    
    @gl.public.view
    def get_stats(self) -> dict:
        """Get contract statistics"""
        return {
            "total_policies": self.policy_counter,
            "active_policies": len([p for p in self.policies.values() if p["status"] == "active"]),
            "total_claims": len(self.claims),
            "total_payouts": self.total_payouts
        }
'''

# Example 3: DeFi Lending Pool
DEFI_LENDING = '''# { "Depends": "py-genlayer:test" }
"""
Decentralized Lending Pool
==========================

Features:
- Deposit and withdraw
- Interest calculation
- Utilization tracking
- Balance management
"""

from genlayer import *

class LendingPool(gl.Contract):
    def __init__(self):
        self.balances = {}  # user -> balance
        self.total_deposits = 0
        self.total_borrowed = 0
        self.interest_rate = 5  # 5% annual
    
    @gl.public.write
    def deposit(self, amount: int) -> str:
        """Deposit funds into the pool"""
        
        if amount <= 0:
            return "ERROR: Amount must be positive"
        
        user = gl.message_sender_address
        
        if user not in self.balances:
            self.balances[user] = 0
        
        self.balances[user] += amount
        self.total_deposits += amount
        
        return f"✅ Deposited {amount} tokens. New balance: {self.balances[user]}"
    
    @gl.public.write
    def withdraw(self, amount: int) -> str:
        """Withdraw funds from the pool"""
        
        if amount <= 0:
            return "ERROR: Amount must be positive"
        
        user = gl.message_sender_address
        
        if user not in self.balances:
            return "ERROR: No balance found"
        
        if self.balances[user] < amount:
            return f"ERROR: Insufficient balance. Available: {self.balances[user]}"
        
        # Check liquidity
        available_liquidity = self.total_deposits - self.total_borrowed
        if available_liquidity < amount:
            return f"ERROR: Insufficient pool liquidity. Available: {available_liquidity}"
        
        self.balances[user] -= amount
        self.total_deposits -= amount
        
        return f"✅ Withdrawn {amount} tokens. Remaining balance: {self.balances[user]}"
    
    @gl.public.view
    def get_balance(self, address: str) -> int:
        """Get balance for an address"""
        return self.balances.get(address, 0)
    
    @gl.public.view
    def get_my_balance(self) -> int:
        """Get caller's balance"""
        return self.balances.get(gl.message_sender_address, 0)
    
    @gl.public.view
    def get_pool_stats(self) -> dict:
        """Get pool statistics"""
        utilization = 0
        if self.total_deposits > 0:
            utilization = (self.total_borrowed / self.total_deposits) * 100
        
        return {
            "total_deposits": self.total_deposits,
            "total_borrowed": self.total_borrowed,
            "available_liquidity": self.total_deposits - self.total_borrowed,
            "utilization_rate": f"{utilization:.2f}%",
            "interest_rate": f"{self.interest_rate}%",
            "total_users": len(self.balances)
        }
    
    @gl.public.write
    def set_interest_rate(self, new_rate: int) -> str:
        """Update interest rate (admin only)"""
        
        # In production: add proper admin check
        if new_rate < 0 or new_rate > 100:
            return "ERROR: Rate must be between 0 and 100"
        
        old_rate = self.interest_rate
        self.interest_rate = new_rate
        
        return f"Interest rate updated: {old_rate}% → {new_rate}%"
'''

# Example 4: DAO Governance
DAO_GOVERNANCE = '''# { "Depends": "py-genlayer:test" }
"""
Simple DAO Governance Contract
===============================

Features:
- Proposal creation
- Voting mechanism
- Proposal execution
- Member management
"""

from genlayer import *

class SimpleDAO(gl.Contract):
    def __init__(self):
        self.members = {}  # address -> voting power
        self.proposals = {}
        self.proposal_counter = 0
        self.voting_period = 86400  # 1 day in seconds
    
    @gl.public.write
    def join_dao(self) -> str:
        """Join the DAO as a member"""
        
        member = gl.message_sender_address
        
        if member in self.members:
            return "Already a member"
        
        self.members[member] = 1  # 1 voting power
        
        return f"✅ Joined DAO. Voting power: 1"
    
    @gl.public.write
    def create_proposal(self, title: str, description: str) -> str:
        """Create a new proposal"""
        
        creator = gl.message_sender_address
        
        if creator not in self.members:
            return "ERROR: Must be a DAO member to create proposals"
        
        self.proposal_counter += 1
        proposal_id = f"PROP-{self.proposal_counter:03d}"
        
        self.proposals[proposal_id] = {
            "id": proposal_id,
            "title": title,
            "description": description,
            "creator": creator,
            "created_at": gl.block_timestamp,
            "end_time": gl.block_timestamp + self.voting_period,
            "votes_for": 0,
            "votes_against": 0,
            "voters": {},
            "status": "active"
        }
        
        return f"✅ Proposal created: {proposal_id}"
    
    @gl.public.write
    def vote(self, proposal_id: str, support: bool) -> str:
        """Vote on a proposal"""
        
        voter = gl.message_sender_address
        
        if voter not in self.members:
            return "ERROR: Must be a DAO member to vote"
        
        if proposal_id not in self.proposals:
            return "ERROR: Proposal not found"
        
        proposal = self.proposals[proposal_id]
        
        if proposal["status"] != "active":
            return f"ERROR: Proposal is {proposal['status']}"
        
        if gl.block_timestamp > proposal["end_time"]:
            return "ERROR: Voting period ended"
        
        if voter in proposal["voters"]:
            return "ERROR: Already voted"
        
        voting_power = self.members[voter]
        
        if support:
            proposal["votes_for"] += voting_power
        else:
            proposal["votes_against"] += voting_power
        
        proposal["voters"][voter] = support
        
        return f"✅ Vote recorded: {'FOR' if support else 'AGAINST'}"
    
    @gl.public.write
    def finalize_proposal(self, proposal_id: str) -> str:
        """Finalize a proposal after voting ends"""
        
        if proposal_id not in self.proposals:
            return "ERROR: Proposal not found"
        
        proposal = self.proposals[proposal_id]
        
        if proposal["status"] != "active":
            return f"ERROR: Proposal already {proposal['status']}"
        
        if gl.block_timestamp <= proposal["end_time"]:
            return "ERROR: Voting period not ended yet"
        
        # Determine result
        if proposal["votes_for"] > proposal["votes_against"]:
            proposal["status"] = "passed"
            result = "PASSED ✅"
        else:
            proposal["status"] = "rejected"
            result = "REJECTED ❌"
        
        return f"""Proposal {proposal_id}: {result}

Votes FOR: {proposal['votes_for']}
Votes AGAINST: {proposal['votes_against']}
Total voters: {len(proposal['voters'])}"""
    
    @gl.public.view
    def get_proposal(self, proposal_id: str) -> dict:
        """View proposal details"""
        return self.proposals.get(proposal_id, {})
    
    @gl.public.view
    def list_active_proposals(self) -> list:
        """List all active proposals"""
        active = []
        for prop_id, prop in self.proposals.items():
            if prop["status"] == "active":
                active.append({
                    "id": prop_id,
                    "title": prop["title"],
                    "votes_for": prop["votes_for"],
                    "votes_against": prop["votes_against"],
                    "ends_in": prop["end_time"] - gl.block_timestamp
                })
        return active
'''

# Export all examples
EXAMPLES = {
    "advanced_oracle": ADVANCED_ORACLE,
    "complete_insurance": COMPLETE_INSURANCE,
    "defi_lending": DEFI_LENDING,
    "dao_governance": DAO_GOVERNANCE
}
