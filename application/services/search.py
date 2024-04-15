import requests, webbrowser, tempfile, sys

def upload_image(image_path):
    upload_url = "https://api.imgbb.com/1/upload"
    params = {
        "key": "a89b360a3b703a4ab2f7cfba78e09922", #debug key
        "expiration": 60
    }
    files = {"image": open(image_path, "rb")}
    response = requests.post(upload_url, params=params, files=files)
    json_response = response.json()
    if response.status_code == 200 and json_response["success"]:
        return json_response["data"]["url"]
    else:
        return None

def google_image():
    image_url = upload_image(f"{tempfile.gettempdir()}/screenshot.png")
    final_url = f"https://lens.google.com/uploadbyurl?url={image_url}"

    webbrowser.open(final_url)
