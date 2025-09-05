```mermaid
graph TD
    subgraph main.py
        Main[Main Application]
        Menu[Menu Logic]
    end

    subgraph operation.py
        Operation[Operation (Base)]
        Deposit[Deposit]
        Withdraw[Withdraw]
        OperationFactory[OperationFactory]
    end

    subgraph data.py
        AccountData[AccountData]
    end

    %% Coupling arrows
    Main --> OperationFactory
    Main --> AccountData
    OperationFactory --> Deposit
    OperationFactory --> Withdraw
    Deposit --> AccountData
    Withdraw --> AccountData

    %% Cohesion notes
    classDef mainCohesion fill:#e0ffe0,stroke:#333,stroke-width:2px;
    classDef opCohesion fill:#e0f7ff,stroke:#333,stroke-width:2px;
    classDef dataCohesion fill:#fffbe0,stroke:#333,stroke-width:2px;
    class Main,Menu mainCohesion;
    class Operation,Deposit,Withdraw,OperationFactory opCohesion;
    class AccountData dataCohesion;
```