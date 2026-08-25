FROM node:20-alpine

WORKDIR /usr/src/app

RUN addgroup app && adduser -S -G app app

COPY package*.json ./
RUN npm install

COPY . .

HEALTHCHECK CMD wget --spider -q http://localhost:3000/health || exit 1

USER app

CMD ["node", "server.js"]
