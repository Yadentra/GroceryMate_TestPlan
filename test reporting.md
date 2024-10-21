# Test Execution Documentation

## Test Execution Overview

| Test Case ID | Test Case Description                   | Status    | Execution Date | Executed By | Notes                                      |
|---------------|-----------------------------------------|-----------|----------------|-------------|--------------------------------------------|
| TC01          | User Registration                       | Passed    | 16.07.2024     | Mapuranga   | User registered successfully.              |
| TC02          | User Login                              | Passed    | 17.07.2024     | Mapuranga   | User logged in without issues.             |
| TC03          | Product Search Functionality            | Passed    | 18.07.2024     | Mapuranga   | Search results returned relevant products. |
| TC04          | Add Product to Cart                     | Passed    | 19.07.2024     | Mapuranga   | Products added successfully to the cart.   |
| TC05          | Checkout Process                        | Failed    | 20.07.2024     | Mapuranga   | Issues encountered during checkout.        |
| TC06          | Order History and Tracking              | Passed    | 21.07.2024     | Mapuranga   | Order history displayed correctly.         |

## Summary of Findings
- **Total Test Cases Executed:** 6
- **Total Passed:** 5
- **Total Failed:** 1
- **Total Blocked:** 0

## Bug Report

| Bug ID | Test Case ID | Bug Description                                     | Severity | Status       | Assigned To | Date Reported |
|--------|--------------|-----------------------------------------------------|----------|--------------|-------------|----------------|
| BUG01  | TC05         | Unable to complete checkout due to payment failure. | Critical | Open         | Yadentra    | 19.07.2024     |

## Notes
- **General Observations:**
  - The user registration and login features performed as expected without issues.
  - Product search functionality returned relevant results, but loading times were slightly longer than desired.

- **Bugs Identified:**
  - A critical bug affecting payment processing during checkout needs immediate attention from the development team.

- **Recommendations:**
  - Consider optimizing the search functionality to improve response times.
  - Conduct a follow-up round of testing after bug fixes to ensure all issues are resolved.
