from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Replace with your Ganache URL if different
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if not web3.is_connected():
    print("Connection to Ganache failed!")
    exit()

print("Connected to Ganache!")

# Set default account (first account in Ganache)
web3.eth.default_account = web3.eth.accounts[0]

# Load compiled contract
with open(".venv/compiled_hello_world.json", "r") as file:
    compiled_contract = json.load(file)

# Get bytecode and ABI
bytecode = compiled_contract["contracts"]["HelloWorld.sol"]["HelloWorld"]["evm"]["bytecode"]["object"]
abi = compiled_contract["contracts"]["HelloWorld.sol"]["HelloWorld"]["abi"]

# Deploy the contract
HelloWorld = web3.eth.contract(abi=abi, bytecode=bytecode)
print("Deploying contract...")
tx_hash = HelloWorld.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Get the contract address
contract_address = tx_receipt.contractAddress
print(f"Contract deployed at address: {contract_address}")
