"""Minimal demonstration of running work on multiple threads.

Threads let a program run several streams of work concurrently within one
process, sharing memory. Here each thread just prints a message.
"""

import threading


def worker(number):
    print(f"Message from thread {number}")


def main(thread_count=5):
    threads = []
    for n in range(1, thread_count + 1):
        # Pass the function and its args to Thread; do NOT call it yourself
        # (target=worker, args=(n,)) — calling worker(n) here would run it on
        # the main thread instead of starting a new one.
        thread = threading.Thread(target=worker, args=(n,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
