# ATM Management System
## 1. Project Overview
ATM Management System is a beginner-friendly Python console project. It simulates common ATM operations such as PIN verification, balance checking, depositing money, withdrawing money, viewing transaction history, and changing the PIN.

## 2. Features
- PIN verification
- Check account balance
- Deposit money
- Withdraw money
- Transaction history
- Change PIN
- Basic input validation
- Modular Python structure

## 3. Technologies Used
- Python 3
- Python functions
- Classes
- Lists
- Conditional statements
- Loops
- Exception handling
- Basic testing

## 4. Folder Structure
```text
ATM_Management_System_Project/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── account.py
│   ├── transactions.py
│   ├── validation.py
│   ├── operations.py
│   └── menu.py
├── tests/
│   └── test_atm.py
├── docs/
│   └── project_report.pdf
├── README.md
├── statement.md
└── requirements.txt
```

## 5. How to Run
1. Install Python 3.
2. Open the project folder in VS Code or another Python editor.
3. Open the `src` folder in the terminal.
4. Run:
```bash
python main.py
```

Default PIN: `1234`
Starting balance: `Rs. 5000`

## 6. Testing
If pytest is installed, run:
```bash
pytest
```
The test file checks PIN verification, deposit, withdrawal, validation, and transaction history.

## 7. Learning Outcomes
- Learned how to divide a Python project into modules.
- Learned basic class usage.
- Learned functions and parameter passing.
- Learned validation and exception handling.
- Learned basic testing.
- Learned how to organize a project for GitHub.

## 8. Limitations
This is an educational console simulation. It does not connect to a real bank, database, card reader, or payment network. Data is reset when the program is restarted.

## 9. Future Enhancements
- Database storage
- Multiple user accounts
- ATM receipt generation
- Login attempt limit
- Graphical user interface
