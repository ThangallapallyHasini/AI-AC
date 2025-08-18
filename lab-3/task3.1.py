
from typing import List, Tuple, Optional

# Default slabs: (cap, rate). Use float('inf') for the last open slab.
DEFAULT_SLABS: List[Tuple[float, float]] = [
    (100, 1.5),
    (100, 2.5),
    (300, 4.0),
    (float("inf"), 6.0),
]

def calculate_power_bill(
    units: int,
    slabs: Optional[List[Tuple[float, float]]] = None,
    fixed_charge: float = 0.0,
) -> float:
    if units < 0:
        raise ValueError("Units must be non-negative")
    slabs_to_use = slabs if slabs is not None else DEFAULT_SLABS
    remaining, total = units, 0.0
    for cap, rate in slabs_to_use:
        if remaining <= 0:
            break
        used = remaining if cap == float("inf") else min(remaining, int(cap))
        total += used * rate
        remaining -= used
    return total + float(fixed_charge)

if __name__ == "__main__":
    try:
        u = int(input("Enter units: "))
        print(f"Total bill: {calculate_power_bill(u):.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}")