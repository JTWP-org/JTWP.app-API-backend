# Flask API Project

Project Structure

Your project directory should now look like this:
```markdown
/project_folder |-- config.json |-- .env |-- main_api.py |-- scripts/ |-- csv_init.py |-- api_key.py |-- get_endpoints.py |-- data/
|-- death_events.csv |-- join_events.csv |-- killer_events.csv |-- kys_events.csv |-- left_events.csv |-- join_events.csv
```

## How to Use

### 1. Install Dependencies

Install the required Python packages using pip:

```bash
pip install flask pandas python-dotenv
```

### 2.Generate or Update API Keys 

Your setup scripts are located in the setupScripts/ folder.

    Generate or Update API Key
    Run the script to generate a new primary API key or add a secondary key. For example:

```bash
./setupScripts/make_key.sh
```

This script will:

    Generate a new primary API key (if you choose to).
    Update the .env file with the new key.
    Create or update a hidden Markdown file with curl commands (located at, for example, docs/.curl_commands.md), replacing any placeholder with the new key.
    Optionally generate and append a secondary API key to a secondary key file.


### 3 (FOR DEBUG)
3. Initialize CSV Files

The CSV files are automatically initialized when you run the API. However, if you wish to run the initialization separately, execute:

```bash
python scripts/csv_init.py
```

This will create the necessary CSV files inside the data/ folder if they do not already exist.

### 4. Run the API

Start the API server by running:

```bash
python main_api.py
```

Your API will now be running on port 5000.

<hr>

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
