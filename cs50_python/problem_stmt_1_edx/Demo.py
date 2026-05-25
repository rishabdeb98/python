def main():
    x=input("What is the Answer to the Great Question of Life, the universe and everything? ")
    
    x=x.strip().lower().replace("-"," ")

    if x=="42" or x=="forty two":
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()