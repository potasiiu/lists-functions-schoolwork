"""This is a program that used for an auction and bidding
"""


def number_check(question):
    error = "\nPlease enter a valid input."
    num = ""
    while not num:
        try:
            num = float(input(question))
            return num
        except ValueError:
            print(error)


def bid():
    highest_bid = 0
    while True:
        print(f"The highest bid so far is ${highest_bid}")
        new_bid = number_check("What is your bid? ")
        if new_bid > highest_bid:
            highest_bid = new_bid
        elif new_bid == -1:
            return highest_bid
        else:
            print("Please enter a higher bid.")


def results(auction_item, reserve_price, highest_bid):
    if highest_bid > reserve_price:
        print(f"\nThe auction for the {auction_item} finished with a bid of ${highest_bid}")
    else:
        print(f"The {auction_item} didn't sell.")


def start():
    auction_item = input("What is the auction for? ")
    reserve_price = number_check("What is the reserve price? ")
    highest_bid = bid()
    results(auction_item,reserve_price,highest_bid)


start()
