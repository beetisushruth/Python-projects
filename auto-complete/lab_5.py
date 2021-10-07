def prefix_matches(word, prefix):
    if len(word) < len(prefix):
        return False
    for index, char in enumerate(prefix):
        if word[index] != prefix[index]:
            return False
    return True


def findLastIndex(words, prefix, start_index):
    index = -1
    for i in range(start_index, len(words)):
        word = words[i]
        if prefix_matches(word, prefix):
            index = i
        else:
            break
    return index


def find_start_index(prefix, words):
    for i, word in enumerate(words):
        if prefix_matches(word, prefix):
            return i
    return -1


def find_start_bs(prefix, words):
    left = 0
    right = len(words) - 1
    while left < right:
        mid = (left + right) // 2
        if prefix_matches(words[mid], prefix):
            right = mid
        elif words[mid] < prefix:
            left = mid + 1
        else:
            right = mid - 1
    return left if prefix_matches(words[left], prefix) else -1


def ask_input(words):
    print("Welcome to Auto-Complete")
    sentence = "Enter a prefix to search for: "
    input_text = input(sentence)
    while input_text != "<QUIT>":
        print("Your input", input_text)
        prefix = input_text
        start_index = find_start_bs(prefix, words)
        print(start_index)
        print("No match" if start_index == -1 else words[start_index])
        input_text = input(sentence)
    print("Exiting Auto-Complete! GoodBye!")


def main():
    words = ['aa', 'aaa', 'b', 'ba', 'bab', 'bba', 'bbb', 'bc', 'ca', 'cc']
    ask_input(words)


if __name__ == "__main__":
    main()
