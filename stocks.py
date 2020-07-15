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

for i in purchases:
    for (code, name) in stockDict.items():
        if i[0] == code:
            total = i[1] * i[3]
            formatted_total = "{:,}".format(total)
            print(f"I purchased {name} stock for ${formatted_total}.")
            print('')


for stock in stockDict:
    stock_value = 0
    print(f'------ {stock} ------')
    for purchase in purchases:
        if stock == purchase[0]:
            stock_value += (purchase[1] * purchase[3])
            print(f"{purchase[1]} shares at ${purchase[3]} each on {purchase[2]}.")
    formatted_stock_value = "{:,}".format(stock_value)
    print(f'Total value of stock in portfolio: ${formatted_stock_value}.')
    print('')