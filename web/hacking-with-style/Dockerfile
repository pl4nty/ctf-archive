# Use the official Node.js 18.x image as base image
FROM node:18

# Install the latest version of Chrome dev package and fonts to support major charsets
# Note: This installs the necessary libs to make the bundled version of Chromium that Puppeteer installs work.
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget=1.21.3-1 gnupg=2.2.40-1.1 \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg \
    && sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable=118.0.5993.88-1 libxss1=1:1.2.3-1 \
    fonts-ipafont-gothic=00303-23 fonts-wqy-zenhei=0.9.45-8 fonts-thai-tlwg=1:0.7.3-1 fonts-khmeros=5.0-9 fonts-kacst=2.01+mry-15 fonts-freefont-ttf=20211204+svn4273-2 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r pptruser && useradd -rm -g pptruser -G audio,video pptruser

# Set the user as "pptruser"
USER pptruser

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the image and install dependencies
COPY app/package*.json ./
RUN npm install

# Copy the rest of the application code to the image and build the app
COPY app ./
RUN npm run build

# Set the environment variable APP_ROOT to /app
ENV APP_ROOT=/app

# Expose port 8080
EXPOSE 8080

# Run "npm start" when the container starts
# Not sure why, but npm start invokes npm run build. caused permissions issues on CI-built images
CMD ["node", "dist/main.js"]
