FROM ghcr.io/puppeteer/puppeteer:22.7.1@sha256:ad0e950173405dd0a9289014cf4aebd6efc08b041feb4d08d3a8b96443b36fb1

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
