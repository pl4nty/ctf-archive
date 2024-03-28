FROM ghcr.io/puppeteer/puppeteer:22.6.2@sha256:8679b23599a6e75f38ed611c0a059f3338b16517628de8d92b5dcb9f81287b14

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
