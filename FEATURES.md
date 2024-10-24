# Features

The **Wallet Tracker Application** includes a comprehensive set of features to ensure users can effectively manage and monitor their cryptocurrency portfolios. Below are the detailed descriptions of each feature.

## User Authentication

- **Registration:**
  - Users can create an account using email and password or third-party OAuth providers (e.g., Google, GitHub).
  
- **Login/Logout:**
  - Secure login and logout functionalities.
  
- **Password Recovery:**
  - Mechanism for users to reset forgotten passwords.
  
- **Profile Management:**
  - Users can update their personal information and change passwords.

## Asset Management

### Asset Inflow/Outflow

- **Add Transaction:**
  - Users can register asset inflows (purchases) and outflows (sales) by specifying:
    - Asset type (e.g., Bitcoin, Ethereum)
    - Quantity
    - Price in USD at the time of transaction
    - Date and time of transaction
    - Transaction type (Inflow/Outflow)

- **Edit/Delete Transaction:**
  - Users can modify or remove previously recorded transactions.

### Asset Swaps

- **Register Swap:**
  - Users can log asset swaps by specifying:
    - From Asset and Quantity
    - To Asset and Quantity
    - Swap date and time
    - Exchange rate at the time of swap

- **Swap History:**
  - View a list of all past swaps.

## Data Retrieval

- **API Integration:**
  - Utilize APIs like CoinGecko to fetch real-time and historical price data for supported cryptocurrencies.

- **Data Caching:**
  - Implement caching mechanisms to reduce API calls and improve performance.

## Performance History

- **Portfolio Value Over Time:**
  - Visual representation of the total portfolio value changes over selected periods.

- **Individual Asset Performance:**
  - Track the performance of each asset within the portfolio.

## Asset Dominance Graph

- **Dominance Visualization:**
  - Graph showing the percentage allocation of each asset in the wallet over time.

- **Interactive Charts:**
  - Allow users to hover and see specific data points.

## Dashboard

- **Current Portfolio Status:**
  - Overview of current asset allocations, total portfolio value, and individual asset metrics.

- **Allocation Breakdown:**
  - Pie or bar charts displaying the distribution of assets.

- **Key Metrics:**
  - Display important statistics such as total investment, current value, profit/loss, and ROI.

- **Recent Activity:**
  - List of the latest transactions and swaps.

## Notifications & Alerts

- **Price Alerts:**
  - Notify users when an asset reaches a specified price threshold.

- **Performance Alerts:**
  - Alert users on significant portfolio performance changes.

- **Transaction Reminders:**
  - Remind users to log transactions if not done within a set period.

## Reporting

- **Export Reports:**
  - Allow users to export their portfolio data and performance reports in formats like CSV, PDF, or Excel.

- **Custom Reports:**
  - Enable users to generate reports based on specific criteria or date ranges.

## Multi-Currency Support

- **Fiat Currencies:**
  - Support for multiple fiat currencies (e.g., EUR, GBP) alongside USD.

- **Crypto Pairs:**
  - Handle transactions involving different cryptocurrency pairs.

## Export/Import Data

- **Data Backup:**
  - Allow users to back up their data.

- **Data Import:**
  - Enable users to import data from other wallet tracking tools or CSV files.

## Security Features

- **Data Encryption:**
  - Ensure all sensitive data is encrypted both in transit and at rest.

- **Two-Factor Authentication (2FA):**
  - Provide an option for users to enable 2FA for enhanced security.

- **Role-Based Access Control:**
  - If applicable, manage different user roles and permissions.

---

For more detailed descriptions of additional features and suggestions, refer to the [PROPOSALS.md](PROPOSALS.md) file.
