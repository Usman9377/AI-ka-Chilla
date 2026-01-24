import json
import os

def reduce_notebook_size(input_path, output_path):
    """
    Reduce notebook size by clearing output cells with large images
    while keeping code cells intact
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells_modified = 0
    original_size = os.path.getsize(input_path)
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Check if outputs exist and contain large data
            if 'outputs' in cell and cell['outputs']:
                for output in cell['outputs']:
                    # Clear image/png data which is usually very large
                    if 'data' in output and 'image/png' in output['data']:
                        # Keep a small placeholder instead of removing completely
                        output['data']['image/png'] = ''
                        cells_modified += 1
                    
                    # Also clear any large text outputs (keep only first 1000 chars)
                    if 'text' in output and isinstance(output['text'], list):
                        if len(''.join(output['text'])) > 1000:
                            output['text'] = ['Output cleared to reduce file size\n']
    
    # Save the modified notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    new_size = os.path.getsize(output_path)
    reduction = ((original_size - new_size) / original_size) * 100
    
    print(f"Original size: {original_size / 1024:.2f} KB")
    print(f"New size: {new_size / 1024:.2f} KB")
    print(f"Reduction: {reduction:.2f}%")
    print(f"Cells modified: {cells_modified}")
    
    return new_size < 1024 * 1024  # Return True if under 1MB

if __name__ == "__main__":
    input_file = "data_visualization.ipynb"
    output_file = "data_visualization_optimized.ipynb"
    
    success = reduce_notebook_size(input_file, output_file)
    
    if success:
        print(f"\n✓ Notebook successfully reduced to under 1MB!")
        print(f"✓ Optimized file saved as: {output_file}")
    else:
        print(f"\n⚠ Warning: File is still over 1MB. Further optimization needed.")
