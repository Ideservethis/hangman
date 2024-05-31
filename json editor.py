import json

# Function to read data from a JSON file
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to write data to a JSON file
def write_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data has been successfully written to the file.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
file_path = "data.json"

# Write data to JSON file
data_to_write = {'name': 'John', 'age': 30, 'city': 'New York'}
write_json(data_to_write, file_path)

# Read data from JSON file
data_read = read_json(file_path)
print("Data read from JSON file:")
print(data_read)
