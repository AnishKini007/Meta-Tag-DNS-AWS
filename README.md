# Welcome to your CDK Meta Tag project!

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

Pre-Requisites: U need to have CDK installed and AWS credentials configured to deploy the app.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```
Deploy the app.

```
$ cdk deploy
```
You will recieve to endpoints which you can run on Postman.

Both the endpoints have to be run using the "POST" method.

The MetaApi has to given the "tags" token in the path to authenticate before sending a request i.e eg: https://ziw2svljx0.execute-api.us-east-1.amazonaws.com/prod/tags 

The DNSApi has to be given the "record" token in the path to authenticate before sending a request.

Input parameters:

```

DNSApi Key : domain , Value:eg: flipkart.com && Key: txtrecord , Value: eg: "clojars flipkartoss"

MetaApi Key: url , Value:eg: https://www.taskseveryday.com/ && Key: tag , Value: eg:description

```


You will see the responses of each api in the response section of postman.

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
