import base64
import binascii
import json
import sys
    

if __name__ == "__main__":
    if not 1 < len(sys.argv) < 3:
        print("Usage: python tokens.py TOKEN")
    else:
        token = sys.argv[1]
        decoded = {}
        for part in token.split(".")[:2]:
            padding = "=" * (-len(part) % 4)
            try:
                payload = base64.urlsafe_b64decode(part + padding)
            except binascii.Error:
                print(f"Error decoding part: {part}")
            else:
                decoded.update(json.loads(payload))
        print(json.dumps(decoded, indent=4))
