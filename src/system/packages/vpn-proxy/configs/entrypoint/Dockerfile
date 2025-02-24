FROM debian:latest

RUN apt-get update && apt-get install -y wireguard iproute2 iptables

COPY configs/entrypoint/wg0.conf /etc/wireguard/wg0.conf

ENTRYPOINT ["wg-quick", "up", "wg0"]