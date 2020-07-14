stockDict = {
    "GE": "General Electric",
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

# for i in purchases:
#     print(i)
#     for (code, name) in stockDict.items():
#         if i[0] == code:
#             total = i[1] * i[3]
#             print(f"I purchased {name} stock for ${total}.")

new_stock_dict = dict()

for stock in stockDict:
    for purchase in purchases:
        if stock == purchase[0]:
            entry = f"{purchase[1]} shares at ${purchase[3]} each on {purchase[2]}"
            new_stock_dict[stock] = entry
            print(new_stock_dict)