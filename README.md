# QR Code Wi-Fi Generator

Generate QR codes for Wi-Fi credentials, URLs/websites, and WhatsApp chats.  
Scan the QR code with your phone to quickly join a network, open a website, or start a WhatsApp chat.

## Features

- **Wi-Fi QR Code:**  
  Generate a QR code for Wi-Fi credentials (SSID, password, security type).
- **URL/Website QR Code:**  
  Generate a QR code that opens a website or URL.
- **WhatsApp Chat QR Code:**  
  Generate a QR code to open a WhatsApp chat with a phone number (no need to save the contact).

## Usage

1. Run the script:
    ```
    python wifi_qr_code.py
    ```
2. Choose the QR code type:
    - 1: Wi-Fi
    - 2: URL/Website
    - 3: WhatsApp Chat
3. Enter the required details.
4. Scan the generated PNG file with your phone.

## Examples

- **Wi-Fi:**  
  Enter your SSID, password, and security type (WPA/WPA2/WPA3/WPA2-WPA3/WEP).
- **URL/Website:**  
  Enter a URL (e.g., `https://example.com`).
- **WhatsApp Chat:**  
  Enter a phone number with country code (e.g. (Israel +972), `972512553480`).

## Requirements

- Python 3.x
- `qrcode` and `pwinput` libraries

## Install dependencies

```
pip install qrcode[pil] pwinput
```

## Output

- Wi-Fi QR code: `wifi_qr.png`
- URL QR code: `url_qr.png`
- WhatsApp chat QR code: `whatsapp_chat_qr.png`

## License
---

Feel free to contribute or suggest new features!