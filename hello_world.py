def hello(to):
    return f"Hello {to}"

def main():
    user = input("Name: ")
    print(hello(user))

if __name__ == "__main__":
    main()