# Developer Guide

Welcome to the **Wallet Tracker Application Developer Guide**. This document provides essential instructions for setting up the development environment, running the application, executing tests, and building the project. Follow the steps below to get started.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.8+**
- **Git**
- **Node.js** (if applicable for frontend assets)
- **PostgreSQL/MySQL** (or your chosen database)
- **Virtual Environment Tool** (e.g., `venv` or `conda`)

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/wallet-tracker.git
   cd wallet-tracker
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add the necessary configurations:

   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/wallet_tracker
   SECRET_KEY=your_secret_key
   API_KEY=your_api_key
   ```

## Running the Application

To start the application locally:

1. **Initialize the Database**

   ```bash
   cd src/__main__
   python init_db.py
   ```

2. **Run the Streamlit App**

   ```bash
   streamlit run src/client/app.py
   ```

   The application will be accessible at `http://localhost:8501`.

## Running Tests

The project uses **Pytest** for testing the server-side components.

1. **Navigate to the Tests Directory**

   ```bash
   cd src/tests
   ```

2. **Run All Tests**

   ```bash
   pytest
   ```

3. **Run Specific Test Suite**

   ```bash
   pytest test_authentication.py
   ```

## Building the Application

To build and deploy the application, follow these steps:

1. **Prepare for Deployment**

   Ensure all dependencies are listed in `requirements.txt` and configurations are set in `.env`.

2. **Build the Frontend Assets** (if applicable)

   ```bash
   cd src/client
   npm install
   npm run build
   ```

3. **Deploy to Hosting Service**

   You can deploy the application using platforms like **Streamlit Cloud**, **Heroku**, or **AWS**. Below is an example using Streamlit Cloud:

   - **Sign Up/Login** to [Streamlit Cloud](https://streamlit.io/cloud).
   - **Connect Your GitHub Repository**.
   - **Configure Deployment Settings**, specifying the main app file (e.g., `src/client/app.py`).
   - **Deploy** the application.

4. **Migrate the Database on Production**

   Ensure that the production database is set up and migrate the necessary tables:

   ```bash
   python src/__main__/init_db.py
   ```

## Additional Notes

- **Code Style:** The project follows PEP 8 guidelines. It's recommended to use linters like `flake8` to maintain code quality.
  
- **Continuous Integration:** Set up CI/CD pipelines using tools like **GitHub Actions** to automate testing and deployment.

- **Contributing:** Refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to the project.

For any further assistance or queries, feel free to reach out to the development team.
