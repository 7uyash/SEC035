def main():
    try:
        number = int(input("Enter a positive integer: "))
        if number < 1:
            print("Please enter a positive integer.")
            return
        total_sum = sum(range(1, number + 1))
        print(f"The sum of numbers from 1 to {number} is: {total_sum}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

