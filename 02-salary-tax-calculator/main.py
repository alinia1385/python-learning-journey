def calculate_tax(salary, has_child):
    
    if salary <= 10_000_000:
        tax = 0
    elif salary <= 25_000_000:
        tax = (salary - 10_000_000) * 0.10
    else:
        
        first_tier_tax = 15_000_000 * 0.10
        second_tier_tax = (salary - 25_000_000) * 0.20
        tax = first_tier_tax + second_tier_tax

   
    if has_child:
        tax -= 500_000

    
    return max(0, tax)

def main():
    try:
        salary = float(input("Enter monthly salary: "))
        
        child_input = input("Does the employee have a child? (yes/no): ").strip().lower()
        has_child = child_input == "yes"

        tax = calculate_tax(salary, has_child)
        net_salary = salary - tax

        print("\n--- Salary Breakdown ---")
        print(f"Gross Salary: {salary:,.0f}") 
        print(f"Tax Deducted: {tax:,.0f}")
        print(f"Net Salary:   {net_salary:,.0f}")
        print("------------------------")

    except ValueError:
        print("Error: Please enter a valid number for salary.")

if __name__ == "__main__":
    main()
