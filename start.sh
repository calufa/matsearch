export ARG=${1}
FILE_PATH="${ARG}/start.yaml"

function cleanup {
	docker-compose -f ${FILE_PATH} down
	docker rm -f $(docker ps -a -q)
}

trap cleanup EXIT
cleanup

docker-compose -f ${FILE_PATH} build main
docker-compose -f ${FILE_PATH} run \
	--name matsearch \
	--service-ports \
	main
