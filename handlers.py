import requests

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Connection Error:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something Else:", err)
    return wrapper