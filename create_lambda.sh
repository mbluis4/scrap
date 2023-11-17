 aws lambda create-function --function-name getPrices --runtime python3.10 --handler lambda_handler.lambda_handler --role arn:aws:iam::679602148783:role/faucets-role --zip-file fileb://my_deployment_package.zip

 #update

 aws lambda update-function-code --function-name getPrices --zip-file fileb://my_deployment_package.zip

 # create api gateway

aws apigatewayv2 create-api --name faucets-api --protocol-type HTTP --target arn:aws:lambda:us-east-1:679602148783:function:getPrices