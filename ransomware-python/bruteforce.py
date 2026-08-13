from zipfile import ZipFile
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except RuntimeError:
        return False
def main():
    print("[+] Beginning bruteforce")
    found = False
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for password in f:
                password=password.strip()

                if attempt_extract(zf, password):
                    print("[+] Password FOUND:", password)
                    found = True
                    break

    if not found:
        print("[-] Password NOT FOUND in list")
    print("<<< PROCESS ENDED")
if __name__ == "__main__":
    main()