<h1># API Curl Commands</h1>

## DEATH

```bash
curl -X POST http://jtwp.app:5000/api/submit_death \
  -H "Content-Type: application/json" \
  -H "X-API-Key: API_KEY_HERE" \
  -d '{
        "deathEvent": {
          "timeStamp": "2025-02-14T12:34:56",
          "eventDetail": [
            {
              "name": "PlayerB",
              "clan": "ClanX",
              "killer": "PlayerA",
              "headshot": true,
              "item": "AK47"
            }
          ],
          "stats": [
            {
              "cash": 0,
              "armor": 0,
              "health": 0,
              "score": 0,
              "killedAtLoc": "A1",
              "levelname": "Map1"
            }
          ]
        }
      }'
```

---

## KILL

```bash
curl -X POST http://jtwp.app:5000/api/submit_killer \
  -H "Content-Type: application/json" \
  -H "X-API-Key: API_KEY_HERE" \
  -d '{
        "killerEvent": {
          "timeStamp": "2025-02-14T12:35:00",
          "eventDetail": [
            {
              "name": "PlayerA",
              "clan": "ClanX",
              "victim": "PlayerB",
              "headshot": true,
              "item": "AK47"
            }
          ],
          "stats": [
            {
              "cash": 0,
              "armor": 0,
              "health": 0,
              "score": 0,
              "killedAtLoc": "A1",
              "levelname": "Map1"
            }
          ]
        }
      }'
```

---

## TEAMKILL

```bash
curl -X POST http://jtwp.app:5000/api/submit_teamkill \
  -H "Content-Type: application/json" \
  -H "X-API-Key: API_KEY_HERE" \
  -d '{
        "teamKillEvent": {
          "timeStamp": "2025-02-14T12:40:00",
          "eventDetail": [
            {
              "name": "PlayerX",
              "clan": "ClanY",
              "killed": "PlayerZ",
              "headshot": true,
              "item": "AK47"
            }
          ],
          "stats": [
            {
              "cash": 0,
              "armor": 0,
              "health": 0,
              "score": 0,
              "killedAtLoc": "B2",
              "levelname": "Map3"
            }
          ]
        }
      }'
```

---

## KYS

```bash
curl -X POST http://jtwp.app:5000/api/submit_kys \
  -H "Content-Type: application/json" \
  -H "X-API-Key: API_KEY_HERE" \
  -d '{
        "kysEvent": {
          "timeStamp": "2025-02-14T12:50:00",
          "eventDetail": [
            {
              "name": "PlayerC",
              "clan": "ClanZ",
              "item": "AK47"
            }
          ],
          "stats": [
            {
              "cash": 0,
              "armor": 0,
              "health": 0,
              "score": 0,
              "killedAtLoc": "C3",
              "levelname": "Map4"
            }
          ]
        }
      }'
```

---

## JOIN

```bash
curl -X POST http://jtwp.app:5000/api/submit_join \
  -H "Content-Type: application/json" \
  -H "X-API-Key: API_KEY_HERE" \
  -d '{
        "joinEvent": {
          "timeStamp": "2025-02-14T13:00:00",
          "eventDetail": [
            {
              "name": "PlayerD",
              "clan": "ClanD"
            }
          ],
          "stats": [
            {
              "spawnedAtLoc": "D4",
              "levelname": "Map5"
            }
          ]
        }
      }'
```

---

## LEFT

```bash
curl -X POST http://jtwp.app:5000/api/submit_left \
  -H "Content-Type: application/json" \
  -H "X-API-Key: API_KEY_HERE" \
  -d '{
        "leftEvent": {
          "timeStamp": "2025-02-14T13:05:00",
          "eventDetail": [
            {
              "name": "PlayerD",
              "clan": "ClanD"
            }
          ],
          "stats": [
            {
              "lastAtLoc": "D5",
              "levelname": "Map5"
            }
          ]
        }
      }'
```


