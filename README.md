# syndicate-tasks
##### 1. Create Virtual env
```
virtualenv .syndicate_venv -p python3
```

If you get not found error use:
```
pip3 install virtualenv
```

##### 2. Activate venv:
```
source .syndicate_venv/bin/activate
```

##### 3. Install syndicate:
```
pip3 install aws-syndicate
```

```
syndicate --version
```


##### 4. Generate Project:
```
syndicate generate project --name syndicate-quickstart-project
```
```
cd syndicate-quickstart-project/
```

Eg:
```
syndicate generate project --name task02
```

##### 5. Set Credentials:
```
syndicate generate config --name "dev" \
    --region "eu-central-1" \
    --bundle_bucket_name "syndicate-education-platform-custom-sandbox-artifacts-sbox02/d499ad33/task02" \
    --prefix "cmtr-d499ad33-" \
    --extended_prefix "true" \
    --tags "course_id:SEP_GL_7,course_type:stm,student_id:d499ad33,type:student" \
    --iam_permissions_boundary "arn:aws:iam::905418349556:policy/eo_role_boundary" \
    --access_key "######" \
    --secret_key "ORr+wBeKWTCAIx83ZIh/S0bfglToLte4o2GEJtW7" \
    --session_token "IQoJb3JpZ2luX2VjEKb//////////wEaCXVzLWVhc3QtMSJHMEUCIACvJEtzXgjnmr3P2fj00gBGcNRUsaw3qi7MTcRyrpx9AiEA0Jp4UaJSy61l/+bjnVfuOO5Rhn11viq5YvDMdMVmxXUq5gIIv///////////ARAAGgw5MDU0MTgzNDk1NTYiDC2e3u8PCQfrftcR6Sq6AnpdMc2AfiEjAnmefMVxgfyRFRdkvb8ENrCc49S64y+hg5IVj+JVcIktJYE5kE9eCEt7gMRSOFwyZiwVN1mCQqgjBFIHxg2tXNY84A3rz4zZcnBBym9vHMf1FLwJtjn7DIjmaWWxfkmbdTfOQ009yh8iSfBYzL8JhBYPMMv2vEZP6R7nx01lQGrBdzsSUDjE6PTKsP0H6BGE8EBMTBYbKb6ILdhy9vnNPDPaw4r3FoJY4k4Pu2cv/yblpP/O0RUycq/GvJUS7LmploPduxLBq6fr5Qg5yw/KgaxWtZUBOYd86F5r6j4HFC69G59tndTkduxx2DHvrQ7c9WA521lGpkLI2sxLWokYVg+Soeg7wQMVTXAC5WAz4/LkBnKpoz5xGMjOOG/WlwhIfcfc97Ezbv7PZEveOVd9DgujMLyDqL0GOp0Bsv0RuPvCrGdLzKVgZ+xT90qebMzArU5w/MGOwSSfh/R5KMo7WwJbkEhp7voGKKpV+pmXr13pPeNA6HWF8RGWIpgwWXRNSz/CiwvSxFU7sFLzovvzgvTtXbcU8nhpcEefDt5kUBcxxPx5m4xUeZEzUu5vYjX6ndu2Hwjfcu98m0i/ncDtxt/20OOjwNZ843bRiOImRlAJiq6E30MF3A=="
```

##### 6. Set SDCT_CONF::
```
Unix: export SDCT_CONF="/Users/snahar/syndicate-tasks/task02/.syndicate-config-dev"
Windows: setx SDCT_CONF /Users/snahar/syndicate-tasks/task02/.syndicate-config-dev
```

```
echo $SDCT_CONF
```

##### 7. Generate lambda:
```
syndicate generate lambda --name hello_world --runtime python
```

##### 8. Create deploy target bucket:
```
syndicate create_deploy_target_bucket
```


##### 9. Syndicate build:
```
syndicate build -v
```

##### 2. Syndicate deploy:
```
syndicate deploy -v
```

##### 2. Activate venv:
```
source .syndicate_venv/bin/activate
```

##### 2. Activate venv:
```
source .syndicate_venv/bin/activate
```

##### 2. Activate venv:
```
source .syndicate_venv/bin/activate
```

##### 2. Activate venv:
```
source .syndicate_venv/bin/activate
```

##### 2. Activate venv:
```
source .syndicate_venv/bin/activate
```

##### 2. Activate venv:
```
source .syndicate_venv/bin/activate
```


