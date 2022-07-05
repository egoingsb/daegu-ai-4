# def vat(가격, 부가가치세율=0.1):
#     print(가격 * 부가가치세율)

# def vat_email(가격, 부가가치세율=0.1):
#     email('egoing@gmail.com', 가격 * 부가가치세율)

def vat(가격, 부가가치세율=0.1):
    return 가격 * 부가가치세율

print(vat(2000))
# email('egoing@gmail.com', vat(3000,0.2))
