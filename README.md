# ATM Machine Simulator

Python CLI program that simulates a basic bank ATM.

**GitHub:** https://github.com/alaricxc/mini_atm_simulator
No extra libraries. No files. No classes. All account data stays in a dictionary in RAM, so closing the program (press `q` or Ctrl+C) resets balances, PIN changes and lockouts.

## How to run

```
python main.py
```

On macOS / Linux:

```
python3 main.py
```

Python 3 is enough. Nothing to install.

## Test accounts

| Account No. | PIN  | Starting Balance |
|-------------|------|------------------|
| 1001        | 1234 | Rs. 15,000       |
| 1002        | 9999 | Rs. 5,000        |
| 1003        | 5555 | Rs. 80,000       |
| 1004        | 0000 | Rs. 0            |

## Menu

After login:

1. Check Balance
2. Deposit Funds
3. Withdraw Cash (multiples of 100, daily cap Rs. 20,000)
4. Transfer Funds (to another account in the same program)
5. Mini Statement (last 5 transactions)
6. Change PIN (4 digits)
7. Logout

Login allows 3 wrong PIN tries, then the account is locked for that run.

## Files

| File | What it is |
|------|------------|
| `main.py` | Whole program |
| `README.md` | This file |
| `Project_Report.html` | Printable project report (open in browser → Ctrl+P) |

## Report

Open `Project_Report.html` in a browser and print it (A4, include background graphics if you want the cover to look right). Fill student name / roll / college on the first page before printing.
