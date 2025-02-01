import requests
import os

GITHUB_TOKEN = 'YOURS_TOKEN_HERE!!'

def get_default_branch(github_repo_url):
    parts = github_repo_url.strip('/').split('/')
    username, repo_name = parts[-2], parts[-1]
    
    api_url = f'https://api.github.com/repos/{username}/{repo_name}'
    
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'  
    }
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info['default_branch']
    else:
        print(f"Error: {response.status_code}")
        return None

def get_repo_files(github_repo_url, branch):
    parts = github_repo_url.strip('/').split('/')
    username, repo_name = parts[-2], parts[-1]
    
    api_url = f'https://api.github.com/repos/{username}/{repo_name}/contents'
    
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'  
    }
    
    files = []
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        items = response.json()
        for item in items:
            if item['type'] == 'dir':
                folder_files = get_repo_files_from_subfolder(username, repo_name, item['path'], branch)
                files.extend(folder_files)
            elif item['type'] == 'file':
                files.append(item)
    else:
        print(f"Error: {response.status_code}")
    
    return files

def get_repo_files_from_subfolder(username, repo_name, folder_path, branch):
    api_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{folder_path}'
    
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'  
    }
    
    response = requests.get(api_url, headers=headers)
    
    files = []
    if response.status_code == 200:
        items = response.json()
        for item in items:
            if item['type'] == 'dir':
                files.extend(get_repo_files_from_subfolder(username, repo_name, item['path'], branch))
            elif item['type'] == 'file':
                files.append(item)
    
    return files

def convert_to_jsdelivr(github_url, branch):
    github_url = github_url.replace('https://github.com/', '')
    
    parts = github_url.split('/')
    
    username = parts[0]
    repo_name = parts[1]
    file_path = '/'.join(parts[4:])
    
    jsdelivr_url = f'https://cdn.jsdelivr.net/gh/{username}/{repo_name}@{branch}/{file_path}'
    return jsdelivr_url

def save_to_log(file_name, content):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    with open(f'logs/{file_name}.txt', 'a') as log_file:
        log_file.write(content + "\n")

def main():
    github_repo_url = input("Masukkan link GitHub repository: ")

    branch = get_default_branch(github_repo_url)
    if not branch:
        print("Tidak dapat mengambil branch default.")
        return

    files = get_repo_files(github_repo_url, branch)

    if not files:
        print("Repository tidak ditemukan atau tidak ada file.")
        return

    css_js_files = [file for file in files if file['type'] == 'file' and (file['name'].endswith('.css') or file['name'].endswith('.js'))]

    print(f"\nDitemukan {len(css_js_files)} file CSS dan JS.")

    file_name = f"file_links_{github_repo_url.split('/')[-1]}"
    save_to_log(file_name, f"Ditemukan {len(css_js_files)} file CSS dan JS di repository {github_repo_url}:\n")

    print("\nDaftar file CSS dan JS yang ditemukan:")
    for i, file in enumerate(css_js_files, start=1):
        github_url = file['html_url']
        print(f"[{i}] Link GitHub: {github_url}")
        save_to_log(file_name, f"[{i}] GitHub Link: {github_url}")

    while True:
        choice = input("\nMasukkan nomor file yang ingin dikonversi ke JSDelivr (pisahkan dengan koma, ketik 'allKonfersi' untuk semua): ").strip().lower()
        
        if choice == 'allkonfersi':
            print("\nKonversi semua file ke JSDelivr:")
            for i, file in enumerate(css_js_files, start=1):
                github_url = file['html_url']
                jsdelivr_url = convert_to_jsdelivr(github_url, branch)
                print(f"[{i}] GitHub JSDelivr: {jsdelivr_url}")
                save_to_log(file_name, f"[{i}] GitHub JSDelivr: {jsdelivr_url}")
            break
        else:
            try:
                selected_files = [int(num) for num in choice.split(',') if num.strip().isdigit()]
                print("\nKonversi file yang dipilih ke JSDelivr:")
                for num in selected_files:
                    if 1 <= num <= len(css_js_files):
                        github_url = css_js_files[num - 1]['html_url']
                        jsdelivr_url = convert_to_jsdelivr(github_url, branch)
                        print(f"[{num}] GitHub JSDelivr: {jsdelivr_url}")
                        save_to_log(file_name, f"[{num}] GitHub JSDelivr: {jsdelivr_url}")
                    else:
                        print(f"Nomor {num} tidak valid.")
                break
            except ValueError:
                print("Input tidak valid. Masukkan nomor yang benar.")

    print("\nHasil telah disimpan di folder 'logs'. Selesai!")

if __name__ == "__main__":
    main()
