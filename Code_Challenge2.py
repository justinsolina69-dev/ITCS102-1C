Amount = eval(input(" Hi Please ENTER Withdraw amount : "))
print("Here's the breakdown ...")

Thousand = Amount // 1000
Amount %= 1000

FiveHundred = Amount // 500
Amount %= 500

TwoHundred = Amount // 200
Amount %= 200

OneHundred = Amount // 100
Amount %= 100

Fifty = Amount // 50
Amount %= 50

Twenty = Amount // 20
Amount %= 20

Ten = Amount // 10
Amount %= 10

Five = Amount // 5
Amount %= 5

One = Amount // 1
Amount %= 1

print(" ₱1000:", Thousand )
print(" ₱500:", FiveHundred )
print(" ₱200:", TwoHundred )
print(" ₱100:", OneHundred)
print(" ₱50:", Fifty)
print(" ₱20:", Twenty )
print(" ₱10:", Ten )
print(" ₱5:", Five )
print(" ₱1:", One)

