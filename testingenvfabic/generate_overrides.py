import json

# Load ARM template
with open('./testingenvfabic/TemplateForWorkspace.json') as f:
    template = json.load(f)

# Collect all notebook Spark pool parameter names
params = {}
for resource in template.get("resources", []):
    if resource.get("type") == "Microsoft.Synapse/workspaces/notebooks":
        notebook_name = resource["name"].split('/')[-1]  # Get notebook display name
        notebook_name = notebook_name[:-3]
        param_name = f"{notebook_name}_properties_bigDataPool_referenceName"
        params[param_name] = {"value": "newpool"}  # JSON format

# Save JSON to override.txt
with open("override.json", "w") as f:
    json.dump(params, f, indent=2)
