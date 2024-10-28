
# Streisand URL Encoder/Decoder

This Python script encodes and decodes Streisand-formatted URLs, converting them between a base64-encoded `bplist` format and JSON. It provides two main functions:
- **Decoding**: Converts an encoded Streisand URL to a human-readable JSON format.
- **Encoding**: Converts JSON data to a Streisand URL format.

## Features
- Supports decoding Streisand URLs with base64 and `bplist` decoding.
- Encodes JSON data back into Streisand URL format.
- Displays decoded JSON output.

## Requirements
- Python 3.6 or higher
- Install dependencies via:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

### Decoding a Streisand URL
To decode a Streisand URL, use the `-d` flag followed by the encoded string:
```bash
python route-decoder.py -d 'streisand://...'
```
This will output the decoded JSON data.

### Encoding JSON to Streisand URL
To encode JSON back to Streisand URL format, use the `-e` flag followed by a JSON string:
```bash
python route-decoder.py -e '{"rules": [{"ip": [], "outboundTag": "direct", ...}]}'
```

## Example
```bash
# Decode example
python script.py -d 'streisand://aW1wb3J0L3JvdXRlOi8vWW5Cc2...'

# Encode example
python script.py -e '{"rules": [{"ip": ["geoip:ru"], "outboundTag": "direct"}], "name": "Routing", "uuid": "B4BC7FBC-0B99-4930-B1EC-7EC2EFD7B117"}'
```


## License
This project is licensed under the MIT License.
