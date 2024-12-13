# Blog Generation with AWS Bedrock

This project demonstrates how to generate blog content using the AWS Bedrock service. It includes two main scripts:

- **`bedrock_testing.py`**: A script to test the AWS Bedrock model by generating a short poem about AI.
- **`app.py`**: A Lambda function that generates blog posts based on a specified topic and saves the content to an S3 bucket.

## Getting Started

To use this project, ensure you have an AWS account with access to the Bedrock and S3 services. You will also need Python and the Boto3 library installed.

## Prerequisites

- Python 3.x
- Boto3 library (install using `pip install boto3`)

## Usage

1. **Run `bedrock_testing.py`** to test the model directly.
2. **Deploy `app.py`** as an AWS Lambda function to generate blog content based on user input.

## License

This project is licensed under the MIT License.

