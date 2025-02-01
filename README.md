# 🎉 **Welcome to JSDeliver Link Generator!** 🎉

🚀 **Want to quickly convert CSS or JS links from your GitHub repository to JSDelivr links**? No need to do it one by one, this tool is here to help you do it in bulk with just a few simple steps! 💻🔗

## 🛠️ How to Use

### 1. Clone the repository 🧑‍💻

First, clone the repository to your local machine:

```bash
git clone https://github.com/ridwan-arch-v/jsDeliverLinkGenerators
```

### 2. Navigate to the tools folder 🔄

After cloning, navigate to the `tools` folder:

```bash
cd jsDeliverLinkGenerators/tools
```

### 3. Add your **Personal Access Token (PAT)** 🔑

You’ll need to generate a GitHub **Personal Access Token (PAT)** and insert it in the script. 

Open the script and set your token like this:

```python
GITHUB_TOKEN = 'YOURS_TOKEN_HERE!!'  # Add your GitHub token here
```

### 4. Run the script 🏃‍♂️

Execute the script to get started:

```bash
python glink.py
```

### 5. Enter your repository link 🔗

The script will ask for your GitHub repository link. Just copy and paste it when prompted!

### 6. Troubleshooting  🚧

If you get a `403` error, it means your token doesn’t have the necessary permissions. 🛑 Create a new **Personal Access Token (PAT)** with the right scopes and try again. Make sure to check all the important permissions when generating the token. ✅

### 7. Convert links 📤

Once you’ve successfully run the script, it will output a list of files with numbers. You can then convert them to **JSDelivr links**! 🧳🌍

### 8. Choose files to convert 🔥

- To convert **all files**, type: 

```bash
allkonfersi
```

- To convert **one file**, just type its number (e.g., `2`):

```bash
2
```

- To convert **multiple files**, enter the numbers separated by commas (e.g., `1, 5, 9`):

```bash
1, 5, 9
```

### 🎉 Done! 🎉

Once you’ve made your choice, the tool will generate the **JSDelivr links** for you, and you’re all set! 🌟

Enjoy converting your files like a pro! 💪

If you have any questions or run into any issues, feel free to open an issue on the repository. 🚨

Happy coding! 💻✨