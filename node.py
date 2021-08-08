from uuid import uuid4

from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet


class Node:
    def __init__(self):
        # self.wallet.public_key = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        """ Returns the transaction value from the user input (a new transaction amount) as a float. """
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        return tx_recipient, tx_amount

    def get_user_choice(self):
        """ Returns the choice from the user input as a string. """
        user_input = input('Your choice: ')
        return user_input

    def print_blockchain_elements(self):
        """ Prints the blockchain list  """
        for block in self.blockchain.chain:
            print('Outputting Block')
            print(block)

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('5: Create wallet')
            print('6: Load wallet')
            print('7: Save wallet')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(
                    self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print('Mining failed! Seems like you don\'t have a wallet yet')
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please try again.')
            if not Verification.verify_chain(self.blockchain.chain):
                print('Manipulation detected!')
                waiting_for_input = False
            print('Balance of {}: {:6.2f}'.format(
                self.wallet.public_key, self.blockchain.get_balance()))

        print('Done!')


if __name__ == '__main__':
    node = Node()
    node.listen_for_input()
