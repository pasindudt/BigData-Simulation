# Use the official Node.js 14 image as the base image
FROM node:14

# Set the working directory inside the container to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Serve the application using a production-ready server (e.g., serve)
RUN npm install -g serve
CMD ["serve", "-s", "build"]

# Expose the port on which the app will run (default is 5000 for serve)
EXPOSE 5000
