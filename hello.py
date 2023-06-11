def hello(f):
    return f"Hello {f}"

def goodbye(f):
    print("Please to meet you.")
    return f"Goodbye {f}"

def main():
    user = input("Name: ")

    print(hello(user))
    print(goodbye(user))

if __name__ == "__main__":
    main()