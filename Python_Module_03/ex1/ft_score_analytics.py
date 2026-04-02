#!/usr/bin/python3.10

import sys


def score_analytics():
    print("=== Player Score Analytics ===")
    scores = []
    if len(sys.argv) > 1:
        i = 1
        while i < len(sys.argv):
            try:
                score = int(sys.argv[i])
                scores = scores + [score]
            except ValueError as e:
                print(e)
            i += 1
        if scores:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(sys.argv) - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / (len(sys.argv) - 1)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}\n")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")


if __name__ == "__main__":
    score_analytics()
