# Proposals

This document outlines additional features, suggestions, and supporting information to enhance the **Wallet Tracker Application**. These proposals aim to provide extended functionality, improve user experience, and ensure the application's robustness.

## Additional Features & Suggestions

1. **Tax Reporting:**
   - Generate tax reports based on user transactions to assist in filing taxes.

2. **Integration with Exchanges:**
   - Allow users to connect their exchange accounts (e.g., Binance, Coinbase) for automatic transaction imports.

3. **Mobile App Companion:**
   - Develop a mobile version or companion app for on-the-go access.

4. **Social Sharing:**
   - Enable users to share their portfolio performance or specific achievements on social media.

5. **AI-Powered Insights:**
   - Provide predictive analytics or investment suggestions based on historical data.

6. **Dark Mode:**
   - Offer a dark mode theme for better user experience in low-light environments.

7. **Customizable Widgets:**
   - Allow users to customize their dashboard with widgets of their choice.

8. **Backup and Restore:**
   - Provide options for users to back up their data and restore it if needed.

9. **Localization:**
   - Support multiple languages to cater to a global user base.

10. **API Access for Users:**
    - Allow users to access their data programmatically via a personal API.

## Non-Functional Requirements

### Performance

- **Response Time:**
  - The application should respond to user interactions within 2 seconds.

- **Data Refresh Rate:**
  - Real-time data updates should occur at least every minute.

### Scalability

- **User Growth:**
  - The system should handle an increasing number of users without performance degradation.

- **Data Volume:**
  - Efficiently manage large volumes of transaction and price data.

### Usability

- **User-Friendly Interface:**
  - Intuitive and easy-to-navigate UI.

- **Accessibility:**
  - Compliance with accessibility standards (e.g., WCAG) to support users with disabilities.

### Reliability

- **Uptime:**
  - Aim for 99.9% uptime.

- **Data Integrity:**
  - Ensure accuracy and consistency of all data.

### Maintainability

- **Code Quality:**
  - Write clean, modular, and well-documented code.

- **Update Mechanism:**
  - Facilitate easy updates and feature additions.

## Technology Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **APIs:** CoinGecko for cryptocurrency data
- **Database:** PostgreSQL/MySQL or cloud-based solutions like Firebase
- **Authentication:** OAuth 2.0, JWT
- **Hosting:** Streamlit Cloud, AWS, Heroku, or similar platforms
- **Version Control:** Git and GitHub/GitLab

## User Interface (UI) Design

- **Responsive Design:**
  - Ensure compatibility across various devices and screen sizes.

- **Dashboard Layout:**
  - Clear separation of different sections like portfolio overview, transaction history, and charts.

- **Interactive Elements:**
  - Use interactive charts and tables for better data visualization.

- **Consistent Styling:**
  - Maintain a consistent color scheme, typography, and component styling throughout the application.

## Assumptions

- **User Knowledge:**
  - Users have basic knowledge of cryptocurrency and wallet management.

- **Supported Cryptocurrencies:**
  - The application will initially support major cryptocurrencies available on CoinGecko.

- **Manual Data Entry:**
  - Users will manually input transactions unless exchange integrations are implemented.

## Constraints

- **API Rate Limits:**
  - Adhere to the rate limits imposed by CoinGecko and other integrated APIs.

- **Budget:**
  - Development within a specified budget, impacting feature scope and technology choices.

- **Timeline:**
  - Project deadlines may affect the prioritization of features.

## Appendix

### Glossary

- **Inflow:** Addition of assets to the wallet (e.g., purchasing cryptocurrency).
- **Outflow:** Removal of assets from the wallet (e.g., selling cryptocurrency).
- **Swap:** Exchanging one cryptocurrency for another within the wallet.

### References

- [CoinGecko API Documentation](https://www.coingecko.com/en/api)
- [Streamlit Documentation](https://docs.streamlit.io/)
