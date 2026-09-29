# atm sim

MAX_TRY = 3
dLimit = 20000  # 20000 as sir said

def record_txn(acc, t, amt):
    rec = {"type": t, "amount": amt, "balance_after": acc["balance"]}
    acc["history"].append(rec)
    # print(t, amt)

def get_amt(msg):
    while True:
        x = input(msg).strip()
        try:
            a = float(x)
            if a <= 0:
                print("enter amount > 0")
            else:
                return a
        except:
            print("numbers only")

def checkBal(acc):
    print("\n--- BALANCE ---")
    print("Available Balance: Rs." + str(acc["balance"]))

def do_deposit(acc):
    print("\n--- deposit ---")
    amt = get_amt("Enter amount to deposit: Rs.")
    acc["balance"] = acc["balance"] + amt
    record_txn(acc, "Deposit", amt)
    print("deposited Rs." + str(amt))
    print("Available Balance: Rs." + str(acc["balance"]))

def withdraw(acc):
    print("\n--- WITHDRAWAL ---")
    x = input("Enter withdrawal amount (multiples of 100): Rs.").strip()
    try:
        amt = float(x)
    except:
        print("numbers only")
        return
    if amt <= 0:
        print("enter amount > 0")
        return
    # atm notes are 100s
    if amt % 100 != 0:
        print("only multiples of 100")
        return
    if amt > acc["balance"]:
        print("not enough money")
        return
    if acc["daily_withdrawn"] + amt > dLimit:
        print("daily limit is Rs." + str(dLimit))
        print("already taken Rs." + str(acc["daily_withdrawn"]))
        return
    acc["balance"] = acc["balance"] - amt
    acc["daily_withdrawn"] = acc["daily_withdrawn"] + amt
    record_txn(acc, "Withdrawal", amt)
    print("Please collect your cash.")
    print("Available Balance: Rs." + str(acc["balance"]))

def doTransfer(acc, db):
    print("\n--- FUND TRANSFER ---")
    dest = input("Enter the destination Account Number: ").strip()
    if dest == acc["acc_num"]:
        print("cant send to yourself")
        return
    if dest not in db:
        print('Invalid acc no')
        return
    try:
        amt = float(input("Enter transfer amount: Rs.").strip())
    except:
        print("bad amt")
        return
    if amt <= 0:
        print("enter amount > 0")
        return
    if amt > acc["balance"]:
        print("not enough money for transfer")
        return
    acc["balance"] = acc["balance"] - amt
    record_txn(acc, "Transfer TO " + dest, amt)
    other = db[dest]
    other["balance"] = other["balance"] + amt
    record_txn(other, "Transfer FROM " + acc["acc_num"], amt)
    print("done")
    print("Available Balance: Rs." + str(acc["balance"]))


def mini_stmt(acc):
    print("\n--- MINI STATEMENT ---")
    print("Recent Transactions (Last 5):")
    hist = acc["history"]
    if len(hist) == 0:
        print("no txns")
        return
    n = len(hist)
    start = n - 5
    if start < 0:
        start = 0
    i = start
    while i < n:
        t = hist[i]
        print("Type: " + t["type"] + " | Amt: " + str(t["amount"]) + " | Bal: " + str(t["balance_after"]))
        i = i + 1
    print("Available Balance: Rs." + str(acc["balance"]))

def pinchange(acc):
    print("\n--- PIN CHANGE ---")
    p1 = input("Enter new 4-digit PIN: ").strip()
    if len(p1) == 4:
        if p1.isdigit() == True:
            p2 = input("Re-enter new PIN to confirm: ").strip()
            if p1 == p2:
                acc["pin"] = p1
                print("pin changed")
            else:
                print("pins dont match")
        else:
            print("PIN must be 4 digits")
    else:
        print("PIN must be 4 digits")

def userMenu(user, db):
    while True:
        print("")
        print("==============================")
        print("    WELCOME, " + user["name"].upper())
        print("==============================")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Cash")
        print("4. Transfer Funds")
        print("5. Mini Statement")
        print("6. Change PIN")
        print("7. Logout")
        print("")
        ch = input("Select an option (1-7): ").strip()
        n = ch
        if n == "1":
            checkBal(user)
        else:
            if n == '2':
                do_deposit(user)
            else:
                if n == "3":
                    withdraw(user)
                else:
                    if n == "4":
                        doTransfer(user, db)
                    else:
                        if n == "5":
                            mini_stmt(user)
                        else:
                            if n == "6":
                                pinchange(user)
                            else:
                                if n == "7":
                                    print("Logging out...")
                                    print("Goodbye " + user["name"])
                                    break
                                else:
                                    print("wrong option")
                                    print("please enter 1-7")

def startATM():
    db = {
        "1001": {
            "acc_num": "1001",
            'name': "Ayush Jain",
            "pin": "1234",
            "balance": 15000,
            "locked": False,
            "daily_withdrawn": 0,
            "history": [{"type": "Initial Deposit", "amount": 15000, "balance_after": 15000}]
        },
        "1002": {
            "acc_num": "1002",
            "name": "Rahul Verma",
            "pin": "9999",
            "balance": 5000.0,
            "locked": False,
            "daily_withdrawn": 0.0,
            "history": [{"type": "Initial Deposit", "amount": 5000.0, "balance_after": 5000.0}]
        },
        '1003': {
            "acc_num": "1003",
            "name": "Ananya Sharma",
            "pin": "5555",
            "balance": 80000.0,
            "locked": False,
            "daily_withdrawn": 0.0,
            "history": [{"type": "Initial Deposit", "amount": 80000.0, "balance_after": 80000.0}]
        },
        "1004": {
            "acc_num": "1004",
            'name': "Guest Test",
            "pin": "0000",
            "balance": 0,
            "locked": False,
            "daily_withdrawn": 0,
            "history": []
        }
    }

    while True:
        print("")
        print("********************************")
        print("   WELCOME TO XYZ ATM")
        print("********************************")
        print("")
        accno = input("Enter Account Number (or q to quit): ").strip()
        if accno == "q" or accno == "Q" or accno.lower() == "q":
            print("shutting down")
            print("bye")
            break
        if accno not in db:
            print("Error: Account number not recognized.")
            print("try again")
            continue
        acc = db[accno]
        tmp = acc
        if tmp["locked"] == True:
            print("this account is locked")
            print("too many wrong pins")
            continue
        # pin check
        tries = 0
        ok = 0
        while tries < MAX_TRY:
            userpin = input("Enter PIN: ").strip()
            if userpin == acc["pin"]:
                ok = 1
                print("login ok")
                break
            else:
                tries = tries + 1
                left = MAX_TRY - tries
                if left > 0:
                    print("wrong pin, " + str(left) + " left")
                if left == 0:
                    print("no tries left")
        if ok == 1:
            print("Welcome " + acc['name'])
            userMenu(acc, db)
        else:
            acc["locked"] = True
            print("account locked now")
            print("contact bank")

# TODO: maybe write balances to a file later
if __name__ == "__main__":
    startATM()
