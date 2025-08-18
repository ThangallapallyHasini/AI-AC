from typing import List, Tuple
SLABS: List[Tuple[float, float]] = [
    (100, 1.5),
    (100, 2.5),
    (300, 4.0),
    (float("inf"), 6.0),
]

FIXED_CHARGE = 0.0  
def calculate_power_bill(units: int) -> Tuple[float, List[Tuple[str, float]]]:
    if units < 0:
        raise ValueError("Units must be non-negative")

    remaining_units = units
    total_charge = 0.0
    breakdown: List[Tuple[str, float]] = []

    for slab_units, rate in SLABS:
        if remaining_units <= 0:
            break

        if slab_units == float("inf"):
            used_in_slab = remaining_units
        else:
            used_in_slab = min(remaining_units, int(slab_units))

        charge = used_in_slab * rate
        breakdown.append((f"{used_in_slab} units @ {rate:.2f}", charge))
        total_charge += charge
        remaining_units -= used_in_slab

    if FIXED_CHARGE:
        breakdown.append(("Fixed charge", FIXED_CHARGE))
        total_charge += FIXED_CHARGE

    return total_charge, breakdown


def main() -> None:
    try:
        raw = input("Enter units consumed (non-negative integer): ")
        units = int(raw)
        if units < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative whole number.")
        return

    total, details = calculate_power_bill(units)

    print("\nBill breakdown:")
    for label, amount in details:
        print(f"- {label}: {amount:.2f}")
    print(f"Total bill for {units} units: {total:.2f}")


if __name__ == "__main__":
    main()