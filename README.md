# Python Password Manager (CLI)

A command-line based Password Manager built using Python that allows users to securely store and manage credentials. This project demonstrates secure handling of sensitive data with basic encryption and user-friendly features.

## Features
- Add new account (website, username, password)
- Password masking (hide/show option)
- Search account by website
- Delete account
- Input validation for reliable data handling
- Password generation (optional)
- Basic encryption using base64
- JSON file storage for persistence

## Technologies Used
- Python
- JSON (for data storage)
- Base64 (for encoding passwords)

## How It Works
- User inputs account details
- Passwords are encoded before saving
- Data is stored in a JSON file
- Passwords are decoded only when displayed

## Purpose
This project was built to understand secure data handling, file storage, and CLI-based application design.

## Future Improvements
- Strong encryption methods
- GUI or web interface
- Master password protection
