# Operating Systems Lab — CPU Scheduling, Page Replacement and Disk Scheduling(Python)

## Task 1 — CPU Scheduling
- FCFS (First Come First Serve): `Task1/fcfs.py`
- SJF (Shortest Job First, Non-Preemptive): `Task1/sjf.py`
- SRTF (Shortest Remaining Time First, Preemptive SJF): `Task1/srtf.py`
- Priority (Non-Preemptive, lower number = higher priority): `Task1/priority.py`
- Round Robin (with Time Quantum set inside file): `Task1/round_robin.py`

## Task 3 — Page Replacement
- FIFO (First-In First-Out): `Task3/fifo.py`
- OPT (Optimal): `Task3/opt.py`
- LRU (Least Recently Used): `Task3/lru.py`

## Task 4 — Disk Scheduling
- FCFS (First Come First Serve): `Task4/fcfs_disk.py`
- SSTF (Shortest Seek Time First): `Task4/sstf.py`
- SCAN (Elevator): `Task4/scan.py`
- C-SCAN (Circular SCAN): `Task4/cscan.py`
- LOOK: `Task4/look.py`
- C-LOOK (Circular LOOK): `Task4/clook.py`

## How to Run
Each algorithm is a separate file with its own sample input at the top. From the repository root, run:

```bash
python Task1/fcfs.py
python Task1/sjf.py
python Task1/srtf.py
python Task1/priority.py
python Task1/round_robin.py
python Task3/fifo.py
python Task3/opt.py
python Task3/lru.py
python Task4/fcfs_disk.py
python Task4/sstf.py
python Task4/scan.py
python Task4/cscan.py
python Task4/look.py
python Task4/clook.py
```

Or from inside the Task1 folder:

```bash
python fcfs.py
python sjf.py
python srtf.py
python priority.py
python round_robin.py
```

From inside Task3:

```bash
python fifo.py
python opt.py
python lru.py
```

From inside Task4:

```bash
python fcfs_disk.py
python sstf.py
python scan.py
python cscan.py
python look.py
python clook.py
```

## Output Format
Each algorithm prints:
- A clearly labeled algorithm header
- A table with Process ID, Arrival Time (AT), Burst Time (BT), Waiting Time (WT), Turnaround Time (TAT)
- Average Waiting Time and Average Turnaround Time

Priority value and Time Quantum are included only when applicable.

## Notes for Submission
- Each `.py` file contains its own sample input and prints only that algorithm’s output.
- Output tables are compact and fit in 1–2 screenshots.
- Code is clean and readable for academic review and GitHub hosting.
