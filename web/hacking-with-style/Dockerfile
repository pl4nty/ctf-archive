FROM ghcr.io/puppeteer/puppeteer:22.5.0@sha256:3e3cf3aeac42f61000c255ac82910c3141d11cda20f911d2686e17817fd21aa8

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
