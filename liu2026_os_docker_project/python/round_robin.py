"""
Round Robin CPU Scheduling Simulation
LIU-2026 Operating Systems Project
"""
from collections import deque

processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
    {"pid": "P4", "arrival": 3, "burst": 6},
]
quantum = 2


def round_robin(process_list, q):
    processes = sorted([p.copy() for p in process_list], key=lambda x: x["arrival"])
    remaining = {p["pid"]: p["burst"] for p in processes}
    completion = {}
    timeline = []
    ready = deque()
    time = 0
    i = 0

    while i < len(processes) or ready:
        while i < len(processes) and processes[i]["arrival"] <= time:
            ready.append(processes[i])
            i += 1

        if not ready:
            time = processes[i]["arrival"]
            continue

        current = ready.popleft()
        pid = current["pid"]
        run_time = min(q, remaining[pid])
        start = time
        time += run_time
        remaining[pid] -= run_time
        timeline.append((pid, start, time))

        while i < len(processes) and processes[i]["arrival"] <= time:
            ready.append(processes[i])
            i += 1

        if remaining[pid] > 0:
            ready.append(current)
        else:
            completion[pid] = time

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
    timeline, results = round_robin(processes, quantum)
    print("=== Round Robin Scheduling ===")
    print(f"Quantum = {quantum}\n")
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
