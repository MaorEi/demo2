FROM ubuntu:latest

# ==== CONFIGURE =====
# Use a Node 20 base image
FROM node:20-alpine
# Set the working directory to /frontend inside the container
WORKDIR /frontend
# Copy frontend files
COPY . .
# ==== BUILD =====
# Install dependencies (npm ci makes sure the exact versions in the lockfile gets installed)
RUN npm ci
# Build the app
RUN npm run build
# ==== RUN =======
# Set the env to "production"
ENV NODE_ENV production
# Expose the port on which the app will be running (3000 is the default that `serve` uses)
EXPOSE 3000
# Start the app
CMD [ "npm", "run", "start" ]