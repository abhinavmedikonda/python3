loan = float(input("total loan: ")) # 1000
apr = float(input("annual percentage rate: ")) # 10
instalment = float(input("instalment amount: ")) # 50
months = int(input("months to calculate: ")) # 24

mpr = apr/100/12

print('mpr: ', mpr)

for i in range(months):
    interest = loan * mpr
    loan += interest
    if(loan < instalment):
        print("loan payment is complete in", i+1, "months")
        print("last payment:", loan)
        break

    loan -= instalment
    print(f'payment {i}, monthly interest: {interest}', end='')
    print(', pending amount:', loan)