
docker build -t docker-ml-model -f Dockerfile .

docker run docker-ml-model python3 inference.py
