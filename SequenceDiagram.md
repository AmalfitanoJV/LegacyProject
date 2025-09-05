```Mermaid
sequenceDiagram
    participant User
    participant Main
    participant AccountManager
    participant OperationFactory
    participant Operation
    participant AccountData

    User->>Main: Start app (python src/main.py)
    Main->>User: Show menu
    User->>Main: Select option (1-4)
    Main->>OperationFactory: get_operation(choice, [amount])
    OperationFactory->>Operation: Create operation instance
    Main->>AccountManager: perform_operation(operation)
    AccountManager->>Operation: execute(account)
    Operation->>AccountData: read_balance() / write_balance([amount])
    AccountData-->>Operation: Return balance / update balance
    Operation->>User: Print result (balance, credited, debited, error)
    User->>Main: Select next option or exit
    Main->>User: Print exit message (if chosen)
```