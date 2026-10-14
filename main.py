from sjf_package.sjf_non_preemptive import sjf_non_preemptive
from sjf_package.sjf_preemptive import sjf_preemptive
from sjf_package.charts import compare_modes, draw_gantt


DEFAULT_PRIORITY = 1
DEFAULT_CONTEXT_SWITCH = 0
DEFAULT_PROCESS_COUNT = 3
DEFAULT_AT = [0, 2, 4]
DEFAULT_BT = [5, 3, 7]


def read_non_negative_integer(prompt, default=None):
    while True:
        try:
            raw_value = input(prompt)
            if raw_value.strip() == "":
                if default is not None:
                    print(f"Input unavailable; using default {default}.")
                    return default
                raise ValueError("Empty input is not allowed.")

            value = int(raw_value)
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except EOFError:
            if default is not None:
                print(f"Input unavailable; using default {default}.")
                return default
            raise
        except KeyboardInterrupt:
            if default is not None:
                print(f"\nInput interrupted; using default {default}.")
                return default
            raise
        except ValueError:
            print("Please enter a valid integer.")


def main():
    print("=" * 40)
    print("       SJF CPU SCHEDULING")
    print("=" * 40)

    print("\nChoose tie-breaking priority:")
    print("1. Order of Arrival")
    print("2. Process ID (P1 before P2, etc.)")

    while True:
        try:
            priority = int(input("Enter your choice (1 or 2): "))
            if priority in (1, 2):
                break
            print("Invalid choice. Enter 1 or 2.")
        except EOFError:
            priority = DEFAULT_PRIORITY
            print(f"\nInput unavailable; using default priority {priority}.")
            break
        except KeyboardInterrupt:
            priority = DEFAULT_PRIORITY
            print(f"\nInput interrupted; using default priority {priority}.")
            break
        except ValueError:
            print("Please enter a valid integer.")

    cs = read_non_negative_integer("\nEnter context-switch overhead: ", default=DEFAULT_CONTEXT_SWITCH)

    while True:
        try:
            n = int(input("\nEnter number of processes: "))
            if n > 0:
                break
            print("Number of processes must be greater than zero.")
        except EOFError:
            n = DEFAULT_PROCESS_COUNT
            print(f"\nInput unavailable; using default process count {n}.")
            break
        except KeyboardInterrupt:
            n = DEFAULT_PROCESS_COUNT
            print(f"\nInput interrupted; using default process count {n}.")
            break
        except ValueError:
            print("Please enter a valid integer.")

    at = []
    bt = []

    for i in range(n):
        print(f"\nProcess P{i + 1}")
        default_at = DEFAULT_AT[i] if i < len(DEFAULT_AT) else 0
        default_bt = DEFAULT_BT[i] if i < len(DEFAULT_BT) else 1
        at.append(read_non_negative_integer("Enter arrival time: ", default=default_at))

        while True:
            burst_time = read_non_negative_integer("Enter burst time: ", default=default_bt)
            if burst_time > 0:
                bt.append(burst_time)
                break
            print("Burst time must be greater than zero.")

    print("\n" + "=" * 40)
    print("SCHEDULING CONFIGURATION")
    print("=" * 40)
    print("Tie-breaker:", "Order of Arrival" if priority == 1 else "Process ID")
    print("Context-switch overhead:", cs)

    non_preemptive_results = sjf_non_preemptive(at, bt, n, priority, cs)
    preemptive_results = sjf_preemptive(at, bt, n, priority, cs)

    draw_gantt(non_preemptive_results["timeline"], "Non-Preemptive SJF")
    draw_gantt(preemptive_results["timeline"], "Preemptive SJF (SRTF)")
    compare_modes(
        non_preemptive_results["average_waiting_time"],
        non_preemptive_results["average_turnaround_time"],
        preemptive_results["average_waiting_time"],
        preemptive_results["average_turnaround_time"],
    )


if __name__ == "__main__":
    main()
