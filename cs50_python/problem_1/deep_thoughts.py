def main():
    #prompt user for file name
    file_name=input("File name: ").strip().lower()

    #Dictionary mapping extensions to media types
    media_types={
        ".gif": "image/gif",
        ".jpg":"image/jpeg",
        ".jpeg":"image/jpeg",
        ".png":"image/png",
        ".pdf":"application/pdf",
        ".txt":"text/plain",
        ".zip":"application/zip",
    }
    for ext,media in media_types.items():
        if file_name.endswith(ext):
            print(media)
            return

    print("application/octet-stream")

if __name__ == "__main__":
    main()
