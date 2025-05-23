FROM python:3.12-slim AS compiler

WORKDIR /app/
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

FROM python:3.12-slim AS runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
RUN apt-get update
RUN mkdir -p /var/lib/apt/lists/partial
RUN apt --force-yes -y install libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx libu2f-udev \
    fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libdrm2 libgbm1 libgtk-3-0 \
    libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxkbcommon0 \
    libxrandr2 xdg-utils wget libcurl4
RUN wget -O driver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz && tar -xvf driver.tar.gz && chmod +x geckodriver && mv geckodriver /usr/local/bin

COPY main.py bruteforce.py xss.py sqli.py /app/
COPY files/* /app/files/

ENTRYPOINT ["python", "-u", "main.py"]