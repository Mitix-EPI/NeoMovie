FROM node:12.2.0-alpine as build

MAINTAINER alexandre.juan@epitech.eu

WORKDIR /app

COPY ./NeoMovie/ ./

RUN npm install
RUN npm run build --prod

FROM nginx:1.16.0-alpine

COPY --from=build /app/dist/NeoMovie /usr/share/nginx/html

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]