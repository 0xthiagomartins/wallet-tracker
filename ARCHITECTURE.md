# Project Architecture

The **Wallet Tracker Application** is organized into several key directories within the `src/` folder. Below is an overview of each component to facilitate easy understanding and navigation for developers.

## Directory Structure

```
src/
├── client/
├── server/
├── tests/
└── main/
```

### src/client

**Description:**  
This directory contains the Streamlit application, which serves as the frontend of the Wallet Tracker Application. It manages the user interface, user interactions, and displays data visualizations.

**Contents:**
- Streamlit scripts for different pages and components.
- Static assets such as images and CSS files.
- Configuration files specific to the frontend.
- **Requirements:** Refer to `client/requirements.txt`.

### src/server

**Description:**  
The `server/` folder houses all backend services. This includes APIs, business logic, data processing, and interactions with external services like databases and third-party APIs. It utilizes **SQLModel** and **sqlmodel-controller** for ORM and controller-based CRUD operations.

**Contents:**
- API endpoint implementations.
- Service modules handling various functionalities (e.g., authentication, data retrieval).
- Utility functions and middleware.
- **SQLModel:** For ORM and database interactions.
- **sqlmodel-controller:** For managing CRUD operations with high-level abstractions.

### src/tests

**Description:**  
This directory is dedicated to testing the server-side components using Pytest. It ensures that all services function correctly and helps maintain code quality.

**Contents:**
- Test suites for different server modules.
- Mock data and fixtures.
- Configuration for Pytest.

### src/__main__.py

**Description:**  
The `__main__.py` file serves as the application initializer. It bootstraps the entire application, setting up necessary configurations and starting the Streamlit server.

**Contents:**
- Entry point scripts.
- Initialization code for services and dependencies.
- Environment configuration files.

## Additional Notes

- **Modularity:** The project follows a modular architecture, separating concerns between the client, server, and testing components to enhance maintainability and scalability.
- **Testing:** Comprehensive tests are written using Pytest to cover all critical functionalities, ensuring reliability and facilitating future developments.
- **Configuration Management:** Configuration files are organized to manage different environments (development, testing, production) efficiently.

For more detailed information on features and proposals, refer to the [FEATURES.md](FEATURES.md) and [PROPOSALS.md](PROPOSALS.md) files respectively.
