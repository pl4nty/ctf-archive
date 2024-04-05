FROM ghcr.io/puppeteer/puppeteer:22.6.3@sha256:dbeeaeed53755c65c716e2743c347a1c9d9b6f0a080c727c8c0b6efb5a4a99a1

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
