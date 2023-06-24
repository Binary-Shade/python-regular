import requests


def main():
    url="https://www.geeksforgeeks.org/"
    response=requests.get(url)

    if response.status_code == 200:
        print("request successfull")
        print("content")
        with open("file.txt","w") as file:
            file.write(response.text)

    else:
        print("request failed with status code"+response.status_code)

if __name__=="__main__":
    main()