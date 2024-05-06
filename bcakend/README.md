# How to Run Bcakend

### Create Python Environment (Recommended for Development)
```
python -m venv .
```

### Install Requirements
```
pip install -r requirements.txt
```

### Import Protobuf
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobs/game_protoc.proto
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
???
```