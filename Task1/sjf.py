# Shortest Job First (SJF) Scheduling Algorithm Implementation
# non-preemptive version
# Sample Input 
# Each process has:
# - pid: Process ID (string)
# - arrival: Arrival Time (int)
# - burst: Burst Time (int)
processes = [
    {"pid": "P1", "arrival": 0, "burst": 6},
    {"pid": "P2", "arrival": 1, "burst": 8},
    {"pid": "P3", "arrival": 2, "burst": 7},
    {"pid": "P4", "arrival": 3, "burst": 3},
]


def sjf_schedule(proc_list):
  
    # Sort by arrival to process events in time order
    remaining = proc_list[:]
    remaining.sort(key=lambda p: p["arrival"])  # stable order by arrival

    time = 0
    results = []

    while remaining:
        # Collect processes that have arrived by current time
        available = [p for p in remaining if p["arrival"] <= time]

        if not available:
            # No process available; jump to next arrival time
            time = remaining[0]["arrival"]
            available = [p for p in remaining if p["arrival"] <= time]

        # Pick the process with shortest burst; tie-break by arrival then pid
        p = min(
            available,
            key=lambda x: (x["burst"], x["arrival"], x["pid"]) 
        )

        start_time = time
        waiting = start_time - p["arrival"]
        finish_time = start_time + p["burst"]
        turnaround = finish_time - p["arrival"]

        results.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "waiting": waiting,
            "turnaround": turnaround,
        })

        # Advance time and remove the process from remaining
        time = finish_time
        remaining.remove(p)

    return results


def print_sjf_output(results):

    n = len(results)
    avg_wait = sum(r["waiting"] for r in results) / n if n else 0.0
    avg_tat = sum(r["turnaround"] for r in results) / n if n else 0.0

    print("Algorithm: SJF")
    print("-" * 48)
    print("Process | AT | BT | WT | TAT")
    print("-" * 48)

    for r in results:
        print(f"{r['pid']:<7} | {r['arrival']:>2} | {r['burst']:>2} | {r['waiting']:>2} | {r['turnaround']:>3}")

    print("-" * 48)
    print(f"Average Waiting Time = {avg_wait:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


if __name__ == "__main__":
    results = sjf_schedule(processes)
    print_sjf_output(results)
