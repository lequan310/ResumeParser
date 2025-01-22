# Build the app
FROM oven/bun:alpine AS build

WORKDIR /app
COPY package.json bun.lock ./

RUN bun install

COPY . .
RUN bun run build

# Deploy the app - copy the build files to the nginx server
FROM nginx:stable-alpine-slim

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]