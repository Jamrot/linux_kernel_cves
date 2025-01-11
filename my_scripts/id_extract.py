import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def extract_id(data):
    ids = []
    for cve_id, cve_data in data.items():
        fix_version = cve_data.get('fixes')
        if fix_version and fix_version not in ids:
            ids.append(fix_version)
    return ids

def write_file(file_path, data):
    with open(file_path, 'w') as f:
        for d in data:
            f.write(d + '\n')

def main():
    data = read_json('data/kernel_cves.json')
    ids = extract_id(data)
    write_file('my_scripts/commits.txt', ids)

if __name__ == '__main__':
    main()