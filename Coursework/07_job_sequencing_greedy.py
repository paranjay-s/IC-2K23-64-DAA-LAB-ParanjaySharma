"""
Design and Analysis of Algorithms - Coursework Task 7
Title: Job Sequencing with Deadlines using Greedy Strategy

Algorithmic Paradigm: Greedy Strategy
Greedy Strategy:
    1. Sort all jobs in descending order of their profit.
    2. For each job, check if a time slot is available on or before its deadline.
    3. Greedily assign the job to the latest possible free slot to leave earlier
       slots open for other jobs with tighter deadlines.

Time Complexity:
    - Sorting: O(n log n)
    - Slot allocation: O(n * D), where D = max(deadline)
    - Overall: O(n log n + n * D)  [can be O(n log n) with DSU]
Space Complexity: O(D) for the time slot array
"""

class Job:
    def __init__(self, job_id: str, deadline: int, profit: int):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"{self.job_id}(Deadline={self.deadline}, Profit={self.profit})"


def job_sequencing(jobs: list):
    """
    Schedules jobs to maximize total profit within deadlines.
    
    Returns:
        tuple: (scheduled_jobs_sequence, total_profit, slot_schedule)
    """
    # 1. Sort jobs descending by profit
    sorted_jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)

    # 2. Find max deadline to size the time slots
    max_deadline = max(j.deadline for j in jobs) if jobs else 0

    # Slots from 1 to max_deadline (0-indexed array of size max_deadline + 1)
    slots = [None] * (max_deadline + 1)
    total_profit = 0
    scheduled_count = 0

    # 3. Greedily schedule each job in latest available slot <= deadline
    for job in sorted_jobs:
        # Search backwards from min(max_deadline, job.deadline) down to 1
        for slot in range(min(max_deadline, job.deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job
                total_profit += job.profit
                scheduled_count += 1
                break

    # Extract sequence of scheduled jobs
    schedule = [(slot, slots[slot]) for slot in range(1, max_deadline + 1) if slots[slot] is not None]
    job_sequence = [job.job_id for _, job in schedule]

    return job_sequence, total_profit, slots


def main():
    print("=" * 65)
    print(" TASK 7: JOB SEQUENCING WITH DEADLINES (GREEDY STRATEGY) ")
    print("=" * 65)

    # Sample jobs dataset
    job_pool = [
        Job("J1", deadline=2, profit=100),
        Job("J2", deadline=1, profit=19),
        Job("J3", deadline=2, profit=27),
        Job("J4", deadline=1, profit=25),
        Job("J5", deadline=3, profit=15),
    ]

    print("Available Jobs:")
    print(f"{'Job ID':<8} | {'Deadline':<10} | {'Profit':<10}")
    print("-" * 35)
    for j in job_pool:
        print(f"{j.job_id:<8} | {j.deadline:<10} | {j.profit:<10}")

    job_seq, total_profit, slots = job_sequencing(job_pool)

    print("\nOptimal Slot Allocations:")
    print(f"{'Time Slot':<12} | {'Assigned Job':<14} | {'Profit':<10}")
    print("-" * 42)
    for slot_idx in range(1, len(slots)):
        job = slots[slot_idx]
        if job is not None:
            print(f"Slot {slot_idx:<7} | {job.job_id:<14} | {job.profit:<10}")
        else:
            print(f"Slot {slot_idx:<7} | {'[EMPTY]':<14} | {'0':<10}")

    print("-" * 42)
    print(f"Optimal Job Execution Sequence: {' -> '.join(job_seq)}")
    print(f"Maximum Total Profit: {total_profit}")
    print("=" * 65)


if __name__ == "__main__":
    main()

