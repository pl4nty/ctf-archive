FROM ghcr.io/puppeteer/puppeteer:19.11.1@sha256:1055a530495260018e13e192cb66f80eeb5fefc8ca61fb41e5cf352976dd2dab

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
