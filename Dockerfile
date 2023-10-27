# Use the official PostgreSQL image from DockerHub
FROM postgres

# Set environment variables (you can change these if needed)
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase