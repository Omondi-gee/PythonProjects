#Movie tickets for PG-13
ages = [10, 15, 12, 18, 8, 14]
for age in ages:
    if age < 13:
        continue
    print (f"Allowed : Age {age}")
