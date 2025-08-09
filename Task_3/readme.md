Here’s a **README.md** for your **Task Automation Script** in Markdown format:

````markdown
# 🛠️ Python Task Automation Script

A multi-functional Python script that automates **three common tasks**:  
1. Moving `.jpg` files between folders  
2. Extracting email addresses from a `.txt` file  
3. Scraping the `<title>` of a webpage  

---

## 📌 Features
### 1️⃣ Move `.jpg` Files
- Moves all `.jpg` files from a source folder to a destination folder.
- Creates the destination folder if it doesn't exist.
- Displays the number of files moved.

### 2️⃣ Extract Emails from `.txt` Files
- Reads a `.txt` file.
- Finds and extracts all **valid email addresses**.
- Removes duplicates.
- Saves the extracted emails to a new `.txt` file.

### 3️⃣ Scrape Webpage Title
- Fetches the HTML of a given webpage.
- Extracts the `<title>` tag content.
- Saves it to a file.

---

## 🛠️ Requirements
- Python 3.x  
- `requests` library (install with `pip install requests`)

---

## 🚀 How to Run
1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/task-automation-script.git
   cd task-automation-script
````

2. **Install required dependencies**

   ```bash
   pip install requests
   ```

3. **Run the script**

   ```bash
   python automation.py
   ```

---

## 📂 Usage Menu

When you run the script, you’ll see:

```
📌 Task Automation Menu
1. Move all .jpg files from one folder to another
2. Extract all email addresses from a .txt file
3. Scrape the title of a webpage
4. Exit
```

### Example 1: Move `.jpg` Files

```
Enter the source folder path: C:\Users\Me\Pictures
Enter the destination folder path: C:\Users\Me\Desktop\JPG_Files
✅ 5 JPG files moved.
```

### Example 2: Extract Emails

```
Enter the path of the text file: emails.txt
Enter the output file path to save emails: extracted_emails.txt
✅ Extracted 12 emails and saved to extracted_emails.txt
```

### Example 3: Scrape Webpage Title

```
Enter the webpage URL: https://example.com
Enter the output file path to save the title: title.txt
Title saved: Example Domain
```

---

## 📂 File Structure

```
task-automation-script/
│
├── automation.py   # Main script
└── README.md       # Documentation
```

---

## 📜 License

This project is licensed under the **MIT License** — you can use, modify, and share it.

```