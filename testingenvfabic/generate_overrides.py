import json

# Load ARM template
with open('./testingenvfabic/TemplateForWorkspace.json') as f:
    template = json.load(f)

# Collect all notebook Spark pool parameter names
params = []
for resource in template.get("resources", []):
    if resource.get("type") == "Microsoft.Synapse/workspaces/notebooks":
        notebook_name = resource["name"].split('/')[-1]  # Get notebook display name
        notebook_name = notebook_name[:-3]
        param_name = f"{notebook_name}_properties_bigDataPool_referenceName"
        params.append(param_name)

# Set the production spark pool name
spark_pool_name = "newpool"

# Generate OverrideArmParameters string
override_str = "\n".join([f"{p}={spark_pool_name}" for p in params])
print(override_str)

# Save to file for GitHub Actions
with open("override.txt", "w") as f:
    f.write(override_str)
