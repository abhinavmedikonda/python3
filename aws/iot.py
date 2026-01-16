import json
import time
import os
from awsiot import mqtt5_client_builder, mqtt5

import psutil # 3rd party
def get_cpu_percent():
    return psutil.cpu_percent(interval=1)

def get_memory_percent():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage_percent():
    disk = psutil.disk_usage("/")
    return disk.percent

def get_network_stats():
    net = psutil.net_io_counters()
    return {
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv
    }

def main():

    client = mqtt5_client_builder.mtls_from_path(
        endpoint="a33zf4phy2n7a7-ats.iot.us-east-1.amazonaws.com",
        cert_filepath=os.path.expanduser("~/.ssl/device-certificate.crt"),
        pri_key_filepath=os.path.expanduser("~/.ssl/device-private.key"),
        ca_filepath=os.path.expanduser("~/.ssl/root-CA.crt"),
        client_id="mac"
    )

    # Start MQTT5 connection (sync call)
    client.start()

    print("Started AWS IoT MQTT5 Client. Publishing every 10 seconds…")

    while True:
        metrics = {
            "cpu_percent": get_cpu_percent(),
            "memory_percent": get_memory_percent(),
            "disk_percent": get_disk_usage_percent(),
            "network": get_network_stats()
        }

        payload = json.dumps(metrics)

        # Publish using MQTT5 PublishPacket
        client.publish(
            mqtt5.PublishPacket(
                topic="mac/performance",
                payload=payload.encode("utf-8"),
                qos=mqtt5.QoS.AT_LEAST_ONCE
            )
        )

        print("Published:", metrics)

        time.sleep(10)  # Publish every 10 seconds

    # (never reached, but good practice)
    client.stop()

if __name__ == "__main__":
    main()
