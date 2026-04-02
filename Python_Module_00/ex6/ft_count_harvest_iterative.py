def ft_count_harvest_iterative():
    print(*(f"Day {day}" for day in range
          (1, int(input("Days until harvest: ")) + 1)), "Harvest time!",
          sep="\n")
