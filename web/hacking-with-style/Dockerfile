FROM ghcr.io/puppeteer/puppeteer:22.8.1@sha256:47dfe51a5377b054c94cd7f48a655c39e0c16d58e1ca01a7beb392a40d664376

WORKDIR /app

COPY app/package*.json ./
RUN npm ci

COPY app ./
RUN npm run build

# npm start runs build from prestart
CMD ["node", "dist/main.js"]
EXPOSE 8080

ENV APP_ROOT=/app
