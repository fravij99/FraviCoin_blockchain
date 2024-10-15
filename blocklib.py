# blockchain.py

import datetime
import hashlib
import json
import uuid
# blockchain.py

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []  # Qui memorizziamo le transazioni
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.transactions
        }
        self.transactions = []  # Resetta le transazioni dopo che sono state aggiunte al blocco
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        """Aggiunge una nuova transazione alla lista di transazioni."""
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.print_previous_block()['index'] + 1

    def get_balance(self, user):
        """Calcola il saldo di un utente controllando tutte le transazioni nella blockchain."""
        balance = 0
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['sender'] == user:
                    balance -= transaction['amount']  # Riduci il saldo per l'importo inviato
                if transaction['receiver'] == user:
                    balance += transaction['amount']  # Aumenta il saldo per l'importo ricevuto
        return balance
    

    
    def smart_contract(blockchain, sender, receiver, amount):
        """Contratto intelligente che verifica se il mittente ha abbastanza saldo."""
        sender_balance = blockchain.get_balance(sender)
    
        if sender_balance >= amount:
            return True
        else:
            return False  # Il mittente non ha abbastanza fondi

    def register_user(self, username):
        """Registra un nuovo utente e assegna un bilancio e una lista di beni."""
        user_id = str(uuid.uuid4())
        self.users[user_id] = {
            'username': username,
            'balance': 100,  # Bilancio iniziale
            'goods': []  # Beni iniziali vuoti
        }
        return user_id

    def list_good_for_sale(self, user_id, good_name, price):
        """Elenco dei beni in vendita con un prezzo."""
        self.users[user_id]['goods'].append({
            'name': good_name,
            'price': price
        })

    def buy_good(self, buyer_id, seller_id, good_name):
        """Compra un bene da un utente."""
        goods = self.users[seller_id]['goods']
        good = next((g for g in goods if g['name'] == good_name), None)

        if good:
            price = good['price']
            if self.users[buyer_id]['balance'] >= price:
                # Effettua la transazione
                self.add_transaction(buyer_id, seller_id, price)
                self.users[buyer_id]['goods'].append(good)
                self.users[seller_id]['goods'].remove(good)
                return True
            else:
                return False  # Bilancio insufficiente
        return False  # Bene non trovato


    def update_balances(self):
        """Aggiorna i bilanci dopo ogni blocco minato."""
        for transaction in self.transactions:
            sender = transaction['sender']
            receiver = transaction['receiver']
            amount = transaction['amount']

            # Aggiorna il bilancio degli utenti
            self.users[sender]['balance'] -= amount
            self.users[receiver]['balance'] += amount


    def print_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
        return True
