FROM python AS base
RUN curl https://cmake.org/files/v3.12/cmake-3.12.0-rc3.tar.gz -o cmake-3.12.0-rc3.tar.gz \
    && tar -xvf cmake-3.12.0-rc3.tar.gz \
    && cd cmake-3.12.0-rc3 \
    && ./bootstrap \
    && make \
    && make install \
    && cp -r bin /usr/ \
    && cp -r share /usr/ \
    && cp -r doc /usr/share/ \
    && cp -r man /usr/share/
WORKDIR /server
COPY . /server
RUN pip install pipenv \
    && pipenv install
ENTRYPOINT pipenv run python server.py