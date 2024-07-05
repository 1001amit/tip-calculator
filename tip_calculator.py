def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip
    return tip, total_amount

def main():
    print("Welcome to the Tip Calculator!")
    bill_amount = float(input("Enter the bill amount: ₹"))
    tip_percentage = float(input("Enter the tip percentage: "))
    
    tip, total_amount = calculate_tip(bill_amount, tip_percentage)
    
    print(f"\nTip: ₹{tip:.2f}")
    print(f"Total amount to be paid: ₹{total_amount:.2f}")

if __name__ == "__main__":
    main()
