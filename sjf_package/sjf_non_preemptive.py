def sjf_non_preemptive(at, bt, n, priority, cs):
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n
    done = [False] * n

    time = 0
    count = 0
    order = []
    last = -1

    while count < n:
        shortest = -1

        for i in range(n):
            if at[i] <= time and not done[i]:
                if shortest == -1:
                    shortest = i
                    continue

                candidate_key = (
                    bt[i],
                    at[i] if priority == 1 else i,
                    i,
                )
                shortest_key = (
                    bt[shortest],
                    at[shortest] if priority == 1 else shortest,
                    shortest,
                )
                if candidate_key < shortest_key:
                    shortest = i

        if shortest == -1:
            time += 1
            last = -1
            continue

        if last != -1 and last != shortest:
            time += cs

        start = time
        time += bt[shortest]

        ct[shortest] = time
        tat[shortest] = ct[shortest] - at[shortest]
        wt[shortest] = tat[shortest] - bt[shortest]
        done[shortest] = True
        count += 1

        order.append((shortest, start, time))
        last = shortest

    print("\n" + "=" * 50)
    print("       NON-PREEMPTIVE SJF")
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