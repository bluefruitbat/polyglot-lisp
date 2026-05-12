#!/usr/bin/env python3
"""
generate-mental-models-compose.py

Updated script to manage the per-model structure and produce docker-compose.yml
for running all mental models in isolated containers.
"""

import os
from pathlib import Path
import yaml

def generate_compose():
    models_dir = Path('mental_models')
    if not models_dir.exists():
        print('No mental_models directory found.')
        return

    services = {}
    for model_dir in models_dir.iterdir():
        if model_dir.is_dir():
            model_name = model_dir.name
            services[model_name] = {
                'build': {
                    'context': f'./mental_models/{model_name}',
                    'dockerfile': 'Dockerfile'
                },
                'container_name': f'mental-model-{model_name}',
                # No shared volumes or networks beyond default
                # Explicitly isolated
            }

    compose_config = {
        'version': '3.8',
        'services': services
    }

    with open('docker-compose.yml', 'w') as f:
        yaml.dump(compose_config, f, default_flow_style=False)

    print(f'Generated docker-compose.yml with {len(services)} mental models.')
    print('Models are completely self-contained as per specification.')

if __name__ == '__main__':
    generate_compose()

# To use: python generate-mental-models-compose.py
# Then: docker compose up
