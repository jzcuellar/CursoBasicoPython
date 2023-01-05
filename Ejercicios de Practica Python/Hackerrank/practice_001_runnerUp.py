# Get the Second best runnerUp record

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

records = list(arr)

records_uniques = []

for i in records:
    if i in records_uniques:
        continue
    else:
        records_uniques.append(i)

records_uniques = sorted(records_uniques, reverse=True)
print(records_uniques[1])

