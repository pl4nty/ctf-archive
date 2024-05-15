FROM ghcr.io/puppeteer/puppeteer:22.8.2@sha256:344f509553cdd34cdc59cc7dbe7c13e647fdb539ada5f543c52d4275ab20c777

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
