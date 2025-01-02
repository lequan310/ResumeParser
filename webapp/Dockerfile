# Build the app
FROM node:current-alpine3.21 AS build

RUN npm install -g pnpm

WORKDIR /app
COPY package.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .
RUN pnpm run build

# Deploy the app - copy the build files to the nginx server
FROM nginx:stable-alpine-slim

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]