# Flask API Project

## Project Structure

Your project directory might look like this:

```
/project_folder
  |-- config.json
  |-- .env
  |-- csv_init.py
  |-- api_key.py
  |-- get_endpoints.py
  |-- main_api.py
  |-- setup_service.sh      # (Optional: Bash script to set up a systemd service)
```

## How to Use

### 1. Install Dependencies

Install the required Python packages using pip:

```bash
pip install flask pandas python-dotenv
```

### 2. Configure Environment Variables

Create a file named `.env` in your project folder with the following content (replace the API key with your actual key):

```ini
API_KEY={KEY}
```



### 4. Initialize CSV Files

Run the CSV initialization script to create the necessary CSV files (if they don’t exist):

```bash
python csv_init.py
```

### 5. Run the API

Start the API server by running:

```bash
python main_api.py
```

Your API will now be running on port 5000.

### 6. Setting Up as a Service (Optional)

If you want your API to run as a background service on a Linux system, use the provided `setup_service.sh` script. First, make the script executable and then run it with sudo:

```bash
sudo chmod +x setup_service.sh
sudo ./setup_service.sh
```

This script creates a systemd service for your API, reloads systemd, enables the service at boot, and starts it immediately.

### 7. Testing the API

You can use the provided curl commands (see `api_commands.md` for details) to test the different endpoints.

## Endpoints

The API exposes the following endpoints:

- **POST /api/submit_death**: Submit a death event.
- **POST /api/submit_killer**: Submit a killer event.
- **POST /api/submit_teamkill**: Submit a teamkill event.
- **POST /api/submit_kys**: Submit a KYS event.
- **POST /api/submit_join**: Submit a join event.
- **POST /api/submit_left**: Submit a left event.

Optional GET endpoints are available to retrieve the stored events from each CSV file.

---

Follow these steps to set up, run, and test your API. For additional configuration or modifications, refer to the corresponding module files in your project.
```

Simply copy and paste the above content into a file named `README.md` in your project directory. This README file will guide users through the setup and usage of your Flask API project.
