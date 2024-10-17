import base64

with open("assets/folder.png", "rb") as img_file:
    # Read the binary content and encode it in Base64
    encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
    print(f'data:image/png;base64,{encoded_string}')
