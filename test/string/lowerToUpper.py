def main():
    user_input = input("Enter a string: ")
    print("Characters in the string:")
    for char in user_input:
        print(char)
    upper_case = user_input.upper()
    print(f"The string in uppercase: {upper_case}")
    upper_case = user_input.lower()
    print(f"The string in uppercase: {upper_case}")

if __name__ == "__main__":
    main()
