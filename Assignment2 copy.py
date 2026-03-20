from Assignment2models import FuelDispenser, CarWash

def main():
    # Create a list containing different types of assets
    assets = [
        FuelDispenser(liters_sold=500, price_per_liter=1.45),
        FuelDispenser(liters_sold=320, price_per_liter=1.50),
        CarWash(number_of_washes=15, price_per_wash=12.00),
        CarWash(number_of_washes=8, price_per_wash=20.00)
    ]

    total_revenue = 0

    print("--- Station Revenue Report ---")
    for asset in assets:
        revenue = asset.calculate_revenue()
        total_revenue += revenue
        # type(asset).__name__ gets the class name (e.g., 'CarWash')
        print(f"{type(asset).__name__} generated: ${revenue:,.2f}")

    print("-" * 30)
    print(f"Total Station Revenue: ${total_revenue:,.2f}")

if __name__ == "__main__":
    main()
    