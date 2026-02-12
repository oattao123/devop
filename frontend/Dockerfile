# frontend/Dockerfile

FROM node:22-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

RUN npm run build

# ใน Production จริง เราอาจใช้ Container นี้แค่ Copy file ออกมา

# หรือใช้ Multi-stage เพื่อรัน Nginx/Caddy ในตัวก็ได้

# แต่ใน Lab นี้เราจะใช้ Caddy หลักตัวเดียวในการ mount volume

CMD ["echo", "Build Complete"]