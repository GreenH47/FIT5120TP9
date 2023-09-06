sudo apt-get update
sudo apt install python3-virtualenv
virtualenv mysql_test
source mysql_test/bin/activate
python3 --version  
sudo apt install python3-pip
python3 -m pip install --upgrade pip
mkdir -p lambda_layers/python/lib/python3.8/site-packages
cd lambda_layers/python/lib/python3.8/site-packages

pip install mysql-connector-python -t .
cd ~/lambda_layers
sudo apt install zip
zip -r mysql_lambda_layer.zip *

sudo apt install awscli
aws configure
aws s3 cp  mysql_lambda_layer.zip s3://{}/