# backend dockerfile
FROM python:3
WORKDIR /app

# Copy the requirements file and install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . ./
# Run migrations
RUN python manage.py migrate --noinput
# Collect static files
RUN python manage.py collectstatic --noinput



# Expose the port for the Django application
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
