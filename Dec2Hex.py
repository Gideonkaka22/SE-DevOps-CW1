import sys

def decimal_to_hex(decimal_value):
    try:
        decimal_value = int(decimal_value)  # Convert input to integer
        return hex(decimal_value)[2:].upper()  # Convert to hex without '0x'
    except ValueError:
        return "Error: Invalid input. Please enter a valid integer."
    except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting...")
    exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input provided. Please enter an integer.")
    else:
        result = decimal_to_hex(sys.argv[1])
        print(result)
