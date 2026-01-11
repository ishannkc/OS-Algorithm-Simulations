# First-Come, First-Served (FCFS) Scheduling Algorithm Implementation


# Sample Input 

# Each process has:
# - pid: Process ID (string)
# - arrival: Arrival Time (int)
# - burst: Burst Time (int)
processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
]


def fcfs_schedule(proc_list):
    """Compute FCFS scheduling results.

    Returns a list of dicts with keys:
    - pid, arrival, burst, waiting, turnaround
    """
    # Sort by arrival time (FCFS order)
    procs = sorted(proc_list, key=lambda p: p["arrival"]) 

    current_time = 0
    results = []

    for p in procs:
        arrival = p["arrival"]
        burst = p["burst"]

        # CPU starts this process when it arrives if idle, otherwise after current_time
        start_time = max(current_time, arrival)
        waiting = start_time - arrival
        finish_time = start_time + burst
        turnaround = finish_time - arrival

        results.append({
            "pid": p["pid"],
            "arrival": arrival,
            "burst": burst,
            "waiting": waiting,
            "turnaround": turnaround,
        })

        current_time = finish_time  # advance CPU time

    return results


def print_fcfs_output(results):
    """Prints the FCFS output table and averages in a clean format."""
    # Compute averages
    n = len(results)
    avg_wait = sum(r["waiting"] for r in results) / n if n else 0.0
    avg_tat = sum(r["turnaround"] for r in results) / n if n else 0.0

    # Table header
    print("Algorithm: FCFS")
    print("-" * 48)
    print("Process | AT | BT | WT | TAT")
    print("-" * 48)

    # Table rows
    for r in results:
        # Align fields for a screenshot-friendly table
        print(f"{r['pid']:<7} | {r['arrival']:>2} | {r['burst']:>2} | {r['waiting']:>2} | {r['turnaround']:>3}")

    # Footer and averages
    print("-" * 48)
    print(f"Average Waiting Time = {avg_wait:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


if __name__ == "__main__":
    # Run FCFS on the sample input and print ONLY the algorithm output
    results = fcfs_schedule(processes)
    print_fcfs_output(results)
