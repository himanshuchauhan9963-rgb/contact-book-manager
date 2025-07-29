import string

def clean_text(text):
    # Remove punctuation and convert to lowercase
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def word_frequency(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            cleaned_text = clean_text(text)
            words = cleaned_text.split()
            
            freq = {}
            for word in words:
                freq[word] = freq.get(word, 0) + 1
            
            # Sort by frequency
            sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

            print("📈 Top 5 Most Frequent Words:\n")
            for word, count in sorted_freq[:5]:
                print(f"{word} → {count} times")
    
    except FileNotFoundError:
        print("❌ File not found. Please check the file path.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the path to your text file: ")
    word_frequency(filename)
