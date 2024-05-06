FROM ghcr.io/puppeteer/puppeteer:22.8.0@sha256:3ca4940d7d79084d1212a33e647bbae6e1bcc54672deb242555e266a83001de1

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
