# Simple Navbar
This is a simple navbar implemented as a Python app using http.server and urllib.parse.

## Running the app
To run the app, execute the following command:
```bash
PORT=8080 python main.py
```
Replace `8080` with the desired port number.

## Cloud Run compatibility
The app is designed to be compatible with Cloud Run. The `PORT` environment variable is used to determine the port number to listen on.