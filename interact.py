from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if not web3.is_connected():
    print("Connection to Ganache failed!")
    exit()

print("Connected to Ganache!")

# Set the default account
web3.eth.default_account = web3.eth.accounts[0]
default_account = web3.eth.accounts[0]  # Explicitly assign the default account

# Contract address (replace with your contract address)
contract_address = "0xB90571B75adACf50d17391F40ca9B271F6936471"

# Load compiled contract
with open(".venv/compiled_hello_world.json", "r") as file:
    compiled_contract = json.load(file)

# Get ABI
abi = compiled_contract["contracts"]["HelloWorld.sol"]["HelloWorld"]["abi"]

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Interact with the contract
# 1. Retrieve the initial message
initial_message = contract.functions.getMessage().call()
print(f"Initial message: {initial_message}")

# 2. Update the message
tx_hash = contract.functions.setMessage("Hello, PyCharm World!").transact({'from': default_account})
web3.eth.wait_for_transaction_receipt(tx_hash)
print("Message updated!")

# 3. Retrieve the updated message
updated_message = contract.functions.getMessage().call()
print(f"Updated message: {updated_message}")
