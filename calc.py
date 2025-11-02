#!/usr/bin/env python3
"""
discount_target_solver_all_targets_pretty.py

Computes the highest discount that can be applied on remaining cabins
to reach each revenue target (Low, Base, High), without exceeding 90% occupancy.

User inputs:
- Available cabins per category (A, B, C)
- Current realized (net) revenue
"""

import math
import numpy as np
import pandas as pd

# --- CONSTANT SETTINGS ---
cabins_counts_total = [9, 12, 3]    # total cabins per category (A, B, C)
G = [4100.0, 3200.0, 2500.0]        # gross per cabin A,B,C
port_per_person = 330.0              # fixed per passenger
commission = 0.26                    # commission rate
targets = {"Low": 55000, "Base": 70000, "High": 110000}
max_passengers = 48                  # ship capacity (2 per cabin)
max_occupancy = 0.90                 # cap at 90%

# --- USER INPUT SECTION ---
print("\n=== Ship Discount Target Calculator (All Targets) ===\n")

available_A = int(input("Enter number of AVAILABLE cabins in Category A (max 9): ") or 0)
available_B = int(input("Enter number of AVAILABLE cabins in Category B (max 12): ") or 0)
available_C = int(input("Enter number of AVAILABLE cabins in Category C (max 3): ") or 0)
available = [available_A, available_B, available_C]
available_total = sum(available)

realized_revenue = float(input("Enter currently realized NET revenue (e.g., 25000): ") or 0)

# --- Helper functions ---
def compute_total_net(discount_frac, available_cabins):
    """Compute total net if given discount fraction applied to available cabins."""
    potential_new_passengers = 2 * sum(available_cabins)
    total_possible = int(round(max_passengers * max_occupancy))
    passengers_added = min(potential_new_passengers, total_possible)
    gross_remaining = sum(available_cabins[i] * G[i] for i in range(len(G)))
    # apply discount and commission
    net_from_cabins = gross_remaining * (1 - discount_frac) * (1 - commission)
    port_total = port_per_person * passengers_added
    total_net = realized_revenue + net_from_cabins + port_total
    avg_net_per_person = total_net / (passengers_added if passengers_added > 0 else 1)
    return {
        "discount": discount_frac,
        "total_net": total_net,
        "avg_net_per_person": avg_net_per_person,
        "passengers_added": passengers_added,
        "net_from_cabins": net_from_cabins,
        "port_total": port_total,
        "gross_remaining": gross_remaining
    }

def find_discount_for_target(target_value, available_cabins):
    """Find highest discount fraction that still reaches or exceeds target."""
    grid = np.linspace(0, 1, 2001)  # step 0.05%
    feasible = []
    for D in grid:
        res = compute_total_net(D, available_cabins)
        if res["total_net"] >= target_value:
            feasible.append(res)
    if not feasible:
        return None
    return max(feasible, key=lambda x: x["discount"])

# --- Run for all targets ---
rows = []
print("\n=== Results ===\n")

for tname, tvalue in targets.items():
    result = find_discount_for_target(tvalue, available)
    print(f"{tname} ({tvalue:,.0f})\n")
    if result is None:
        print("❌ Target cannot be reached even with 100% discount (and occupancy capped at 90%).\n")
        rows.append({
            "Target": tname,
            "Target_Value": tvalue,
            "Feasible": False,
            "Highest_Discount_%": None,
            "Total_Net_Revenue": None,
            "Avg_Net_per_Person": None,
            "Passengers_Added": None,
            "Gross_Remaining": None,
            "Net_from_Cabins": None,
            "Port_Total": None,
            "Comment": "Unreachable"
        })
    else:
        print("✅ Feasible target reached:")
        print(f" Highest discount possible: {result['discount']*100:.2f}%")
        print(f" Total net revenue: {result['total_net']:,.2f}")
        print(f" Average net per passenger (approx): {result['avg_net_per_person']:,.2f}")
        print(f" Gross remaining cabin value (before discount): {result['gross_remaining']:,.2f}")
        print(f" Net from cabins after discount/commission: {result['net_from_cabins']:,.2f}")
        print(f" Port charges total: {result['port_total']:,.2f}")
        print(f" Passengers added (max possible): {result['passengers_added']}")
        print(f"With the current revenue of {realized_revenue:,.2f} and by selling {available_total} cabins.\n")

        rows.append({
            "Target": tname,
            "Target_Value": tvalue,
            "Feasible": True,
            "Highest_Discount_%": round(result["discount"]*100,2),
            "Total_Net_Revenue": round(result["total_net"],2),
            "Avg_Net_per_Person": round(result["avg_net_per_person"],2),
            "Passengers_Added": result["passengers_added"],
            "Gross_Remaining": round(result["gross_remaining"],2),
            "Net_from_Cabins": round(result["net_from_cabins"],2),
            "Port_Total": round(result["port_total"],2),
            "Comment": f"With current revenue {realized_revenue:,.2f} and {available_total} cabins."
        })

df = pd.DataFrame(rows)
df.to_csv("discount_target_results.csv", index=False)
print("Results saved to: discount_target_results.csv\n")
