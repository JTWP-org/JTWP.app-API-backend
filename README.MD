# Flask API Project


## How to Use

### 1. Install Dependencies

Install the required Python packages using pip:

```bash
pip install flask pandas python-dotenv
```


### 2. allow port 5000 through firewall

```bash
sudo allow ufw 5000
```


### 3. Configure Environment Variables and build CURL cmds for POST events

Create a file named `.env` in your project folder with the api key (make your own or use the bash script to Generate a 32-byte random string and encode it in hexadecimal )
Update (or create) your .env file with the new key. and build the .built_curls.md with updated CURL cmds to be used in UE5 logic (note this file is hidden as it has API key ):

```bash
./setupScripts/makeKey.sh 
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

