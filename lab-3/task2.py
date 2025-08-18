"""
Power bill calculator using configurable slab rates.

Edit the `SLABS` list to match your tariff. Each tuple is (units_in_slab, rate_per_unit).
Use float('inf') for the last open-ended slab.
"""

from typing import List, Tuple

# Example slab configuration:
# - First 100 units @ 1.5
# - Next 100 units @ 2.5
# - Next 300 units @ 4.0
# - Remaining units @ 6.0
SLABS: List[Tuple[float, float]] = [
    (100, 1.5),
    (100, 2.5),
    (300, 4.0),
    (float("inf"), 6.0),
]

FIXED_CHARGE = 0.0  # Set a fixed charge if applicable (e.g., 50.0)


def calculate_power_bill(units: int) -> Tuple[float, List[Tuple[str, float]]]:
    """Return total bill and a breakdown for the given units using SLABS.

    Breakdown items are (label, charge) pairs, where label describes the slab usage.
    """
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