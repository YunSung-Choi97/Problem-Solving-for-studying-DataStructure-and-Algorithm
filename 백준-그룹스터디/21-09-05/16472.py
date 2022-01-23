import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

change_idx = [0]
alphabet = [string[0]]

pre_char = string[0]
for i in range(1, len(string)):
    if string[i] != pre_char:
        change_idx.append(i)
        alphabet.append(string[i])
        pre_char = string[i]

end_idx = 0
result = ''
storage = []
for i, start_idx in enumerate(change_idx):
    storage.append(string[start_idx])

    for j in range(i+1, len(change_idx)):

        if j != len(change_idx)-1:
            if alphabet[j] not in storage and len(storage) == N:
                end_idx = change_idx[j]
                if len(result) < len(string[start_idx:end_idx]):
                    result = string[start_idx:end_idx]
                storage = []
                break
            elif alphabet[j] not in storage:
                storage.append(alphabet[j])

        else:
            if alphabet[j] not in storage and len(storage) == N:
                end_idx = change_idx[j]
                if len(result) < len(string[start_idx:end_idx]):
                    result = string[start_idx:end_idx]
                storage = []
                break
            else:
                end_idx = len(string)
                if len(result) < len(string[start_idx:end_idx]):
                    result = string[start_idx:end_idx]

print(result)