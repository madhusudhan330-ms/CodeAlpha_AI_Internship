import sys
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize required NLP models quietly
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Dataset: Collection of FAQ queries and target responses
faq_data = [
    {
        "question": "What is your return policy?",
        "answer": "You can return any product within 30 days of purchase for a full refund, provided it is in its original packaging."
    },
    {
        "question": "How long does shipping take?",
        "answer": "Standard shipping takes 3-5 business days. Express shipping options deliver within 1-2 business days."
    },
    {
        "question": "How can I track my order?",
        "answer": "Once your order ships, an email containing a tracking link will be sent directly to your registered address."
    },
    {
        "question": "What payment methods do you accept?",
        "answer": "We securely process payments via all major credit cards (Visa, MasterCard, Amex), PayPal, and Apple Pay."
    },
    {
        "question": "How do I contact customer support?",
        "answer": "Our human support team can be reached 24/7 via email at support@example.com or phone at 1-800-555-0199."
    }
]

faq_questions = [item["question"] for item in faq_data]

def preprocess_and_match(user_query):
    # Standardize intent space by evaluation
    all_texts = faq_questions + [user_query]
    
    # Vectorize strings via structural weight matrices
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Calculate angular distance scores (Cosine Similarity)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
    
    # Identify index of closest semantic match
    best_match_idx = similarity_scores.argmax()
    highest_score = similarity_scores[best_match_idx]
    
    # Return answer if confidence passes math threshold (25% similarity match)
    if highest_score > 0.25:
        return faq_data[best_match_idx]["answer"]
    else:
        return "I'm sorry, I couldn't find a matching answer in our database. Could you please rephrase your question?"

def main():
    print("==================================================")
    print("🤖 AI FAQ Chatbot Active (Type 'exit' to quit) 🤖")
    print("==================================================")
    print("Bot: Hello! Ask me anything about our shipping, returns, or payments.")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Bot: Goodbye! Have a wonderful day.")
                break
            
            if not user_input:
                continue
                
            response = preprocess_and_match(user_input)
            print(f"Bot: {response}")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()