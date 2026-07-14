bank_bal = 850

print(f"Your current bank balance:R {bank_bal}")
print("=============================")
withdraw_amount = float(input("How much do you wish to withdraw?: R "))


if withdraw_amount <= 0:
    print("Invalid amount. You must withdraw more than R0")
elif withdraw_amount <= bank_bal:
    print(f"Withdrawal successful! Remaining balance: R {bank_bal - withdraw_amount}")
elif withdraw_amount > bank_bal:
    print("Declined. Insufficient funds")
