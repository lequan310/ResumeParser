# Build the app
FROM node:current-alpine3.21 AS build

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

# Deploy the app - copy the build files to the nginx server
FROM nginx:stable-alpine-slim

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]