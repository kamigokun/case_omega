#!/usr/bin/env python3
"""
timeline_correlation.py — merges multiple forensic log sources (auth logs,
file-activity logs, browser history) into a single chronological timeline
CSV, for building the attack timeline required by Sub-Problem 4.

This mirrors what a tool like log2timeline/plaso does at a larger scale:
normalize timestamps across sources, tag each event with its origin, and
sort into one super-timeline an investigator can read top to bottom.

Usage:
    python3 timeline_correlation.py --out attack_timeline.csv \
        sample-logs/auth_log.csv sample-logs/file_activity_log.csv sample-logs/browser_history.csv
"""
import argparse
import csv
from datetime import datetime


def load_csv(path, source_label):
    events = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            ts = row.get("timestamp")
            try:
                dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
            except (ValueError, TypeError):
                continue
            summary_fields = {k: v for k, v in row.items() if k != "timestamp"}
            summary = "; ".join(f"{k}={v}" for k, v in summary_fields.items() if v)
            events.append({
                "timestamp_utc": dt.isoformat() + "Z",
                "source": source_label,
                "details": summary,
            })
    return events


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("logs", nargs="+", help="CSV log files to merge")
    ap.add_argument("--out", default="attack_timeline.csv")
    args = ap.parse_args()

    all_events = []
    for path in args.logs:
        label = path.split("/")[-1].replace(".csv", "")
        all_events.extend(load_csv(path, label))

    all_events.sort(key=lambda e: e["timestamp_utc"])

    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp_utc", "source", "details"])
        writer.writeheader()
        writer.writerows(all_events)

    print(f"Wrote {len(all_events)} correlated events to {args.out}")
    print("\nPreview:")
    for e in all_events[:10]:
        print(f"  {e['timestamp_utc']}  [{e['source']}]  {e['details']}")


if __name__ == "__main__":
    main()