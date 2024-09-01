import itertools

def generate(string,length):
    draft_perm = list(itertools.combinations(string,length))
    combinations = []
    for dft in draft_perm:
        permutations = list(itertools.permutations(dft))
        new_combinations = ["".join(p) for p in permutations]
        combinations.extend(new_combinations)
    return combinations

def main():
    word = input("Enter the word: ")
    length = int(input("Enter the length of the password (length should not be learger than word) : "))

    passwd_lst = generate(word, length)

    with open('passwords.txt', 'w') as file:
        for passwd in passwd_lst:
            file.write(passwd + '\n')

    print("The possible password list: ")
    for passwd in passwd_lst:
        print(passwd)

    print(len(passwd_lst))

if __name__ == "__main__":
    main()
