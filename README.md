# Cloud Resume Challenge

I wanted to pickup the Cloud Resume Challenge because it was a great chance for me to showcase my knowledge, and my ability to apply that knowledge in a useful example.

### HTML & CSS 

The first step of the challenge was converting my resume into HTML format so it can be available as a webpage. After creating the HTML webpage, I went on to style it using CSS to make the webpage more presentable.

### Hosting on AWS (S3, CloudFront, Route 53)

The next step is to host the resume website using AWS services. For that, I used Amazon S3 to host a static website. Once the website was set up, I used Amazon CloudFront to host the website securely using HTTPS, and also to make it available through edge locations for faster delivery. The following step was to register a DNS name for my website to be accessible by a name of my choosing. I used Amazon Route 53 to register a domain for my website. 

### Setting up visitor count (JavaScript, DynamoDB, API Gateway, Lambda, Python)

The next part of the project was setting up a visitor count on the website. At first, I created a JavaScript code to show a count on the website. Then I set up a DynamoDB database to store and retrieve the count into the website. In order for the JavaScript code and DynamoDB table to communicate, I set up an API gateway. Once that was set up, I created a Lambda function using Python to update the count in the DynamoDB table. 

### CloudFormation and Testing

Instead of setting up all these services manually, it is best to automate the process using AWS CloudFormation. Using a SAM template, I set up these services to be launched through CloudFormation automatically as infrastructure as code. I then set up testing for my Python code that will be used when I set up CI/CD in the next step.

### GitHub and CI/CD

I set up a GitHub repository to store all the files and code that I am using for this project. I then set up CI/CD through GitHub Actions for both my back-end and front-end code. This way whenever I make an update or a change to my CloudFormation template or Python code, it tests the code, and then automatically deploys it onto AWS. The same will happen if I make any updates to my website code, the S3 bucket will be updated automatically. 
