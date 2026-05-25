def main():
    x=input("File Name: ").strip().lower() 
    if '.' not in x:
        print("application/octet-stream")
        return
    ext=x.rsplit('.',1)[1].strip()
    mapping={
        'gif':'image/gif',
        'jpg':'image/jpeg',
        'jpeg':'image/jpeg',
        'png':'image/png',
        'pdf':'application/pdf',
        'txt':'text/plain',
        'zip':'application/zip',
    }
    print(mapping.get(ext,'application/octet-stream'))
if __name__=="__main__":
    main()

