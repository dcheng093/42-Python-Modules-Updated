def ft_count_harvest_recursive(days: int = 1, n: int = False):
    n = n or int(input("Days until harvest: "))
    print(f"Day {days}" if days <= n else
          "Harvest time!") or (days <= n and ft_count_harvest_recursive(days +
                                                                        1, n))
