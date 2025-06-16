# AI Bill Parser

A Python program that searches through US Congress bill data to find and extract bills related to artificial intelligence.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone or download this repository
2. Create and activate a virtual environment:
```bash
python3 -m venv bill_parser_env
source bill_parser_env/bin/activate  # On Windows, use: bill_parser_env\Scripts\activate
```

3. Install required packages:
```bash
pip install pandas openpyxl
```

## Usage

1. Create an account at [LegiScan](https://legiscan.com/US/datasets)
2. Download the US Congress bill data from [LegiScan](https://legiscan.com/US/datasets)
3. Extract the downloaded files to a folder named "US" in the same directory as the script
4. Run the script:
```bash
python bill_parser.py
```

The script will:
- Search through all JSON files in the US directory
- Find bills containing "artificial intelligence" in their title or description
- Save the results to "ai_bills.xlsx"

## Output

The generated Excel file (ai_bills.xlsx) contains the following information for each AI-related bill:
- Bill number
- Title
- Description
- Status
- Status date
- URLs (LegiScan and Congress.gov)
- Sponsor information
- Party affiliation



