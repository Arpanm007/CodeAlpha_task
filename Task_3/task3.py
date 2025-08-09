import os
import shutil
import re
import requests

#task 1: moving .jpg files
def move_jpg_files():
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")

    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            shutil.move(
                os.path.join(source_folder, filename),
                os.path.join(destination_folder, filename)
            )
            moved_count += 1
            print(f"Moved: {filename}")

    print(f"✅ {moved_count} JPG files moved.")

#task 2: extracting emails .txt
def extract_emails():
    input_file = input("Enter the path of the text file: ")
    output_file = input("Enter the output file path to save emails: ")

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}', text)
    emails = list(set(emails))  #to remove duplicates

    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"✅ Extracted {len(emails)} emails and saved to {output_file}")

#task 3: scraping web titles
def scrape_title():
    url = input("Enter the webpage URL: ")
    output_file = input("Enter the output file path to save the title: ")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        html_content = response.text

        match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE)

        if match:
            title = match.group(1).strip()
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(title)
            print(f"Title saved: {title}")
        else:
            print("❌ No title found on the page.")
    except requests.RequestException as e:
        print(f"❌ Error fetching URL: {e}")

#main function
def main():
     while True:
        print("\n📌 Task Automation Menu")
        print("1. Move all .jpg files from one folder to another")
        print("2. Extract all email addresses from a .txt file")
        print("3. Scrape the title of a webpage")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_title()
        elif choice == "4":
            print("👋 Exiting program!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__=="__main__":
    main()