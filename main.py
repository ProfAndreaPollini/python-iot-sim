from flask import Flask

from sim.toggle import ToggleSensor
from sim.sensor import Sensor

app = Flask(__name__)

sensors = [
    ToggleSensor(id="s-01", description="lampadina"),
    ToggleSensor(id="s-02", description="lampadina"),
    ToggleSensor(id="s-03", description="allarme atomico"),
    ToggleSensor(id="s-04", description="porta aperta"),
    Sensor(id="temperature-01", description="sensore di temperatura"),
    Sensor(id="umidita-01", description="sensore di umiditá"),
    Sensor(id="cleancode-01", description="sensore di bellezza del codice"),
    Sensor(id="luce-01", description="sensore di luce"),
]


def search_index_by_id(sensor_id: str):
    for pos, sensor in enumerate(sensors):
        if sensor.id == sensor_id:
            return pos

    return -1


@app.route("/<sensor_id>", methods=["GET"])
def sensor_details(sensor_id):
    sensor_pos = search_index_by_id(sensor_id)
    if sensor_pos >= 0:
        return {"sensor": sensors[sensor_pos]}
    else:
        return {"kind": "error", "payload": f"Sensor {sensor_id} not found"}


@app.route("/<sensor_id>/toggle", methods=["PUT"])
def set_sensor_value(sensor_id: str):
    sensor_pos = search_index_by_id(sensor_id)
    if sensor_pos >= 0 and isinstance(sensors[sensor_pos], ToggleSensor):
        sensors[sensor_pos].toggle()
    return {"kind": "error", "payload": f"Sensor {sensor_id} not found"}


@app.route("/", methods=["GET"])
def hello_world():
    for sensor in sensors:
        sensor.update()
    return {"sensors": sensors}
