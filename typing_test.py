#!/usr/bin/env python3
"""typing_test - Terminal typing speed test."""
import sys, time, random

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick daft zebras jump.",
    "The five boxing wizards jump quickly.",
    "Sphinx of black quartz, judge my vow.",
    "Two driven jocks help fax my big quiz.",
    "The job requires extra pluck and zeal from every young wage earner.",
    "A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent.",
]

def test(sentences=3):
    targets = random.sample(SENTENCES, min(sentences, len(SENTENCES)))
    print("Type the following text as fast as you can:\n")
    total_chars = 0; total_errors = 0
    start = time.time()
    for target in targets:
        print(f"  \033[33m{target}\033[0m")
        typed = input("  > ")
        errors = sum(1 for a,b in zip(target, typed) if a != b) + abs(len(target)-len(typed))
        total_chars += len(target)
        total_errors += errors
    elapsed = time.time() - start
    wpm = (total_chars / 5) / (elapsed / 60)
    accuracy = max(0, (total_chars - total_errors) / total_chars * 100)
    print(f"\n  ⌨️  {wpm:.0f} WPM | {accuracy:.1f}% accuracy | {elapsed:.1f}s")

def main():
    args = sys.argv[1:]
    n = int(args[0]) if args and args[0].isdigit() else 3
    test(n)

if __name__ == '__main__': main()
