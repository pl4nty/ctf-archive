FROM ghcr.io/puppeteer/puppeteer:19.7.1@sha256:74a60ede6a5b3221082a5f7c61d37b139c9627aa9dcc9d61d6dabc0ef72d76ee

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
