# Instruction tuning an LLM with Lora. Text-to-SQL example

This example is taken from: https://github.com/philschmid/deep-learning-pytorch-huggingface/blob/main/training/fine-tune-llms-in-2024-with-trl.ipynb

This is an up to date example of how to fine-tune models using Lora with Huggingface. The link is well worth a read. 

This is a text to sql using a chat style fine-tuning. Though the example is generic enough that it can be easily adapted to other use-cases. The prepare_data function in the main.py file shows how to prep the data. This has already been run and the data is in the test and train_dataset.json files.

This example will work on an A100 or 4090. Probably will not work on v100 or other older GPU.

## Prerequisites

We need an adequate compute (multi-gpu A100), get a Huggingface access token so we can download models in the jobs, then we need to add the token to the workspace keyvault, finally we need to give the compute access to the keyvault. Follow these steps to make that happen:

1.  Get the access token from huggingface so the code can download the base models. The token from huggingface go to the huggingface website, register, go to your account -> settings -> access tokens
2. Add your hugginface hub key to the azure ml keyvault with name: HUB-TOKEN. But you must first give your microsoft account permissions to add secrets:
    - Go to the KeyVault for the Azure ML Workspace, 
        - On the left panel select "Access Policies" (6th link down). 
        - Then click "+ Create", Secret Permissions "Select All", then click Next, 
        - In the "Principal" panel add your own microsoft account, 
        - on the application panel click Next, 
        - then click "Create"
    - Now add the HUB-TOKEN as a secret. 
        - In the Key Vault home page, select "Secrets" in the left panel, 
        - Press "+ Generate/Import" at the top of the main panel.
        - In the "Create a secret" panel set the "Name" as "HUB-TOKEN",
        - Set the "Secret value" as that from the huggingface website, 
        - click "Create". Done.
3. In the Azure ML Workspace you need to create a cluster machine with System managed identity and then in KeyVault give that identity read secret permissions. This is so the cluster machine can read the keyvault during job runs.
    - In the compute panel of AML, clieck "Create", 
    - Select a Low priority Standard_NC48ads_A100_v4, click Next
    - Add a "compute name"
    - In the advanced settings (just below "Enable SSH access" but above "Add tags"), select "Assign a managed identity"
    - Clieck "Create"
    - When the server appears in the compute list, click on the server name and scroll down to the bottom of the page.
    - In the "managed identity" section copy the Principal ID. This is the Azure AD account name.
    - Add this Principal ID to the KeyVault so that it can access the secrets in the keyvault. You can follow the steps in the previous section used to add permissions to your account to do this.




## To run the Azure ML job:

Step 1: `cd llm`

Step 2: update azure-ml-job.yaml to specify the compute target in your workspace. You need to create a compute or cluster in azure ml for this.

Step 3: Run the job 
`az ml job create -f ./src/instruction_text_to_sql/azure-ml-job.yaml --resource-group RG_NAME --workspace-name WS_NAME`

When the image is built, the job takes about 8-11 mins to run. The finetuning only takes a couple of minutes on the small dataset.

You can specify a different model using the model_name parameter in the azure-ml-job.yaml file. For example, a smaller model is: `"microsoft/phi-2"`. You can find these names from Huggingface model cards.


## Multi-GPU Training

In ./src/finetuning you can run the acclerate commands to parallelise training across multi-gpus on a multi-gpu machine

`az ml job create -f ./src/instruction_text_to_sql/azure-ml-job-multigpu.yaml --resource-group RG_NAME --workspace-name WS_NAME`


