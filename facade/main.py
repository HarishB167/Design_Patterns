from .notification_service import NotificationService

if __name__ == "__main__":
    service = NotificationService()
    service.send("Hellow World", "target")