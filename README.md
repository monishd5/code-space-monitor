# Code-Space Monitor

This is a simple Flask application that provides system monitoring data via an HTTP endpoint.

## Features
- Displays system information using the `top` command.
- Shows server time in IST (Indian Standard Time).
- Runs inside a GitHub Codespace.

## Setup Instructions

### 1. Clone the Repository
```sh
 git clone https://github.com/your-username/code-space-monitor.git
 cd code-space-monitor
```

### 2. Install Dependencies
Make sure you have Python installed, then install Flask:
```sh
pip install flask pytz
```

### 3. Run the Flask App
```sh
python app.py
```

The application will start on port **5000**:
```
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
```

### 4. Access the Monitoring Endpoint
Once the server is running, access the endpoint:
```
http://localhost:5000/htop
```
This will display system monitoring details.

## Exposing Port 5000 in GitHub Codespaces
If running inside a **GitHub Codespace**, expose port **5000**:

```sh
gh codespace ports visibility 5000:public
```

If you get an error, try manually setting the port visibility in the Codespace UI:
1. Open your **GitHub Codespace**.
2. Go to **Ports** in the panel.
3. Find **5000**, click **Edit**, and set visibility to **Public**.

## Stopping the Server
Press `CTRL+C` to stop the Flask server.

## Troubleshooting
- If you get a **404 Not Found** error when accessing `/htop`, ensure the server is running.
- If the port isn’t exposed, manually configure it in **GitHub Codespaces Ports**.
- Restart the Codespace if visibility settings do not apply:
  ```sh
  gh codespace stop --codespace <YOUR_CODESPACE_NAME>
  gh codespace start --codespace <YOUR_CODESPACE_NAME>
  ```

## License
This project is open-source. Feel free to modify and use it.

---
Developed by **Monish D** 🚀

