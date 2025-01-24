from wechatpy import WeChatClient
from wechatpy.exceptions import WeChatClientException

class WeChatMethod:
    def __init__(self, app_id, app_secret):
        """
        Initialize the WeChatMethod class with WeChat AppID and AppSecret.

        :param app_id: WeChat AppID
        :param app_secret: WeChat AppSecret
        """
        self.client = WeChatClient(app_id, app_secret)

    def send_notification(self, openid, message):
        """
        Send a WeChat notification to a user.

        :param openid: The recipient's WeChat OpenID
        :param message: The message to send
        """
        try:
            self.client.message.send_text(openid, message)
            print(f"WeChat message sent to {openid}")
        except WeChatClientException as e:
            print(f"Failed to send WeChat message: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your WeChat credentials
    app_id = "your_app_id"
    app_secret = "your_app_secret"

    wechat = WeChatMethod(app_id, app_secret)
    wechat.send_notification("user_openid", "Hello from FuncNotify via WeChat!")
