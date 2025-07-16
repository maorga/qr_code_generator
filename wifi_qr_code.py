import qrcode
import pwinput

def escape_wifi_string(s):
    """
    Escape special characters in Wi-Fi strings to ensure they are correctly formatted for QR codes.
    This function replaces backslashes, semicolons, commas, and colons with their escaped.
    Example:
    'MyNetwork' becomes 'MyNetwork'
    'My;Network' becomes 'My\\;Network'
    """
    return s.replace('\\', '\\\\').replace(';', '\\;').replace(',', '\\,').replace(':', '\\:')

def generate_wifi_qr(ssid, password, security):
    """
    Generate a QR code for Wi-Fi credentials.
    :param ssid: The SSID of the Wi-Fi network.
    :type ssid: str
    :param password: The password for the Wi-Fi network.
    :type password: str
    :param security: The security type of the Wi-Fi network (WPA, WPA2, WPA3, WPA2-WPA3, WEP).
    :type security: str
    :return: None
    :rtype: None
    Generates a QR code and saves it as 'wifi_qr.png'.
    """
    ssid = escape_wifi_string(ssid.strip())
    password = escape_wifi_string(password.strip())
    security = security.strip().upper()

    # Map WPA2, WPA3, WPA2-WPA3 to WPA
    if security in ['WPA2', 'WPA3', 'WPA2-WPA3']:
        security = 'WPA'

    valid_security_types = ['WPA', 'WEP', '']
    if security not in valid_security_types:
        print("Invalid security type. Please use 'WPA', 'WPA2', 'WPA3', 'WPA2-WPA3', 'WEP', or leave blank for open network.")
        return None

    wifi_string = f"WIFI:S:{ssid};T:{security};P:{password};;"
    qr = qrcode.make(wifi_string)
    qr.save("wifi_qr.png")
    print("QR code saved as 'wifi_qr.png'")

def main():
    print("Enter WiFi details to generate QR code:")
    ssid = input("SSID (Name of a Wi-Fi network): ")
    password = pwinput.pwinput("Password (Leave empty for no password): ")
    security = input("Security Type (WPA/WPA2/WPA3/WPA2-WPA3/WEP): ")

    generate_wifi_qr(ssid, password, security)

if __name__ == "__main__":
    main()