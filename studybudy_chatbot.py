import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('stopwords')

pairs = [
    # Greetings
    (r'hi|hello|hey', ['Hey there! 📘 I\'m StudyBuddy. Need help with your studies today?']),
    (r'how are you?', ['I\'m focused and ready to help you ace your goals!']),
    (r'what is your name?', ['I\'m your friendly Study Buddy chatbot. You can call me StudyBuddy!']),
    
    # Study help
    (r'(.*) study tips(.*)', ['Make a timetable, use Pomodoro technique, and take regular breaks. Want help making a schedule?']),
    (r'how to focus(.*)', ['Try studying in short sessions and turn off distractions. I can suggest a study plan if you want.']),
    (r'(.*) motivate(.*)', ['Remember why you started. Small efforts every day lead to big results! 💪']),
    (r'(.*) exam stress(.*)', ['Breathe deeply, break your revision into chunks, and trust your prep. You got this!']),

    # Subject-specific
    (r'(.*) math(.*)', ['Practice daily, focus on concepts, and solve previous papers. Need resources?']),
    (r'(.*) science(.*)', ['Understand the concepts first, don’t just memorize. I can help with science quizzes too.']),
    (r'(.*) history(.*)', ['Make timelines, use mind maps, and connect events logically. I can share a few tricks.']),

    # Time management
    (r'(.*) time table(.*)', ['Sure! Wake at 6am, study in blocks, and sleep by 10pm. Want a full plan?']),
    (r'(.*) schedule(.*)', ['Use morning for theory, afternoon for revision, and night for light reading. Want a printable planner?']),

    # General queries
    (r'where can I find (.*)', ['I can suggest websites or resources for that subject. Want links to free notes?']),
    (r'(.*) break(.*)', ['Take a 5-10 minute break every 25 minutes. Stretch, walk, or drink water.']), 

    # Motivation
    (r'i feel tired', ['Rest is part of success. Even machines need charging! 🧠']),
    (r'i can\'t do it', ['Yes, you absolutely can! Progress > Perfection. Keep going! 💯']),
    
    # Fallback
    (r'(.*)', ['Hmm... I didn’t catch that. Ask me anything about study tips, subjects, motivation or schedule!'])
]

chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

def start_chat():
    print("Hi! I'm your StudyBuddy 🤓. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("StudyBuddy: 📚 Goodbye! Keep learning and take care!")
            break
        response = chatbot_response(user_input)
        print("StudyBuddy:", response)

if __name__ == "__main__":
    start_chat()
