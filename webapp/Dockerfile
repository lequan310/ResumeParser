# Build the app
FROM node:current-alpine3.21 AS build

RUN npm install -g bun

WORKDIR /app
COPY package.json bun.lock ./

RUN bun install --frozen-lockfile

COPY . .
RUN bun run build

# Deploy the app - copy the build files to the nginx server
FROM nginx:stable-alpine-slim AS deploy

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]