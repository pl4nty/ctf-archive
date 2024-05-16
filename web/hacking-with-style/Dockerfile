FROM ghcr.io/puppeteer/puppeteer:22.9.0@sha256:e35ec9f1bbb5bdbc15c87630b36460339a3ae324cdf135c6670ff1fa696d8bb0

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
