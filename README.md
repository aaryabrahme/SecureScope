# SecureScope

SecureScope is a Python-based Data Security Posture Management (DSPM) scanner that discovers sensitive information across files, detects potential secrets using Shannon Entropy, and assigns a risk score to each file.

### Features

### Data Discovery
- Recursive file scanning
- Supports TXT, CSV, PDF, and DOCX files

### Sensitive Data Detection
- Email detection
- Phone number detection
- Plaintext password exposure detection
- High entropy secret detection

### Risk Analysis
- Automated risk scoring
- Severity classification:
  - LOW
  - MEDIUM
  - HIGH
  - CRITICAL

### Reporting
- JSON security reports
- Timestamped scan history
- Scan metadata
- Structured findings
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