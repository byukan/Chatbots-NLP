# Specify a base image
FROM node:alpine

WORKDIR /usr/app

# Install some dependencies
# With this build process, if you make changes to index.js, you won't have to reinstall all the dependencies again.
# You won't invalidate the cache for parts taht are working.
# Split the copy operation out into 2 different steps
# npm install only cares about the package.json file
COPY ./package.json ./
RUN npm install 
COPY ./ ./

# Default command
CMD ["npm", "start"]