if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    # remove occurencies of the same number
    unique_numbers = set(arr)
    # find the max number
    max_number = max(unique_numbers)
    # pop the max no inorder to find the runners_up
    unique_numbers.remove(max_number)
    runners_up = max(unique_numbers)
    print(runners_up)
