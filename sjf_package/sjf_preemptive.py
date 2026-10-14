def sjf_preemptive(at, bt, n, priority, cs):
    rt = bt.copy()
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n

    time = 0
    completed = 0
    order = []
    last = -1

    def find_shortest_process():
        shortest = -1

        for i in range(n):
            if at[i] > time or rt[i] <= 0:
                continue

            if shortest == -1:
                shortest = i
                continue

            candidate_key = (
                rt[i],
                at[i] if priority == 1 else i,
                i,
            )
            shortest_key = (
                rt[shortest],
                at[shortest] if priority == 1 else shortest,
                shortest,
            )
            if candidate_key < shortest_key:
                shortest = i

        return shortest

    while completed < n:
        shortest = find_shortest_process()

        if shortest == -1:
            time += 1
            last = -1
            continue

        if last != -1 and last != shortest:
            time += cs
            shortest = find_shortest_process()

            if shortest == -1:
                last = -1
                continue

        if last == shortest and order:
            process, start, _ = order[-1]
            order[-1] = (process, start, time + 1)
        else:
            order.append((shortest, time, time + 1))

        rt[shortest] -= 1
        time += 1
        last = shortest

        if rt[shortest] == 0:
            ct[shortest] = time
            tat[shortest] = ct[shortest] - at[shortest]
            wt[shortest] = tat[shortest] - bt[shortest]
            completed += 1

    print("\n" + "=" * 50)
    print("       PREEMPTIVE SJF (SRTF)")
    print("=" * 50)

    print("Execution order:", end=" ")
    for process, _, _ in order:
        print(f"P{process + 1}", end=" ")
    print()

    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(
            f"P{i + 1}\t{at[i]}\t{bt[i]}\t"
            f"{ct[i]}\t{tat[i]}\t{wt[i]}"
        )

    average_waiting_time = round(sum(wt) / n, 2)
    average_turnaround_time = round(sum(tat) / n, 2)
    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)

    return {
        "timeline": [(f"P{process + 1}", start, end) for process, start, end in order],
        "average_waiting_time": average_waiting_time,
        "average_turnaround_time": average_turnaround_time,
    }