# Flask API Project

<hr>


```markdown
API PATH: http://jtwp.app:5000

# Current Plan

The backend will receive POST requests from the mod containing information about various events.
The current events include:

- **Join Server**
- **Leave Server**
- **Player Spawned**
- **Player Killed Someone**
  - Validate that the kill is valid (i.e., not a team kill or a suicide)
- **Player Death**
  - Validate that the death is valid (i.e., not a team kill)

Based on these events, statistics will be calculated and stored. When a GET request is made by the
mod or a Discord bot, the stats will be compiled into JSON objects organized by player. For each 
player, a JSON file containing their statistics will be generated, and the API will return that JSON
when requested.

## Statistics Collected

The following statistics are currently being collected more are planned to be added :

- **KILLS**
- **DEATHS**
- **CONNECTIONS**
- **TEAMKILLS**
- **SUICIDES**
- **HEADSHOTS**
- **PLAYER KILLED THE MOST**
- **PLAYER DIED TO THE MOST**
- **GUN USED THE MOST**


```
</hr>


Project Structure

Your project directory should now look like this:

```markdown
/project_folder 
    |-- config.json 
    |-- .env 
    |-- main_api.py 
    |-- math/ 
        |-- kills.py 
        |-- deaths.py 
        |-- tempOut/ 
            |-- kills.json 
            |-- deaths.json
    |-- scripts/ 
        |-- csv_init.py 
        |-- api_key.py 
        |-- get_endpoints.py 
    |-- data/
        |-- death_events.csv 
        |-- join_events.csv 
        |-- killer_events.csv 
        |-- kys_events.csv 
        |-- left_events.csv 
        |-- join_events.csv
```


## How to Use

### 1. Install Dependencies / allow port / perms

<p>
Install the required Python packages using pip:
</p>

```bash
pip install flask pandas python-dotenv
sudo ufw allow 5000
sudo chmod +x makeService.sh
sudo chmod +x makeKey.sh
```

### 2.Generate or Update API Keys 

Your setup scripts are located in the setupScripts/ folder.

<p>
    Generate a new primary API key (if you choose to).
    Update the .env file with the new key.
    Create or update a hidden Markdown file with curl commands (located at docs/.curl_commands.md), replacing any placeholder with the new key.
    Optionally generate and append a secondary API key to a secondary key file for outside api request .
<p>

```bash
bash setupScripts/makeKey.sh
```


### 3. Run the API

<p>
Start the API server by running:
    Your API will now be running on port 5000.
</p>

```bash
python main_api.py
```



<hr>

### 4 (FOR DEBUG)
3. Initialize CSV Files

<p>
The CSV files are automatically initialized when you run the API. However, if you wish to run the initialization separately, execute:
This will create the necessary CSV files inside the data/ folder if they do not already exist.
</p>

```bash
python scripts/csv_init.py
```



### 5. Setting Up as a Service (Optional)

<p>
If you want your API to run as a background service on a Linux system, use the provided `setup_service.sh` script. First, make the script executable and then run it with sudo:
This script creates a systemd service for your API, reloads systemd, enables the service at boot, and starts it immediately.
</p>

```bash
sudo chmod +x setup_service.sh
sudo ./setup_service.sh
```



### 6. Testing the API

You can use the provided curl commands (see `api_commands.md` for details) to test the different endpoints.

<p>

## Endpoints

The API exposes the following endpoints:

```http
- **POST /api/submit_death**: Submit a death event.
- **POST /api/submit_killer**: Submit a killer event.
- **POST /api/submit_teamkill**: Submit a teamkill event.
- **POST /api/submit_kys**: Submit a KYS event.
- **POST /api/submit_join**: Submit a join event.
- **POST /api/submit_left**: Submit a left event.
```
Optional GET endpoints are available to retrieve the stored events from each CSV file.

</p>

