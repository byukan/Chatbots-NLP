# install dependencies
FROM node:alpine as builder
WORKDIR '/app'
COPY package.json .
RUN npm install
# since we're in build and not concerened with changing source code and don't need to create volume mappings
COPY . .
RUN npm run build

# /app/build is going to contain all the files we care about

# previous block complete, start new block
FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html
# default command of nginx starts the server