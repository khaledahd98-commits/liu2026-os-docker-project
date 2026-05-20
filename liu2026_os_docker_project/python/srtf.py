"""
SRTF CPU Scheduling Simulation
Shortest Remaining Time First is the preemptive version of SJF.
LIU-2026 Operating Systems Project
"""

processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
    {"pid": "P4", "arrival": 3, "burst": 6},
]


def srtf(process_list):
    processes = [p.copy() for p in process_list]
    remaining = {p["pid"]: p["burst"] for p in processes}
    completion = {}
    timeline = []
    time = 0
    finished = 0
    last_pid = None
    segment_start = 0

    while finished < len(processes):
        available = [p for p in processes if p["arrival"] <= time and remaining[p["pid"]] > 0]

        if not available:
            time += 1
            continue

        current = min(available, key=lambda p: remaining[p["pid"]])
        pid = current["pid"]

        if last_pid != pid:
            if last_pid is not None:
                timeline.append((last_pid, segment_start, time))
            segment_start = time
            last_pid = pid

        remaining[pid] -= 1
        time += 1

        if remaining[pid] == 0:
            completion[pid] = time
            finished += 1

    if last_pid is not None:
        timeline.append((last_pid, segment_start, time))

    results = []
    for p in processes:
        pid = p["pid"]
        turnaround = completion[pid] - p["arrival"]
        waiting = turnaround - p["burst"]
        results.append({
            "pid": pid,
            "arrival": p["arrival"],
            "burst": p["burst"],
            "completion": completion[pid],
            "turnaround": turnaround,
            "waiting": waiting,
        })
    return timeline, results


if __name__ == "__main__":
    timeline, results = srtf(processes)
    print("=== SRTF Scheduling ===\n")
    print("Gantt chart:")
    for pid, start, end in timeline:
        print(f"{start} -- {pid} -- {end}")

    print("\nResults:")
    total_waiting = 0
    total_turnaround = 0
    for r in results:
        total_waiting += r["waiting"]
        total_turnaround += r["turnaround"]
        print(r)

    print("\nAverage waiting time:", total_waiting / len(results))
    print("Average turnaround time:", total_turnaround / len(results))
