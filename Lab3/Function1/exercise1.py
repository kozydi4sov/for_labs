def grams_to(grams):
    return 28.3495231 * grams
grams_amount = float(input("Enter the amount in grams: "))
ounce_result = grams_to(grams_amount)
print(ounce_result)