import urllib.request
import urllib

def urlreader():
    try:
        with urllib.request.urlopen("http://www.timingindia.com/certificate/MzA4NjpUMTUzNzo1NzE6JkkmNzY=") as url:
            s = url.read()
            print(s)
    except Exception as e:
        print("Common Exception: Not able to open the URL",e)






def main():
    url = "https://www.americanexpress.com/in/content/pdf/make-my-trip-tandc.pdf"
    download_file("example", url)

def download_file(file_name, download_url):
    response = urllib.request.urlopen(download_url)
    file = open(file_name + ".pdf", 'wb')
    files=file.readlines()

    files.write(response.read())
    files.close()

    print("Completed")

if __name__ == "__main__":
    main()



urlreader()



