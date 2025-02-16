# API Curl Commands
DEATH

curl -X POST http://23.139.82.77:5000/api/submit_death \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cf041bae502a8b73340df45377e9e817" \
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

KILL

curl -X POST http://23.139.82.77:5000/api/submit_killer \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cf041bae502a8b73340df45377e9e817" \
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

TEAMKILL

curl -X POST http://23.139.82.77:5000/api/submit_teamkill \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cf041bae502a8b73340df45377e9e817" \
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

KYS

curl -X POST http://23.139.82.77:5000/api/submit_kys \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cf041bae502a8b73340df45377e9e817" \
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

JOIN

curl -X POST http://23.139.82.77:5000/api/submit_join \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cf041bae502a8b73340df45377e9e817" \
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

LEFT

curl -X POST http://23.139.82.77:5000/api/submit_left \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cf041bae502a8b73340df45377e9e817" \
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

