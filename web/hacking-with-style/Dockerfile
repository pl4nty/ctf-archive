FROM ghcr.io/puppeteer/puppeteer:22.6.4@sha256:a0e2b537f2f3eaea4ddce2da97972f458112b9f43be41fc3f4775b2b5de34e9d

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
