def hello(f):
    return f"Hello {f}"

def main():
    user = input("Name: ")
    print(hello(user))

if __name__ == "__main__":
    main()