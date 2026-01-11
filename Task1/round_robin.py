# Round Robin Scheduling Algorithm Implementation

# Sample Input
# Each process has:
# - pid: Process ID (string)
# - arrival: Arrival Time (int)
# - burst: Burst Time (int)
# Time Quantum provided separately
processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 4},
    {"pid": "P3", "arrival": 2, "burst": 2},
]

time_quantum = 2  # edit as needed


def round_robin_schedule(proc_list, tq):

    # Sort by arrival to manage incoming processes
    procs = sorted(proc_list, key=lambda p: p["arrival"])  # stable order

    # Track remaining time and completion
    remaining = {p["pid"]: p["burst"] for p in procs}
    completion = {p["pid"]: None for p in procs}

    time = 0
    i = 0  # index into procs for arrivals
    queue = []  # ready queue of pids

    # Initialize queue with any processes that arrive at time 0
    while i < len(procs) and procs[i]["arrival"] <= time:
        queue.append(procs[i]["pid"])
        i += 1

    # Main loop until all complete
    while any(remaining[pid] > 0 for pid in remaining):
        if not queue:
            # If queue empty, jump to next arrival and enqueue it
            next_arrival = procs[i]["arrival"] if i < len(procs) else None
            if next_arrival is None:
                break  # safety
            time = max(time, next_arrival)
            queue.append(procs[i]["pid"]) 
            i += 1
            continue

        pid = queue.pop(0)
        # Find its full process record
        p = next(pp for pp in procs if pp["pid"] == pid)

        # Run for up to tq or remaining time
        run_time = min(tq, remaining[pid])
        prev_time = time
        time += run_time
        remaining[pid] -= run_time

        # Enqueue newly arrived processes that came during this run
        while i < len(procs) and procs[i]["arrival"] <= time:
            queue.append(procs[i]["pid"]) 
            i += 1

        # If current process not finished, re-enqueue it
        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

    # Build results; WT = TAT - BT, TAT = completion - arrival
    results = []
    for p in procs:
        finish = completion[p["pid"]]
        tat = finish - p["arrival"]
        wt = tat - p["burst"]
        results.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "waiting": wt,
            "turnaround": tat,
        })

    # Sort results by arrival then pid for readability
    results.sort(key=lambda r: (r["arrival"], r["pid"]))
    return results


def print_rr_output(results, tq):
    """Prints the Round Robin output table and averages in a clean format."""
    n = len(results)
    avg_wait = sum(r["waiting"] for r in results) / n if n else 0.0
    avg_tat = sum(r["turnaround"] for r in results) / n if n else 0.0

    print(f"Algorithm: Round Robin (TQ = {tq})")
    print("-" * 48)
    print("Process | AT | BT | WT | TAT")
    print("-" * 48)

    for r in results:
        print(f"{r['pid']:<7} | {r['arrival']:>2} | {r['burst']:>2} | {r['waiting']:>2} | {r['turnaround']:>3}")

    print("-" * 48)
    print(f"Average Waiting Time = {avg_wait:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


if __name__ == "__main__":
    results = round_robin_schedule(processes, time_quantum)
    print_rr_output(results, time_quantum)
