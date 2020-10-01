FROM brunneis/python

RUN \
  apt-get update \
  && apt-get install -y \
     haproxy \
  && mkdir /opt/proxy-balancer \
  && apt-get clean \
  && pip install --upgrade pip \
  && pip install \
     lxml \
  && rm -rf /root/.cache/pip \
  && find / -type d -name __pycache__ -exec rm -r {} \+

COPY \
  get_proxies.py \
  haproxy.cfg.template \
  update-haproxy.sh \
  entrypoint.sh /opt/proxy-balancer/

WORKDIR /opt/proxy-balancer
ENTRYPOINT /opt/proxy-balancer/entrypoint.sh