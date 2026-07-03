# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)
print("Welcome to Secret Auction!")
bids = {}

name = input("What is your name? ")
bid = float(input("What is your bid? $"))
bids[name] = bid

flow = input("Are there any other bidders? Type 'yes' or 'no.'").lower()
while flow == "yes":
    print("\n" * 100)
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid

    flow = input("Are there any other bidders? Type 'yes' or 'no.'").lower()

# print(bids)
max_bid_value = 0
max_bidder = ""

for bidder in bids:
    if bids[bidder] > max_bid_value:
        max_bid_value = bids[bidder]
        max_bidder = bidder

print(f"The winner is {max_bidder} with a bid of ${max_bid_value}")

