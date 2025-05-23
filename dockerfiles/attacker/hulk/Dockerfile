# Source repository:
FROM golang:1-bookworm

WORKDIR /hulk

RUN git clone https://github.com/grafov/hulk . && go build

ENTRYPOINT ["sh", "-c"]
