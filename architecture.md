# Design Diagrams

## System Architecture

```text
User
  |
  v
main.py
  |
  +----> menu.py
  |
  +----> operations.py ----> validation.py
  |             |
  |             +-----------> account.py
  |             |
  |             +-----------> transactions.py
  |
  +----> config.py
```

## Workflow

```text
Start
  |
Enter PIN
  |
Correct? ---- No ----> Exit
  |
 Yes
  v
Show Menu
  |
  +--> Balance
  +--> Deposit
  +--> Withdraw
  +--> History
  +--> Change PIN
  |
 Exit
  |
End
```

## Use Case Diagram (text form)

```text
             +----------------------+
             |   ATM Management     |
             |       System         |
             +----------------------+
               ^   ^   ^   ^   ^
               |   |   |   |   |
             User User User User User
               |   |   |   |   |
              PIN Balance Deposit Withdraw
                           History / PIN Change
```

## Component Diagram

```text
+---------+     +---------+     +-------------+
| main.py | --> | menu.py |     |  config.py  |
+----+----+     +---------+     +-------------+
     |
     v
+-------------+
| operations  |
+------+------+ 
       |
   +---+---+----------------+
   v       v                v
account  validation   transactions
```

## Sequence Diagram (withdrawal)

```text
User -> main.py: Select Withdraw
main.py -> operations.py: withdraw_money()
operations.py -> User: Ask amount
User -> operations.py: Enter amount
operations.py -> account.py: Check balance
account.py -> operations.py: Balance result
operations.py -> account.py: Remove money
operations.py -> transactions.py: Save transaction
operations.py -> User: Show result
```
