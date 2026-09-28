from modules.algorithms import (
    gcd, fibonacci, factorial, is_prime, prime_factors,
    reverse_number, decimal_to_binary, character_to_number
)
from modules.array_tools import (
    reverse_array, count_values, find_max, remove_duplicates,
    kth_smallest, partition_array
)
from modules.search_sort import linear_search, binary_search, bubble_sort
from modules.quiz import run_quiz


def algorithm_lab():
    while True:
        print("\n=== FUNDAMENTAL ALGORITHM LAB ===")
        print("1. GCD")
        print("2. Factorial")
        print("3. Fibonacci")
        print("4. Prime Check")
        print("5. Prime Factors")
        print("6. Reverse Number")
        print("7. Decimal to Binary")
        print("8. Character to Number")
        print("9. Back")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                a, b = map(int, input("Enter two integers: ").split())
                print("GCD:", gcd(a, b))
            elif choice == "2":
                print("Factorial:", factorial(int(input("Enter n: "))))
            elif choice == "3":
                print("Fibonacci:", fibonacci(int(input("Enter number of terms: "))))
            elif choice == "4":
                print("Prime" if is_prime(int(input("Enter n: "))) else "Not prime")
            elif choice == "5":
                print("Prime factors:", prime_factors(int(input("Enter n: "))))
            elif choice == "6":
                print("Reversed:", reverse_number(int(input("Enter n: "))))
            elif choice == "7":
                print("Binary:", decimal_to_binary(int(input("Enter decimal number: "))))
            elif choice == "8":
                ch = input("Enter one character: ")
                print("Number:", character_to_number(ch))
            elif choice == "9":
                return
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Input error:", e)


def array_lab():
    while True:
        print("\n=== ARRAY & LIST LAB ===")
        print("1. Reverse array")
        print("2. Count values")
        print("3. Find maximum")
        print("4. Remove duplicates")
        print("5. Kth smallest")
        print("6. Partition around pivot")
        print("7. Search")
        print("8. Sort")
        print("9. Back")
        choice = input("Choose: ").strip()

        try:
            if choice == "9":
                return
            arr = list(map(int, input("Enter integers separated by spaces: ").split()))

            if choice == "1":
                print("Reversed:", reverse_array(arr))
            elif choice == "2":
                print("Counts:", count_values(arr))
            elif choice == "3":
                print("Maximum:", find_max(arr))
            elif choice == "4":
                print("Without duplicates:", remove_duplicates(arr))
            elif choice == "5":
                k = int(input("Enter k (1-based): "))
                print("Kth smallest:", kth_smallest(arr, k))
            elif choice == "6":
                pivot = int(input("Enter pivot: "))
                left, equal, right = partition_array(arr, pivot)
                print("Less:", left)
                print("Equal:", equal)
                print("Greater:", right)
            elif choice == "7":
                target = int(input("Search value: "))
                method = input("linear or binary? ").strip().lower()
                if method == "binary":
                    sorted_arr = sorted(arr)
                    print("Sorted array:", sorted_arr)
                    print("Index:", binary_search(sorted_arr, target))
                else:
                    print("Index:", linear_search(arr, target))
            elif choice == "8":
                print("Bubble sorted:", bubble_sort(arr))
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Input error:", e)


def main():
    while True:
        print("\n" + "=" * 48)
        print("                 ALGOLABS")
        print("     Interactive Algorithm Learning Lab")
        print("=" * 48)
        print("1. Fundamental Algorithm Lab")
        print("2. Array & List Lab")
        print("3. Quiz Lab")
        print("4. Exit")

        choice = input("Choose a module: ").strip()

        if choice == "1":
            algorithm_lab()
        elif choice == "2":
            array_lab()
        elif choice == "3":
            run_quiz()
        elif choice == "4":
            print("Thanks for using AlgoLabs!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
