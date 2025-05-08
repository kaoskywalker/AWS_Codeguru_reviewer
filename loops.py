def find_duplicates(data):
    duplicates = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates

sample = ["apple", "banana", "apple", "orange", "banana"]
print(find_duplicates(sample))
