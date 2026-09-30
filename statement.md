# Project Statement

## Project Title
ATM Management System

## Problem Statement
Basic ATM activities such as checking balance, depositing money, withdrawing money, and changing a PIN can be represented through a simple software simulation. The aim of this project is to create a beginner-friendly console application that demonstrates these operations using Python.

## Scope
The project provides a simulated ATM environment for one account. It handles PIN verification, balance management, deposits, withdrawals, transaction history, and PIN changes.

## Target Users
- Students learning Python
- Beginners learning modular programming
- Teachers evaluating basic programming concepts

## High-Level Features
1. PIN verification
2. Balance inquiry
3. Deposit
4. Withdrawal
5. Transaction history
6. PIN change
7. Input validation

## Modules
- `main.py` - controls the application flow
- `config.py` - stores project settings
- `account.py` - handles account data and operations
- `transactions.py` - stores transaction history
- `validation.py` - validates inputs
- `operations.py` - performs ATM operations
- `menu.py` - displays the ATM menu

## Non-Functional Requirements
1. Usability - menu and messages should be easy to understand.
2. Reliability - invalid amounts and incorrect PINs should be handled.
3. Maintainability - code should be divided into separate modules.
4. Error Handling - invalid numeric input should not crash the program.
5. Resource Efficiency - the console application should use only basic Python resources.

## Input and Output
Input includes PIN, menu choice, amount, and new PIN. Output includes balance, transaction messages, validation messages, and menu options.

