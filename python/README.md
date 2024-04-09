# Python Client for Zynq UltraScale devices

This is a Sonora Client targetting a Envoy deployment on a Zynq UltraScale device (ARM64).  

# Steps
```

# Host Machine (tested with Python 3.11)
pip install grpcio-tools sonora
cd python
python -m grpc_tools.protoc --proto_path=<full path to>\grpc\gateway\examples\echo --python_out=. --grpc_python_out=. echo.proto

# Target Machine (tested with PYNQv3, RFSoC4x2)
# Install grpc-web Envoy and gRPC server onto the Zynq UltraScale device


docker build --platform linux/arm64 -t grpcweb/node-server -f net/grpc/gateway/docker/node_server/Dockerfile .
docker build --platform linux/arm64 -t grpcweb/envoy -f net/grpc/gateway/docker/envoy/Dockerfile .

docker run -d -p 9000:9000 --name node-server grpcweb/node-server
docker run -d -p 192.168.3.1:8080:8080 --link node-server:node-server grpcweb/envoy


# Connection
# Connect the host machine to the Zynq UltraScale device over USB Gadgets (IP address will be 192.168.3.1)

# Run the echo demonstration
python sonoroa_echo_client.py


```