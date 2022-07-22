from pathlib import Path

root_dir = Path('./')

pdf_list = sorted(root_dir.glob('scan*.pdf')) + sorted(root_dir.glob('image*.pdf'))

print(pdf_list)