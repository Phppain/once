"""maybe_the_last_code.py"""

def greet_all(name1, name2, *names):
    print("Hello,", name1)
    print("Hello,", name2)
    if names:
        print(f"Hi, {'\nHi, '.join(i for i in names)}")

if __name__ == "__main__":
    greet_all("Anna", "Boris", "Anna", "Boris", "Anna", "Boris")
