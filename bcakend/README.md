# How to Run Bcakend

### Create Python Environment (Recommended for Development)
```
python -m venv .
```

### Activate Virtual environment (Windows)
```
./Scripts/activate
```

### Install Requirements
```
pip install -r requirements.txt
```

### Import Protobuf
```
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. protobs/game_protoc.proto
```

### Run Docker for Database
```
docker compose up -d
```

### Migrate Database
```
prisma migrate dev --schema ./prisma/schema.prisma
```

### Run Server
```
python .\grpc_server.py
```

### Client Test
```
python .\grpc_client_test.py
```

then pick the selection