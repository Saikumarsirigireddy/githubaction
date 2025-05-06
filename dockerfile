# Use AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.8

# Copy application files
COPY demo.py . 

# Install dependencies
RUN pip install rich

# Set command for Lambda handler
CMD ["app.lambda_handler"]
