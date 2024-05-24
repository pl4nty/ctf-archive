FROM ghcr.io/puppeteer/puppeteer:22.10.0@sha256:c05550e4a984ae2db55cd469240ae92ad605472756439091adb670c29e85c90e

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
