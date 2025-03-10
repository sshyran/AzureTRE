#!/bin/bash

export TF_LOG=""

# shellcheck disable=SC2154
terraform init -input=false -backend=true -reconfigure \
    -backend-config="resource_group_name=$TF_VAR_mgmt_resource_group_name" \
    -backend-config="storage_account_name=$TF_VAR_mgmt_storage_account_name" \
    -backend-config="container_name=$TF_VAR_terraform_state_container_name" \
    -backend-config="key=${TF_VAR_tre_id}${TF_VAR_workspace_id}${TF_VAR_parent_service_id}guacamolewindowsvm"
terraform plan
terraform apply -auto-approve
