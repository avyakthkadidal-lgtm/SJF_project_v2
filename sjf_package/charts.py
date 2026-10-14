import matplotlib.pyplot as plt


def draw_gantt(timeline, title, save_as=None):
    """
    timeline: list of (pid, start, end) segments
    e.g. ("P1", 0, 7)
    """
    pids = sorted({seg[0] for seg in timeline}, key=lambda s: int(s[1:]))
    row = {pid: i for i, pid in enumerate(pids)}

    fig, ax = plt.subplots(figsize=(9, 3))

    for pid, start, end in timeline:
        ax.broken_barh(
            [(start, end - start)],
            (row[pid] - 0.4, 0.8),
            edgecolor="black"
        )
        ax.text(
            (start + end) / 2,
            row[pid],
            pid,
            ha="center",
            va="center"
        )

    ax.set_yticks(range(len(pids)))
    ax.set_yticklabels(pids)
    ax.set_xlabel("Time")
    ax.set_title(title)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    plt.tight_layout()

    if save_as:
        plt.savefig(save_as)

    plt.show()


def compare_modes(np_wt, np_tat, p_wt, p_tat, save_as=None):
    labels = ["Avg Waiting Time", "Avg Turnaround Time"]
    x = range(len(labels))

    plt.figure()

    plt.bar(
        [i - 0.2 for i in x],
        [np_wt, np_tat],
        width=0.4,
        label="Non-preemptive"
    )

    plt.bar(
        [i + 0.2 for i in x],
        [p_wt, p_tat],
        width=0.4,
        label="Preemptive"
    )

    plt.xticks(list(x), labels)
    plt.ylabel("Time units")
    plt.title("SJF: Preemptive vs Non-Preemptive")
    plt.legend()

    if save_as:
        plt.savefig(save_as)

    plt.show()
