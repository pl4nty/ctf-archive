FROM ghcr.io/puppeteer/puppeteer:22.6.1@sha256:2ad270688c06369e73718cf2cb72ef2d462ba55a4d41542c644ab74852d8367d

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
