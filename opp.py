from flask import Flask, render_template, Response
from mcstatus import JavaServer
import time

app = Flask(__name__)

server_address = "bgr-1.anjas.id:30485"

def get_player_data():
  try:
    server = JavaServer.lookup(server_address)
    status = server.status()
    return status.players.online, [player.name for player in status.players.sample] if status.players.sample else []
  except Exception as e:
    print(f"Error fetching player data: {e}")
    return None, None

def event_stream():
  while True:
    num_players, player_names = get_player_data()
    yield f"data: {{'num_players': {num_players}, 'player_names': {player_names}}}\n\n"
    time.sleep(5)  # Adjust update interval as needed

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/stream")
def stream():
  return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
  app.run(debug=True)  # For local development
