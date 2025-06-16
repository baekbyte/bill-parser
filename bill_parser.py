import json
import os
import pandas
from pathlib import Path

def search_ai_bills(directory):
    """
    Search through all JSON bill files in the directory for AI-related content
    @param directory: Path to the directory containing bill JSON files
    @return: List of dictionaries containing AI-related bill information
    """
    ai_bills = []
    
    # Walking through all JSON files in the directory (US Folder)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                        # Extracting bill information (title, description, etc.)
                        bill_data = data.get('bill', {})
                        title = bill_data.get('title', '').lower()
                        description = bill_data.get('description', '').lower()
                        
                        # Checking if bill is AI-related
                        if 'artificial intelligence' in title or 'artificial intelligence' in description:
                            ai_bills.append({
                                'bill_number': bill_data.get('bill_number', ''),
                                'title': bill_data.get('title', ''),
                                'description': bill_data.get('description', ''),
                                'status': bill_data.get('status', ''),
                                'status_date': bill_data.get('status_date', ''),
                                'url': bill_data.get('url', ''),
                                'state_link': bill_data.get('state_link', ''),
                                'sponsor': bill_data.get('sponsors', [{}])[0].get('name', '') if bill_data.get('sponsors') else '',
                                'party': bill_data.get('sponsors', [{}])[0].get('party', '') if bill_data.get('sponsors') else ''
                            })
                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")
    
    return ai_bills

def save_to_excel(bills, output_file):
    """
    Save bill information to Excel file
    @param bills: List of dictionaries containing bill information
    @param output_file: Path to output Excel file
    """
    if not bills:
        print("No AI-related bills found.")
        return
    
    # Create DataFrame
    df = pandas.DataFrame(bills)
    
    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"Found {len(bills)} AI-related bills. Results saved to {output_file}")

def main():
    # Initializing variables
    us_directory = "US"
    output_file = "ai_bills.xlsx"
    
    # Printing the directory and output file
    print("=== AI Bill Search ===")
    print(f"Searching directory: {us_directory}")
    
    # Searching for AI-related bills
    ai_bills = search_ai_bills(us_directory)
    
    # Saving results
    save_to_excel(ai_bills, output_file)

if __name__ == "__main__":
    main()
