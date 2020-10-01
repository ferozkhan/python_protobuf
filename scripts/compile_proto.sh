#!/usr/bin/env bash
# --proto_path=src --python_out=build/gen src/foo.proto src/bar/baz.proto
protoc --proto_path=../app/protos --python_out=../app/protos/ ../app/protos/message.proto
