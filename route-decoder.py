import base64
import sys
import json
from biplist import readPlistFromString, writePlistToString
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)


def decode_streisand_url(encoded_text):
    # Remove prefix "streisand://"
    if encoded_text.startswith("streisand://"):
        encoded_text = encoded_text[len("streisand://"):]

    # First base64 decoding
    decoded_step1 = base64.b64decode(encoded_text).decode('utf-8')

    # Remove prefix "import/route://"
    if decoded_step1.startswith("import/route://"):
        decoded_step1 = decoded_step1[len("import/route://"):]

    # Second base64 decoding
    decoded_step2 = base64.b64decode(decoded_step1)

    # Decode from bplist
    try:
        plist_data = readPlistFromString(decoded_step2)

        # Convert and format JSON for validation
        json_data = json.loads(json.dumps(plist_data))  # Convert to JSON and back
        formatted_json = json.dumps(json_data, ensure_ascii=False, indent=4)
        return formatted_json
    except Exception as e:
        print(f"Error decoding bplist: {e}")
        return None


def encode_streisand_url(data):
    # Convert data to bplist format
    try:
        plist_data = writePlistToString(data)
    except Exception as e:
        print(f"Error encoding to bplist: {e}")
        return None

    # First base64 encoding
    encoded_step1 = base64.b64encode(plist_data).decode('utf-8')

    # Add prefix "import/route://"
    encoded_step1 = "import/route://" + encoded_step1

    # Second base64 encoding
    encoded_step2 = base64.b64encode(encoded_step1.encode('utf-8')).decode('utf-8')

    # Add prefix "streisand://"
    encoded_text = "streisand://" + encoded_step2
    return encoded_text


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("-d", "-e"):
        print("Usage: python script.py -d '<encoded_text>' or python script.py -e '<json_data>'")
        sys.exit(1)

    mode = sys.argv[1]
    text = sys.argv[2]

    if mode == "-d":
        result = decode_streisand_url(text)
        if result is not None:
            # Print decoded JSON in green
            print(Fore.YELLOW + "Decoded result:\n", result)
        else:
            print("Error decoding")
    elif mode == "-e":
        try:
            data = json.loads(text)
            result = encode_streisand_url(data)
            if result is not None:
                print(Fore.YELLOW + "Encoded result:\n", result)
            else:
                print("Error encoding")
        except json.JSONDecodeError:
            print("Error: invalid JSON format.")
