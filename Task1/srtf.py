# Shortest Remaining Time First (SRTF) Scheduling Algorithm Implementation
# preemptive version of Shortest Job First (SJF)
# Sample Input 

# Each process has:
# - pid: Process ID (string)
# - arrival: Arrival Time (int)
# - burst: Burst Time (int)
processes = [
    {"pid": "P1", "arrival": 0, "burst": 8},
    {"pid": "P2", "arrival": 1, "burst": 4},
    {"pid": "P3", "arrival": 2, "burst": 9},
    {"pid": "P4", "arrival": 3, "burst": 5},
]


def srtf_schedule(proc_list):
   
    # Prepare structures
    procs = [
        {"pid": p["pid"], "arrival": p["arrival"], "burst": p["burst"], "remaining": p["burst"]}
        for p in sorted(proc_list, key=lambda x: x["arrival"])  # time-ordered
    ]

    time = 0
    completed = 0
    n = len(procs)
    completion_time = {p["pid"]: None for p in procs}

    while completed < n:
        # Get available processes
        available = [p for p in procs if p["arrival"] <= time and p["remaining"] > 0]

        if not available:
            # If none available, jump to next arrival and continue
            next_arrival = min([p["arrival"] for p in procs if p["remaining"] > 0])
            time = max(time, next_arrival)
            continue

        # Choose process with shortest remaining time; tie-break by arrival then pid
        current = min(available, key=lambda x: (x["remaining"], x["arrival"], x["pid"]))

        # Run for one time unit
        current["remaining"] -= 1
        time += 1

        # If finished, record completion
        if current["remaining"] == 0:
            completion_time[current["pid"]] = time
            completed += 1

    # Build results and compute WT/TAT from completion times
    results = []
    for p in procs:
        finish = completion_time[p["pid"]]
        tat = finish - p["arrival"]
        wt = tat - p["burst"]
        results.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "waiting": wt,
            "turnaround": tat,
        })

    # Order results by original arrival, then pid for a neat table
    results.sort(key=lambda r: (r["arrival"], r["pid"]))
    return results


def print_srtf_output(results):

    n = len(results)
    avg_wait = sum(r["waiting"] for r in results) / n if n else 0.0
    avg_tat = sum(r["turnaround"] for r in results) / n if n else 0.0

    print("Algorithm: SRTF")
    print("-" * 48)
    print("Process | AT | BT | WT | TAT")
    print("-" * 48)

    for r in results:
        print(f"{r['pid']:<7} | {r['arrival']:>2} | {r['burst']:>2} | {r['waiting']:>2} | {r['turnaround']:>3}")

    print("-" * 48)
    print(f"Average Waiting Time = {avg_wait:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


if __name__ == "__main__":
    results = srtf_schedule(processes)
    print_srtf_output(results)
