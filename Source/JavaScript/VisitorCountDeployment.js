console.log('Loading function');
var AWS = require('aws-sdk');
var lambda = new AWS.Lambda();
exports.handler = function(event, context) {
    key = event.Records[0].s3.object.key
    bucket = event.Records[0].s3.bucket.name
    version = event.Records[0].s3.object.versionId
    if (bucket == "lambdaks" && key == "lambda_function.zip" && version) {
        var functionName = "website-VisitorCountFunction-bKsILjPb0g1T";
        console.log("uploaded to lambda function: " + functionName);
        var params = {
            FunctionName: functionName,
            S3Key: key,
            S3Bucket: bucket,
            S3ObjectVersion: version
        };
        lambda.updateFunctionCode(params, function(err, data) {
            if (err) {
                console.log(err, err.stack);
                context.fail(err);
            } else {
                console.log(data);
                context.succeed(data);
            }
        });
    } else {
        context.succeed("skipping zip " + key + " in bucket " + bucket + " with version " + version);
    }
};