FROM ghcr.io/puppeteer/puppeteer:22.4.1@sha256:f0e5c33fbfe1f7db60fc63e225c232915e130c7ac2c0c9c09bbedbcbf81f8427

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
