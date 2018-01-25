.PHONY: all init test test-verbose database schema lint run runbin runcoap

all: init

init:
	pip install --no-cache-dir --upgrade pip
	pip install --no-cache-dir -r requirements.txt

test:
	nose2 --with-coverage

test-verbose:
	nose2 -v --with-coverage

database:
	cp database/camera-db.json database/camera.db
	cp database/motion-db.json database/motion.db
	cp database/test-db.json database/test.db

schema:
	protoc --proto_path=schema --python_out=agent schema/usp-msg.proto
	protoc --proto_path=schema --python_out=agent schema/usp-record.proto

lint:
	find agent -name "*.py" | egrep -v 'usp_msg_pb2' | egrep -v 'usp_record_pb2' | xargs pylint || :

run:
	python3 -m agent.main -t test

runbin:
	python3 bin/agent.py -t test

runcoap:
	python3 bin/agent.py -t test -c --coap-port 15683
