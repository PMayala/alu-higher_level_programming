#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all = dir(hidden_4)

    for i in range(len(all)):
        if all[i][0] != "_":
            print(f"{all[i]}")
