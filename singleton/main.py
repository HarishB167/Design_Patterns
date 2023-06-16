from .config_manager import ConfigManager

if __name__ == "__main__":
    manager = ConfigManager.get_instance()
    manager.set("name", "Mosh")

    other = ConfigManager.get_instance()
    print(other.get("name"))