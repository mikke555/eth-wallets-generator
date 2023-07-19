from eth_account import Account
import csv
import sys

Account.enable_unaudited_hdwallet_features()

def generate_eth_wallets(count):
    wallets = []

    for _ in range(count):
        acct, mnemonic = Account.create_with_mnemonic()
        wallets.append({
            'address': acct.address,
            'pkey': acct._private_key.hex(),
            'mnemonic': mnemonic,
        })

    with open('output.csv', mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['address', 'pkey', 'mnemonic'])
        writer.writeheader()  # Write the column headers
        writer.writerows(wallets)  # Write the data rows

        print(f"{count} wallets generated.")   
   

if len(sys.argv) < 2:
    print("Please provide a number of wallets to create")
else:
    try:
        count = int(sys.argv[1])
        generate_eth_wallets(count)
    except ValueError:
        print("Invalid integer parameter provided")
