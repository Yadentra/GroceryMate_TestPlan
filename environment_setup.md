# Environment Setup for Grocery Mate Webshop Testing

## Project Overview
This setup document outlines the environment configuration for executing automated tests on the Grocery Mate webshop: [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/).

## Test Environment
The following tools and frameworks are used to execute automated test cases efficiently:

- **Automated Testing Tool**: Selenium WebDriver
- **Programming Language**: Python
- **IDE**: Visual Studio Code
- **API Testing Tool**: Postman
- **Defect Tracking**: JIRA (for recording and tracking bugs)

## System Requirements
- **OS**: Windows 10 / macOS
- **Browser Compatibility**: Chrome, Firefox (latest versions)
- **Dependencies**: 
  - Selenium WebDriver (latest version)
  - Python 3.x
  - Browser Drivers (ChromeDriver for Chrome, GeckoDriver for Firefox)
  
## Setup Instructions

1. **Install Python**  
   Ensure Python 3.x is installed. Verify by running:
   ```bash
   python --version

2. **Install Selenium**
  Install Selenium WebDriver via pip:

  pip install selenium


3. **Configure WebDriver**

  Download ChromeDriver or GeckoDriver based on the browser in use.

  Add the driver to your system PATH.


4. **Install Postman**
  Postman will be used for API testing of backend services. Download and install it from Postman’s official site.


5. **Configure JIRA Access**
  Ensure you have access to the team’s JIRA project for defect tracking.


## Environment Validation

  Test Execution: Run a sample Selenium script to ensure WebDriver setup is functioning.

  API Requests: Send a test request in Postman to verify API connectivity.


## Notes

  Make sure all configurations are aligned with Grocery Mate’s testing requirements. Confirm that all browser drivers are compatible with the installed browser versions.

  This file provides a clear outline of the setup, tools, and environment requirements for testing. Let me know if you need further customization!
