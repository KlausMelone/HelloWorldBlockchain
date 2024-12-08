from solcx import compile_standard, install_solc
import json

# Install the Solidity compiler
install_solc("0.8.0")

# Read the Solidity file
with open("contracts/HelloWorld.sol", "r") as file:
    hello_world_sol = file.read()

# Compile the Solidity contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"HelloWorld.sol": {"content": hello_world_sol}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

# Save the compiled contract to a JSON file
with open(".venv/compiled_hello_world.json", "w") as file:
    json.dump(compiled_sol, file)

print("Contract compiled successfully! ABI and Bytecode saved.")
