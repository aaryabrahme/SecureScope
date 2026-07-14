# SecureScope

SecureScope is a Python-based Data Security Posture Management (DSPM) scanner that discovers sensitive information across files, detects potential secrets using Shannon Entropy, and assigns a risk score to each file.

## Features

- Recursive file scanning
- Supports TXT, CSV, DOCX, and PDF
- Detects:
  - Email addresses
  - Phone numbers
  - PAN numbers
  - Password patterns
- Entropy-based secret detection
- Risk scoring (Low, Medium, High, Critical)
- Structured scan reports

## Tech Stack

- Python
- Regular Expressions
- Shannon Entropy
- pathlib
- python-docx
- PyPDF2

## Project Structure

```text
SecureScope/
├── main.py
├── scanner/
├── sample_data/
├── requirements.txt
└── README.md
```

## Future Improvements

- Streamlit Dashboard
- JSON/PDF report export
- Insider Risk Detection using Isolation Forest
- Risk analytics and charts

## Learning Outcomes

This project was built to understand:

- Data Security Posture Management (DSPM)
- Sensitive data discovery
- Information theory (Shannon Entropy)
- Software architecture and modular design