# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the transaction value from the user input (a new transaction amount) as a float. """
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    """ Returns the choice from the user input as a string. """
    user_input = input('Your choice: ')
    return user_input


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


def print_blockchain_elements():
    """ Prints the blockchain list  """
    for block in blockchain:
        print('Outputting Block')
        print(block)


# Get the first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_transaction(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulte the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please try again.')
    if not verify_chain():
        print('Manipulation detected!')
        break

print('Done!')
