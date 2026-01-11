# CPU Scheduling Simulator (Python)

A beginner-friendly CPU Scheduling Simulator implemented in Python for the Labwork of Operating Systems coursework

## Implemented Algorithms
- FCFS (First Come First Serve): `Task1/fcfs.py`
- SJF (Shortest Job First, Non-Preemptive): `Task1/sjf.py`
- SRTF (Shortest Remaining Time First, Preemptive SJF): `Task1/srtf.py`
- Priority (Non-Preemptive, lower number = higher priority): `Task1/priority.py`
- Round Robin (with Time Quantum set inside file): `Task1/round_robin.py`

## How to Run
Each algorithm is a separate file with its own sample input at the top. From the repository root, run:

```bash
python Task1/fcfs.py
python Task1/sjf.py
python Task1/srtf.py
python Task1/priority.py
python Task1/round_robin.py
```

Or from inside the Task1 folder:

```bash
python fcfs.py
python sjf.py
python srtf.py
python priority.py
python round_robin.py
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
