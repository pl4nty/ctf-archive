FROM ghcr.io/puppeteer/puppeteer:22.6.0@sha256:3892371cb1af53d9f9f129f41e8027a2bf04fe55b3a06b5c852cf5d0b73f1bb7

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
