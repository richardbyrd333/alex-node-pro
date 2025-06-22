from .detector import get_large_transactions

def main():
    txs = get_large_transactions()
    if not txs:
        print("No whale movements detected.")
    else:
        print("🐋 Whale Alert!")
        for tx in txs:
            print(f"From: {tx['from']} To: {tx['to']}")
            print(f"Value: ${tx['value_usd']:.2f} USD")
            print(f"TxHash: {tx['hash']}")
            print("-" * 40)

if __name__ == "__main__":
    main()
