FROM ghcr.io/puppeteer/puppeteer:22.7.0@sha256:f44db3c6903cadf4885cf261f8868d4e0477347ef8a2454550ba272d8398bcbc

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
