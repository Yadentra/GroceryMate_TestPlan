# Grocery Mate Requirements

## Overview
This document outlines the detailed requirements for the new features to be implemented in the Grocery Mate Webshop.

## Features

### 1. Product Rating System

#### Description
The Product Rating System allows customers to rate and review products.

#### Detailed Requirements
- **User Role**: All registered users can rate products they have purchased.
- **Rating Scale**: Users can rate products on a scale of 1 to 5 stars.
- **Review Text**: Users can provide a textual review (optional, up to 500 characters).
- **Display Ratings**: Average rating displayed on the product page.
- **Validation**: Users cannot submit a rating without being logged in and can only rate a product once.

### 2. Age Verification for Alcoholic Products

#### Description
Ensures that customers are of legal age before purchasing alcoholic products.

#### Detailed Requirements
- **Age Verification Prompt**: Appears when a user adds an alcoholic product to the cart.
- **Input Method**: Users enter their date of birth.
- **Validation**: Users must be at least 21 years old to proceed.

### 3. Shipping Cost Changes

#### Description
Updates shipping costs based on user location and cart value.

#### Detailed Requirements
- **Location Input**: Users enter their shipping address.
- **Dynamic Calculation**: System calculates shipping costs based on the address.
- **Shipping Methods**: Various options available with corresponding costs.

## Conclusion
This document aims to provide a detailed foundation for the implementation of new features in the Grocery Mate Webshop.
