# Blocklib.py Library
<img align="right" src=https://github.com/fravij99/FraviCoin_blockchain/blob/master/img.jpeg  width="270">


## Introduction
This library implements a simple blockchain in Python, allowing for user registration, transactions, and smart contracts. The library is designed to be easily extensible and adaptable for various applications.

## Key Features
- Creation and management of a blockchain.
- Addition of transactions between users.
- Registration of new users.
- Management of goods and trade.
- Smart contracts for balance verification.
- Requirements
- Make sure you have Python 3.x installed. You can download Python from python.org.

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
2. Install dependencies, if any:
```bash
pip install -r requirements.txt
```
## Usage
1. Importing the Library
You can import the library in your Python project as follows:
```python

from blockchain import Blockchain
```
2. Creating a New Blockchain
To create a new instance of the blockchain:

```python
blockchain = Blockchain()
```
3. Registering a New User
To register a new user:

```python
user_id = blockchain.register_user("Username")
print("User registered with ID:", user_id)
```
4. Adding a Transaction
To add a new transaction between two users:

```python
next_index = blockchain.add_transaction(sender=user_id1, receiver=user_id2, amount=10)
print("Transaction added to block:", next_index)
```
5. Checking User Balance
To get the balance of a user:

```python
balance = blockchain.get_balance(user_id)
print("User balance:", balance)
```
6. Listing Goods for Sale
To add goods for sale:

```python
blockchain.list_good_for_sale(user_id, "GoodName", 50)
```
7. Buying a Good
To purchase a good from another user:

```python
success = blockchain.buy_good(buyer_id, seller_id, "GoodName")
if success:
    print("Purchase completed successfully!")
else:
    print("Purchase failed.")
```
8. Validating the Blockchain
To check if the blockchain is valid:

```python
is_valid = blockchain.chain_valid(blockchain.chain)
if is_valid:
    print("The blockchain is valid.")
else:
    print("The blockchain is not valid.")
```
9. Smart Contracts Functionality
The smart_contract function checks if the sender has enough balance to make a transaction:

```python
if blockchain.smart_contract(blockchain, sender_id, receiver_id, amount):
    print("Smart contract: sufficient balance.")
else:
    print("Smart contract: insufficient balance.")
```
## Contributing
If you would like to contribute to this project, please open an issue or a pull request. All contributions are welcome!

## License
This library is distributed under the MIT License. See the LICENSE file for more details.

## Contact
For further information, you can contact me at [fravilla30@gmail.com].

