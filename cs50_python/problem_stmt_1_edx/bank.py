def main():
    greetings=input("Greetings: ").lower().strip()
    if greetings.startswith("Hello"):
        print("$0")
    elif greetings.startswith("h"):
        print("$20")
    else:
        print("$100")
if __name__=="__main__":
            main()