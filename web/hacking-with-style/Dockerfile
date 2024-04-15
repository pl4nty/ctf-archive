FROM ghcr.io/puppeteer/puppeteer:22.6.5@sha256:8542506017190515ced6255c0067dd8747dcf3a3b680261a521ca8338357fb5c

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
