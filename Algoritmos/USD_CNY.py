def usd_to_cny(usd_amount):
    conversion_rate = 6.75
    cny_amount = usd_amount * conversion_rate
    return f"{cny_amount:.2f} Chinese Yuan"

# Test cases
print(usd_to_cny(15))  # Should return '101.25 Chinese Yuan'
print(usd_to_cny(465))  # Should return '3138.75 Chinese Yuan'