import 

def hwidcheck():
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    r = requests.get('Pastebin link')

    try:
        if hwid in r.text:
            pass
        else:
            print("[ERROR] HWID Not in database")
            print(f'Your HWID: {hwid}')
            time.sleep(30)
            os._exit()
    except:
        print("[ERROR] Failed to connect to database")
        time.sleep(5)
        os._exit()

    print("HWID Authenticated...")
    time.sleep(1.3)

hwidcheck()
