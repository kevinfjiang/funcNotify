# whatsapp_method.py

from twilio.rest import Client

class WhatsAppMethod:
    def __init__(self, account_sid, auth_token, from_whatsapp_number):
        """
        Initialize the WhatsAppMethod class with Twilio credentials and sender number.

        :param account_sid: Twilio Account SID
        :param auth_token: Twilio Auth Token
        :param from_whatsapp_number: Twilio WhatsApp-approved sender number
        """
        self.client = Client(account_sid, auth_token)
        self.from_whatsapp_number = from_whatsapp_number

    def send_notification(self, to_number, message):
        """
        Send a WhatsApp notification to the recipient.

        :param to_number: Recipient's WhatsApp number (in international format)
        :param message: Message to send
        """
        try:
            self.client.messages.create(
                from_=self.from_whatsapp_number,
                to=f"whatsapp:{to_number}",
                body=message,
            )
            print(f"WhatsApp message sent to {to_number}")
        except Exception as e:
            print(f"Failed to send WhatsApp message: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your Twilio credentials and numbers
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    from_whatsapp_number = "whatsapp:+14155238886"

    whatsapp = WhatsAppMethod(account_sid, auth_token, from_whatsapp_number)
    whatsapp.send_notification("+1234567890", "Hello from FuncNotify via WhatsApp!")
