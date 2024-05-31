import requests

def convert_currency(amount, from_currency, to_currency):
    # API endpoint for currency conversion
    endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        # Fetch latest exchange rates
        response = requests.get(endpoint)
        data = response.json()

        # Check if the API request was successful
        if response.status_code == 200:
            # Convert amount to the target currency
            if to_currency in data['rates']:
                exchange_rate = data['rates'][to_currency]
                converted_amount = amount * exchange_rate
                return converted_amount
            else:
                return f"Error: Currency '{to_currency}' not found."
        else:
            return "Error: Failed to fetch exchange rates."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
amount = 104  # Amount to convert
from_currency = "USD"  # Currency to convert from
to_currency = "EUR"  # Currency to convert to

converted_amount = convert_currency(amount, from_currency, to_currency)
if isinstance(converted_amount, float):
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print(converted_amount)
