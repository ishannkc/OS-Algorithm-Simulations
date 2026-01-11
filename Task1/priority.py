# Priority Scheduling Algorithm (Non-Preemptive)

# Sample Input 

# Each process has:
# - pid: Process ID (string)
# - arrival: Arrival Time (int)
# - burst: Burst Time (int)
# - priority: Priority value (int) — lower is higher priority
processes = [
    {"pid": "P1", "arrival": 0, "burst": 10, "priority": 3},
    {"pid": "P2", "arrival": 2, "burst":  1, "priority": 1},
    {"pid": "P3", "arrival": 3, "burst":  2, "priority": 4},
    {"pid": "P4", "arrival": 5, "burst":  1, "priority": 2},
]


def priority_schedule(proc_list):

    remaining = proc_list[:]
    remaining.sort(key=lambda p: p["arrival"])  # time order

    time = 0
    results = []

    while remaining:
        available = [p for p in remaining if p["arrival"] <= time]

        if not available:
            time = remaining[0]["arrival"]
            available = [p for p in remaining if p["arrival"] <= time]

        # Choose by priority (lower is better), then burst, arrival, pid
        p = min(
            available,
            key=lambda x: (x["priority"], x["burst"], x["arrival"], x["pid"]) 
        )

        start_time = time
        waiting = start_time - p["arrival"]
        finish_time = start_time + p["burst"]
        turnaround = finish_time - p["arrival"]

        results.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "priority": p["priority"],
            "waiting": waiting,
            "turnaround": turnaround,
        })

        time = finish_time
        remaining.remove(p)

    return results


def print_priority_output(results):

    n = len(results)
    avg_wait = sum(r["waiting"] for r in results) / n if n else 0.0
    avg_tat = sum(r["turnaround"] for r in results) / n if n else 0.0

    print("Algorithm: Priority (Non-Preemptive)")
    print("-" * 58)
    print("Process | AT | BT | PR | WT | TAT")
    print("-" * 58)

    for r in results:
        print(f"{r['pid']:<7} | {r['arrival']:>2} | {r['burst']:>2} | {r['priority']:>2} | {r['waiting']:>2} | {r['turnaround']:>3}")

    print("-" * 58)
    print(f"Average Waiting Time = {avg_wait:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


if __name__ == "__main__":
    results = priority_schedule(processes)
    print_priority_output(results)
