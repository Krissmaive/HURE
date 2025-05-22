import hashlib

# 1. Робота з текстом
def word_count(text):
    words = text.lower().split()
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    frequent_words = [word for word, count in count_dict.items() if count > 3]
    return count_dict, frequent_words

def demo_text_analysis():
    text = "яблуко банан яблуко молоко яблуко яблуко банан молоко"
    count_dict, frequent_words = word_count(text)
    print("Підрахунок слів:", count_dict)
    print("Часто вживані слова:", frequent_words)

if __name__ == "__main__":
    demo_text_analysis()