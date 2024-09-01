# Ubuntu 22.04 (jammy)
# https://hub.docker.com/_/ubuntu/tags?page=1&name=jammy
ARG ROOT_CONTAINER=ubuntu:22.04

FROM $ROOT_CONTAINER

LABEL maintainer="Bitcoin Parse Project <dsiegmann@bluewin.ch>"
ARG RDB_USER="parser"
ARG RDB_GRP="users"
ARG RDB_UID="1005"
ARG RDB_GID="100"
ARG PYTHON_VERSION=3.11
ARG HOME="/home/${RDB_USER}"


SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update --yes && \
  apt-get upgrade --yes && \
  apt-get install --yes --no-install-recommends \
  bash \
  nano \
  cron \
  git \
  wget \
  screen \
  g++ \
  python3 \
  python3-dev gcc \
  python3-dev \
  python3-pip \
  python3.10-venv \
  librocksdb-dev \
  libsnappy-dev \
  libleveldb-dev \
  zlib1g-dev \
  libbz2-dev \
  liblz4-dev \
  bzip2 \
  ca-certificates \
  locales \
  sudo \
  wget && \
  apt-get clean && rm -rf /var/lib/apt/lists/* && \
  echo "de_DE.UTF-8 UTF-8" > /etc/locale.gen && \
  locale-gen
  
RUN pip3 install requests && \
     pip3 install virtualenv && \
     pip3 install py3-rocksdb && \
     pip3 install blockchain-parser-1.0 && \
     pip3 install pandas && \
     pip3 install subprocess.run && \
     pip3 install base58 && \
     pip3 install Crypto && \
     pip3 install pycryptodome && \
     pip3 install ripemd-hash && \
     pip3 install ecdsa && \
     pip3 install bech32 && \
     pip3 install psutil && \
     pip3 install tqdm && \
     pip3 install chardet && \
     pip3 install bech32m

  
COPY fix-permissions /usr/local/bin/fix-permissions
RUN chmod 0755 /usr/local/bin/fix-permissions

# Create RDB_USER with name worker user with UID=1005 and in the 'users' group
RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    sed -i.bak -e 's/^%worker/#%users/' /etc/sudoers && \
    sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers && \
    groupmod -g "${RDB_GID}" ${RDB_GRP} && \
    useradd --no-log-init --create-home --shell /bin/bash -g ${RDB_GRP} -u ${RDB_UID} ${RDB_USER} && \
    fix-permissions "/home/${RDB_USER}"

# Setup work directory for backward-compatibility
RUN mkdir "/home/${RDB_USER}/scripts" && \
  mkdir "/home/${RDB_USER}/data" && \
  mkdir "/home/${RDB_USER}/node" && \
  chown -R ${RDB_USER}:${RDB_GRP} /home/${RDB_USER}/data && \
  chown -R ${RDB_USER}:${RDB_GRP} /home/${RDB_USER}/node && \
  chown -R ${RDB_USER}:${RDB_GRP} /home/${RDB_USER}/scripts && \ 
  fix-permissions "/home/${RDB_USER}"

# Copy local files as late as possible to avoid cache busting
COPY cron_job.sh /home/parser/
RUN chmod 0775 /home/parser/cron_job.sh && \
   chown ${RDB_USER}:${RDB_GRP} /home/parser/cron_job.sh

COPY start.sh /usr/local/bin/
RUN chmod 0777 /usr/local/bin/start.sh

RUN chmod gu+rw /var/run
RUN chmod gu+s /usr/sbin/cron
  
ENTRYPOINT ["/usr/local/bin/start.sh"]
CMD ["-f","/dev/null"]
  
COPY cronfile /etc/cron.d/cronfile
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile

RUN fix-permissions /var/spool/cron/crontabs

# Switch back to worker to avoid accidental container runs as root
# USER ${RDB_USER}

WORKDIR "${HOME}"

