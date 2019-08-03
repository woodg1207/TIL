# bubble sort
def bubblesort(samples):
    for i in range(1, len(samples)):
        for j in range(len(samples)-i):
            if samples[j] > samples[j+1]:
                samples[j], samples[j+1] = samples[j+1], samples[j]
    return samples

print(bubblesort([55, 7, 78, 12, 42]))


