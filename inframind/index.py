import boto3
import yaml
from flask import Flask, request, render_template
app = Flask(__name__,template_folder='templates')
@app.route('/', methods =["GET", "POST"])
def hello():
    if request.method == "POST":
        with open("C:/Users/yesgo/Desktop/latest/v2.yaml") as f:
            data = yaml.load(f)
        data['Parameters']['KeyName']['Default'] = request.form.get("Keypair")
        data['Parameters']['DBUser']['Default'] = request.form.get("Dbuser")
        data['Parameters']['DBPassword']['Default'] = request.form.get("Dbpass")
        data['Parameters']['DBRootPassword']['Default'] = request.form.get("Dbroot")
        data['Parameters']['InstanceType']['Default'] = request.form.get("Itype")
        # print(data['Parameters']['KeyName']['Default'])
        client = boto3.client('cloudformation',
            region_name = 'ap-south-1',
            aws_access_key_id='AKIA3HGFH4DA7LKRXVHE',
            aws_secret_access_key='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')
        response = client.create_stack(
            StackName="test",
            TemplateBody=yaml.dumps(data),
            DisableRollback=False,
        )
    return render_template("front.html")
if __name__ == '__main__':
    app.run()



